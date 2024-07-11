from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class StarCatalog:
    def __init__(self, root):
        self.root = root
        self.root.title("Stellar Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        # Definir las variables de instancia
        self.name = StringVar()
        self.catalog = StringVar()
        self.constellation = StringVar()
        self.spectral = StringVar()
        self.distance = StringVar()
        self.radius = StringVar()
        self.mass = StringVar()
        self.visibility = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.selected_id = None

        validate_cmd = self.root.register(self.validate_float_input)

        # Título
        lbltitle = Label(self.root, bd=6, relief=GROOVE, text="STELLAR MANAGEMENT SYSTEM", fg="white", bg="blue", font=("Algerian", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Pie de página
        lblfooter = Label(self.root, bd=3, relief=GROOVE, text="Developed by mateosolinho", fg="white", bg="blue", font=("Brush Script MT", 18))
        lblfooter.pack(side=BOTTOM, fill=X)

        # DataframeLeft
        DataframeLeft = Label(self.root, bd=4, relief=RIDGE, bg='light blue')
        DataframeLeft.place(x=15, y=70, width=460, height=580)

        titleDataframeLeft = Label(DataframeLeft, text="Manage Stars", bg="light blue", fg="black", font=("Brush Script MT", 24, "bold"))
        titleDataframeLeft.grid(row=0, columnspan=2, pady=10)

        lblName = Label(DataframeLeft, text="Name", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblName.grid(row=1, column=0, pady=10, padx=40, sticky='w')
        txtName = Entry(DataframeLeft, textvariable=self.name, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtName.grid(row=1, column=1, pady=10, padx=5, sticky='w')

        lblCatalog = Label(DataframeLeft, text="Catalog", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblCatalog.grid(row=2, column=0, pady=10, padx=40, sticky='w')
        txtCatalog = Entry(DataframeLeft, textvariable=self.catalog, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtCatalog.grid(row=2, column=1, pady=10, padx=5, sticky='w')

        lblConst = Label(DataframeLeft, text="Constellation", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblConst.grid(row=3, column=0, pady=10, padx=40, sticky='w')
        txtConst = Entry(DataframeLeft, textvariable=self.constellation, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtConst.grid(row=3, column=1, pady=10, padx=5, sticky='w')

        lblEspectral = Label(DataframeLeft, text="Spectral Type", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblEspectral.grid(row=4, column=0, pady=10, padx=40, sticky='w')
        txtEspectral = Entry(DataframeLeft, textvariable=self.spectral, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtEspectral.grid(row=4, column=1, pady=10, padx=5, sticky='w')

        lblDistance = Label(DataframeLeft, text="Distance", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblDistance.grid(row=5, column=0, pady=10, padx=40, sticky='w')
        txtDistance = Entry(DataframeLeft, textvariable=self.distance, font=('times new roman', 14), bd=2, relief=GROOVE, validate="key", validatecommand=(validate_cmd, "%P"))
        txtDistance.grid(row=5, column=1, pady=10, padx=5, sticky='w')

        lblRadius = Label(DataframeLeft, text="Radius", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblRadius.grid(row=6, column=0, pady=10, padx=40, sticky='w')
        txtRadius = Entry(DataframeLeft, textvariable=self.radius, font=('times new roman', 14), bd=2, relief=GROOVE, validate="key", validatecommand=(validate_cmd, "%P"))
        txtRadius.grid(row=6, column=1, pady=10, padx=5, sticky='w')

        lblMass = Label(DataframeLeft, text="Mass", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblMass.grid(row=7, column=0, pady=10, padx=40, sticky='w')
        txtMass = Entry(DataframeLeft, textvariable=self.mass, font=('times new roman', 14), bd=2, relief=GROOVE, validate="key", validatecommand=(validate_cmd, "%P"))
        txtMass.grid(row=7, column=1, pady=10, padx=5, sticky='w')

        lblVisibility = Label(DataframeLeft, text="Visibility", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblVisibility.grid(row=8, column=0, pady=10, padx=40, sticky='w')
        txtVisibility = Entry(DataframeLeft, textvariable=self.visibility, font=('times new roman', 14), bd=2, relief=GROOVE, validate="key", validatecommand=(validate_cmd, "%P"))
        txtVisibility.grid(row=8, column=1, pady=10, padx=5, sticky='w')

        # ButtonFrame
        Buttonframe = Frame(DataframeLeft, bd=4, relief=RIDGE, bg='white')
        Buttonframe.place(x=10, y=500, width=425)

        btnAdd = Button(Buttonframe, text="Add", width=10, command=self.add_stars)
        btnAdd.grid(row=0, column=0, padx=10, pady=10)
        btnUpdate = Button(Buttonframe, text="Update", width=10, command=self.update_data)
        btnUpdate.grid(row=0, column=1, padx=10, pady=10)
        btnDelete = Button(Buttonframe, text="Delete", width=10,command=self.delete_data)
        btnDelete.grid(row=0, column=2, padx=10, pady=10)
        btnClear = Button(Buttonframe, text="Clear", width=10, command=self.clear)
        btnClear.grid(row=0, column=3, padx=10, pady=10)

        # DataframeRight
        DataframeRight = Label(self.root, bd=4, relief=RIDGE, bg='light blue')
        DataframeRight.place(x=500, y=70, width=825, height=580)

        lblSearch = Label(DataframeRight, text="Search By", bg="light blue", fg="black", font=("times new roman", 16, 'bold'))
        lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        comboSearch = ttk.Combobox(DataframeRight, width=10, textvariable=self.search_by, font=("times new roman", 12, 'bold'), state='readonly')
        comboSearch['values'] = ("Name", "Catalog", "Constellation", "Espectral Type", "Distance", "Radius", "Mass", "Visibility")
        comboSearch.current(0)
        comboSearch.grid(row=0, column=1, pady=10, padx=20)

        txtSearch = Entry(DataframeRight,width=30,textvariable=self.search_txt,font=('times new roman',14),bd=2,relief=GROOVE)
        txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(DataframeRight,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(DataframeRight,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        # =================================Table=================================

        FrameTable = Frame(DataframeRight,bd=2,relief=RIDGE,bg='light blue')
        FrameTable.place(x=10,y=80,width=785,height=480)

        scroll_x = Scrollbar(FrameTable,orient="horizontal")
        scroll_y = Scrollbar(FrameTable,orient="vertical")
        self.stars_table = ttk.Treeview(FrameTable,columns=("id","name","catalog","constellation","spectral","distance","radius","mass","visibility"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.stars_table.xview)
        scroll_y.config(command=self.stars_table.yview)

        self.stars_table.heading("id",text="ID")
        self.stars_table.heading("name",text="Name")
        self.stars_table.heading("catalog",text="Catalog")
        self.stars_table.heading("constellation",text="Constellation")
        self.stars_table.heading("spectral",text="Spectral Type")
        self.stars_table.heading("distance",text="Distance")
        self.stars_table.heading("radius",text="Radius")
        self.stars_table.heading("mass",text="Mass")
        self.stars_table.heading("visibility",text="Visibility")

        self.stars_table['show']='headings'

        self.stars_table.column("id",width=20)
        self.stars_table.column("name",width=60)
        self.stars_table.column("catalog",width=80)
        self.stars_table.column("constellation",width=80)
        self.stars_table.column("spectral",width=50)
        self.stars_table.column("distance",width=50)
        self.stars_table.column("radius",width=50)
        self.stars_table.column("mass",width=30)
        self.stars_table.column("visibility",width=30)
        self.stars_table.pack(fill=BOTH,expand=1)
        self.stars_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stars")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.stars_table.delete(*self.stars_table.get_children())
            for i in rows:
                self.stars_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def delete_data(self):
        if self.name.get() == "":
            messagebox.showerror("Error", "Name field is required to delete a record.")
            return

        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
    
        try:
            my_cursor.execute("DELETE FROM stars WHERE id=%s", (self.selected_id,))
            conn.commit()

            if my_cursor.rowcount > 0:
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success", "Record has been deleted successfully.")
            else:
                messagebox.showwarning("Warning", "No record found with the provided ID.")
    
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    
        finally:
            conn.close()

    def get_cursor(self, event):
        cursor_row = self.stars_table.focus()
        content = self.stars_table.item(cursor_row)
        row = content['values']
        self.selected_id = row[0]  # Asignar el id de la fila seleccionada
        self.name.set(row[1])
        self.catalog.set(row[2])
        self.constellation.set(row[3])
        self.spectral.set(row[4])
        self.distance.set(row[5])
        self.radius.set(row[6])
        self.mass.set(row[7])
        self.visibility.set(row[8])

    def add_stars(self):
        if self.name.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("""CREATE TABLE IF NOT EXISTS Stars ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, catalog VARCHAR(255), constellation VARCHAR(255), spectral VARCHAR(255), distance DOUBLE, radius DOUBLE, mass DOUBLE, visibility DOUBLE);""")

            my_cursor.execute("insert into stars (name, catalog, constellation, spectral, distance, radius, mass, visibility) values (%s, %s, %s, %s, %s, %s, %s, %s)", (
                self.name.get(),
                self.catalog.get(),
                self.constellation.get(),
                self.spectral.get(),
                self.distance.get(),
                self.radius.get(),
                self.mass.get(),
                self.visibility.get(),
            ))

            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted sucessfully")

    def clear(self):
        self.name.set("")
        self.catalog.set("")
        self.constellation.set("")
        self.spectral.set("")
        self.distance.set("")
        self.radius.set("")
        self.mass.set("")
        self.visibility.set("")
        self.selected_id = None

    def update_data(self):
        if self.selected_id is None:
            messagebox.showerror("Error", "Select a record to update.")
            return

        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()

        try:
            my_cursor.execute("""UPDATE stars SET name = %s, catalog = %s, constellation = %s, spectral = %s, distance = %s, radius = %s, mass = %s, visibility = %s WHERE id = %s """, (
            self.name.get(),
            self.catalog.get(),
            self.constellation.get(),
            self.spectral.get(),
            self.distance.get(),
            self.radius.get(),
            self.mass.get(),
            self.visibility.get(),
            self.selected_id
            ))

            conn.commit()
            if my_cursor.rowcount > 0:
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success", "Record has been updated successfully.")
            else:
                messagebox.showwarning("Warning", "No record found with the provided ID.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            conn.close()

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor() 
        my_cursor.execute("select * from stars where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.stars_table.delete(*self.stars_table.get_children())
            for row in rows:
                self.stars_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Info", "No records found.")
        conn.close()

    def validate_float_input(self, value):
        if value == "" or value.replace('.', '', 1).isdigit():
            return True
        return False
        
# Crear la ventana principal y ejecutar la aplicación
root = Tk()
object = StarCatalog(root)
root.mainloop()
