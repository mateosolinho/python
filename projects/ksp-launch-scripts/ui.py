import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import krpc
import time
import subprocess
import threading
import io
import sys
import os
import signal

class TelemetriaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.conn = krpc.connect(name='Telemetria Espacial')
        self.vessel = self.conn.space_center.active_vessel

        # Configuración básica de la ventana principal
        self.title("Telemetría Espacial")
        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Establecer el tamaño de la ventana al tamaño de la pantalla
        self.geometry(f"{screen_width}x{screen_height - 20}")
        
        # Opcional: Evitar que el usuario redimensione la ventana
        self.resizable(False, False)
        self.configure(bg='black')

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Variables inicializadas para evitar errores
        self.altitude = 0
        self.speed = 0
        self.apoapsis = 0
        self.flight_plan = None  # Variable para almacenar el plan de vuelo cargado

        # Inicialización de variables para los límites de los gráficos
        self.altitude_min = 0
        self.altitude_max = 10000
        self.speed_min = 0
        self.speed_max = 2500
        self.g_force_max = 10

        # Tiempo de misión
        self.mission_start_time = None  # Tiempo en que se activa el motor
        self.current_time = 0  # Tiempo actual en segundos desde el inicio
        self.mission_started = False  # Controlar si la misión ha comenzado

        # Panel de estado de misión
        self.mission_status_frame = ttk.Frame(self, relief=tk.RAISED)
        self.mission_status_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.mission_status_label = tk.Label(self.mission_status_frame, text="Misión: SPACEX-01 | Estado: En curso",
                                             font=("Courier", 20), fg="white", bg="black")
        self.mission_status_label.pack(side=tk.TOP, pady=5)

        # Panel de visualización de gráficos en tiempo real
        self.graph_frame = ttk.Frame(self, relief=tk.RAISED)
        self.graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_real_time_graphs()

        # Panel de datos detallados
        self.data_frame = ttk.Frame(self, relief=tk.RAISED)
        self.data_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        self.create_data_labels()

        # Panel de control
        self.control_frame = ttk.Frame(self, relief=tk.RAISED)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.create_control_buttons()

        # Consola de eventos
        self.console_frame = ttk.Frame(self, relief=tk.RAISED)
        self.console_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.create_event_console()

        # Variable para detener la actualización de gráficos cuando sea necesario
        self.update_id = None  # Variable para almacenar el identificador del 'after'

        # Inicializar proceso de vuelo
        self.flight_plan_process = None  # Proceso del plan de vuelo

        # Iniciar la actualización de datos
        self.update_data()

    def create_real_time_graphs(self):
        """Crea los gráficos en tiempo real con ajustes para ejes X e Y específicos."""
        self.fig, self.ax = plt.subplots(3, 1, figsize=(7, 8))
        self.fig.tight_layout(pad=3.0)

        self.lines = []
        self.titles = ["Altitud", "Velocidad", "G Force"]

        for i, axis in enumerate(self.ax):
            axis.set_title(f"{self.titles[i]}")
            axis.set_xlabel("Tiempo (s)")
            axis.set_ylabel(self.titles[i])
            axis.set_xlim(0, 1)  # Inicialmente, establecer un rango mínimo
            if i == 0:  # Altitud
                axis.set_ylim(self.altitude_min, self.altitude_max)
            elif i == 1:  # Velocidad
                axis.set_ylim(self.speed_min, self.speed_max)
            elif i == 2:  # G Force
                axis.set_ylim(0, self.g_force_max)
            line, = axis.plot([], [], lw=2)
            self.lines.append(line)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def create_data_labels(self):
        labels = ["Velocidad (m/s)", 'V Speed (m/s)', 'H Speed (m/s)' , "Aceleración (m/s²)", "Combustible (L)", "Estado del Motor", "G Force", "GPS (Lat, Lon)", "Pitch", "Heading", "Roll"]
        self.data_vars = [tk.StringVar(value="0") for _ in labels]
        for i, label in enumerate(labels):
            label_widget = ttk.Label(self.data_frame, text=label, font=("Courier", 14), background="black", foreground="white")
            label_widget.grid(row=i, column=0, sticky=tk.W, pady=10)
            data_widget = ttk.Label(self.data_frame, textvariable=self.data_vars[i], font=("Courier", 14), background="black", foreground="lightgreen")
            data_widget.grid(row=i, column=1, sticky=tk.E, pady=10)

    def create_control_buttons(self):
        # Botones de control básicos
        ttk.Button(self.control_frame, text="Seleccionar Plan de Vuelo", command=self.select_flight_plan).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.control_frame, text="Iniciar", command=self.start_mission).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(self.control_frame, text="Restablecer", command=self.reset_all).grid(row=0, column=4, padx=10, pady=10)
        # ttk.Button(self.control_frame, text="Pausar", command=self.pause_mission).grid(row=0, column=2, padx=10, pady=10)
        # ttk.Button(self.control_frame, text="Finalizar", command=self.end_mission).grid(row=0, column=3, padx=10, pady=10)

    def create_event_console(self):
        # Consola para mostrar eventos
        console_label = tk.Label(self.console_frame, text="Consola de Eventos", font=("Courier", 14), fg="white", bg="black")
        console_label.pack(side=tk.TOP, pady=5)
        
        self.console_text = tk.Text(self.console_frame, height=10, font=("Courier", 12), bg="black", fg="lightgreen")
        self.console_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.console_text.insert(tk.END, "Esperando eventos...\n")
        self.console_text.config(state=tk.DISABLED)

    def select_flight_plan(self):
        """Permite al usuario seleccionar un archivo de plan de vuelo y ejecutarlo."""
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py"), ("Todos los Archivos", "*.*")])
        if file_path:
            self.flight_plan = file_path
            self.add_event_to_console(f"Plan de vuelo cargado: {self.flight_plan}")

    def update_data(self):
        """Función para actualizar los datos de forma periódica."""
        # Obtener datos de telemetría desde kRPC
        altitude = self.vessel.flight().mean_altitude
        h_speed = self.vessel.flight().horizontal_speed
        v_speed = self.vessel.flight().vertical_speed
        g_force = self.vessel.flight().g_force
        pitch = self.vessel.flight().pitch
        heading = self.vessel.flight().heading
        roll = self.vessel.flight().roll
        speed = self.vessel.flight(self.vessel.orbit.body.reference_frame).speed
        apoapsis = self.vessel.orbit.apoapsis_altitude
        fuel = self.vessel.resources.amount('LiquidFuel')
        acceleration = self.vessel.flight().g_force
        lat, lon = self.vessel.flight().latitude, self.vessel.flight().longitude

        # Detectar la activación del motor (o la primera etapa)
        if not self.mission_started and self.vessel.control.throttle > 0:
            self.mission_start_time = time.time()
            self.mission_started = True

        # Actualizar el tiempo actual desde el inicio de la misión
        if self.mission_start_time:
            self.current_time = time.time() - self.mission_start_time

        # Solo actualizar gráficos si la misión ha comenzado
        if self.mission_started:
            self.update_graphs([altitude, speed, g_force])

        # Actualizar datos detallados
        self.data_vars[0].set(f"{speed:.2f}")
        self.data_vars[1].set(f"{v_speed:.2f}")
        self.data_vars[2].set(f"{h_speed:.2f}")
        self.data_vars[3].set(f"{acceleration:.2f}")
        self.data_vars[4].set(f"{fuel:.2f}")
        self.data_vars[5].set("Activo" if self.vessel.control.throttle > 0 else "Inactivo")
        self.data_vars[6].set(f"{g_force:.2f}")
        self.data_vars[7].set(f"{lat:.2f}, {lon:.2f}")
        self.data_vars[8].set(f"{pitch:.2f}")
        self.data_vars[9].set(f"{heading:.2f}")
        self.data_vars[10].set(f"{roll:.2f}")

        # Volver a llamar a esta función después de 1 segundo
        self.update_id = self.after(1000, self.update_data)

    def update_graphs(self, new_data):
        """Actualiza los gráficos con los nuevos datos y ajusta dinámicamente los límites del eje Y."""
        for i, line in enumerate(self.lines):
            x_data = list(line.get_xdata())  # Mantener todos los puntos
            y_data = list(line.get_ydata())
            x_data.append(self.current_time)  # Usa el tiempo actual como x_data
            y_data.append(new_data[i])

            # Ajustar límites con margen adicional
            if i == 0:  # Altitud
                self.altitude_max = max(self.altitude_max, max(y_data))
                self.altitude_min = min(self.altitude_min, min(y_data))
                self.ax[i].set_ylim(self.altitude_min, self.altitude_max * 1.1)  # Márgenes del 10%
            elif i == 1:  # Velocidad
                self.speed_max = max(self.speed_max, max(y_data))
                self.speed_min = min(self.speed_min, min(y_data))
                self.ax[i].set_ylim(self.speed_min, self.speed_max * 1.1)  # Márgenes del 10%
            elif i == 2:  # G Force
                self.g_force_max = max(self.g_force_max, max(y_data))
                self.ax[i].set_ylim(0, self.g_force_max * 1.1)  # Márgenes del 10%

            line.set_data(x_data, y_data)
            self.ax[i].set_xlim(x_data[0], x_data[-1])  # Ajustar el límite del eje X al rango de los datos
        
        self.canvas.draw()

    def add_event_to_console(self, event_text):
        """Añadir un evento a la consola de eventos."""
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, f"{event_text}\n")
        self.console_text.see(tk.END)  # Scroll automático
        self.console_text.config(state=tk.DISABLED)

    def start_mission(self):
        """Iniciar la misión y ejecutar el plan de vuelo en un hilo separado."""
        if self.flight_plan:
            self.add_event_to_console("Misión iniciada.")

            # Ejecutar el plan de vuelo en un hilo separado
            threading.Thread(target=self.run_flight_plan, daemon=True).start()

        else:
            self.add_event_to_console("No se ha cargado un plan de vuelo. Seleccione uno primero.")

    def pause_mission(self):
        """Pausar la misión."""
        self.add_event_to_console("Misión pausada.")

    def end_mission(self):
        """Finalizar la misión."""
        self.add_event_to_console("Misión finalizada.")
        
    def reset_all(self):
        """Restablecer todas las gráficas, números y la consola."""
        # Limpiar las gráficas
        self.clear_graphs()

        # Restablecer los números
        self.reset_data_labels()

        # Limpiar la consola
        self.clear_console()

        # Reiniciar la misión
        self.mission_start_time = None
        self.current_time = 0
        self.mission_started = False

        # Terminar el proceso de vuelo si está en ejecución
        if self.flight_plan_process:
            self.terminate_flight_plan()

    def clear_graphs(self):
        """Limpia todas las gráficas."""
        for line in self.lines:
            line.set_data([], [])
        for axis in self.ax:
            axis.set_ylim(0, 1)  # Configura un rango por defecto, puede ajustarse si es necesario
            axis.set_xlim(0, 1)  # Configura un rango por defecto, puede ajustarse si es necesario
        self.canvas.draw()

    def reset_data_labels(self):
        """Restablece todos los valores de las etiquetas de datos a 0."""
        for var in self.data_vars:
            var.set("0")

    def clear_console(self):
        """Limpia el texto en la consola de eventos."""
        self.console_text.config(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        self.console_text.insert(tk.END, "Consola de eventos reiniciada...\n")
        self.console_text.config(state=tk.DISABLED)


    def run_flight_plan(self):
        """Ejecuta el plan de vuelo en un hilo separado y captura la salida en tiempo real."""
        try:
            self.flight_plan_process = subprocess.Popen(
                ['python', '-u', self.flight_plan],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            def read_stream(stream, label):
                for line in iter(stream.readline, ''):
                    if line:
                        self.add_event_to_console(f"{line.strip()}")
                stream.close()

            # Iniciar hilos para leer stdout y stderr en tiempo real
            stdout_thread = threading.Thread(target=read_stream, args=(self.flight_plan_process.stdout, "Output"), daemon=True)
            stderr_thread = threading.Thread(target=read_stream, args=(self.flight_plan_process.stderr, "Error"), daemon=True)
            
            stdout_thread.start()
            stderr_thread.start()

            # Esperar a que el proceso termine
            self.flight_plan_process.wait()

            # Esperar a que los hilos terminen
            stdout_thread.join()
            stderr_thread.join()

        except Exception as e:
            self.add_event_to_console(f"Error al ejecutar el plan de vuelo: {e}")

    def on_closing(self):
        """Método llamado al cerrar la ventana."""
        try:
            self.conn.close()
        except Exception as e:
            print(f"Error al cerrar kRPC: {e}")

        if self.update_id is not None:
            self.after_cancel(self.update_id)  # Cancelar la actualización periódica
        
        # Terminar cualquier proceso de plan de vuelo que esté corriendo
        if self.flight_plan_process:
            self.terminate_flight_plan()

        # Asegurarse de que los hilos de lectura de stdout y stderr se cierren correctamente
        for thread in threading.enumerate():
            if thread is not threading.current_thread():
                try:
                    thread.join(timeout=1)  # Espera a que el hilo termine con un timeout de 1 segundo
                except RuntimeError:
                    pass  # Maneja hilos que no respondan

        self.destroy()  # Destruir la ventana
        
        os._exit(0)  # Forzar la salida del programa


    def terminate_flight_plan(self):
        """Terminación forzada del proceso del plan de vuelo."""
        if self.flight_plan_process:
            try:
                # Enviar una señal SIGKILL al proceso hijo
                os.kill(self.flight_plan_process.pid, signal.SIGKILL)
                self.add_event_to_console("Proceso del plan de vuelo terminado de manera forzada.")
            except Exception as e:
                self.add_event_to_console(f"Error al terminar el proceso del plan de vuelo: {e}")

if __name__ == "__main__":
    app = TelemetriaApp()
    app.mainloop()
