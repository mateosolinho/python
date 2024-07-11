import csv
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from fpdf import FPDF
from datetime import datetime

class StarCatalog:
    def __init__(self, root):
        self.root = root
        self.root.title("Stellar Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        # =======================Variables=========================

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

        # =======================Title=========================

        lbltitle = Label(self.root, bd=6, relief=GROOVE, text="STELLAR MANAGEMENT SYSTEM", fg="white", bg="blue", font=("Algerian", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =======================Footer=========================

        lblfooter = Label(self.root, bd=3, relief=GROOVE, text="Developed by mateosolinho", fg="white", bg="blue", font=("Brush Script MT", 18))
        lblfooter.pack(side=BOTTOM, fill=X)

        # =======================DataframeLeft=========================

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

        # =======================ButtonDataframeLeft=========================

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

        # =======================DataframeRight=========================

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

        # =======================ButtonDataframeRight=========================
        
        Buttonframe2 = Frame(DataframeRight, bd=4, relief=RIDGE, bg='white')
        Buttonframe2.place(x=10, y=500, width=425)

        btnExport = Button(Buttonframe2, text="Export Data", width=10, command=self.export_data)
        btnExport.grid(row=0, column=0, padx=10, pady=10)
        btnPlot = Button(Buttonframe2, text="Plot", width=10, command=self.plot_distribution)
        btnPlot.grid(row=0, column=1, padx=10, pady=10)
        btnPrint = Button(Buttonframe2, text="Statistics", width=10,command=self.show_statistics)
        btnPrint.grid(row=0, column=2, padx=10, pady=10)
        btnReport = Button(Buttonframe2, text="Report", width=10, command=self.generate_report)
        btnReport.grid(row=0, column=3, padx=10, pady=10)

        # =================================Table=================================

        FrameTable = Frame(DataframeRight,bd=2,relief=RIDGE,bg='light blue')
        FrameTable.place(x=10,y=50,width=785,height=420)

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
        """
        Fetches all records from the 'stars' table in the database and populates the 
        Treeview widget with the retrieved data.

        Establishes a connection to the MySQL database, executes a SQL query to retrieve
        all rows from the 'stars' table, and updates the Treeview widget with the fetched
        data. If data is retrieved, it replaces any existing data in the Treeview widget.

        Closes the database connection after the data has been fetched and updated.

        Note:
            Assumes that the 'stars' table has columns corresponding to the data displayed
            in the Treeview widget.
        """
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
        """
        Deletes a record from the 'stars' table based on the selected ID.

        Checks if the 'Name' field is not empty before proceeding with the deletion. 
        Establishes a connection to the MySQL database, executes a SQL query to delete
        the record with the specified ID from the 'stars' table, and commits the transaction.

        If the deletion is successful and a record is deleted, updates the Treeview widget
        by fetching the updated data, clears the input fields, and displays a success message.
        If no record is found with the provided ID, displays a warning message.

        If an error occurs during the deletion process, an error message is displayed.

        Note:
            The ID of the record to be deleted is assumed to be stored in 'self.selected_id'.
            The 'Name' field must be non-empty to proceed with the deletion.
        """
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
        """
        Retrieves the data from the currently selected row in the Treeview widget
        and populates the form fields with the corresponding values.

        This method is typically bound to a Treeview widget event (e.g., clicking on a row).
        It retrieves the ID and other values from the selected row, then sets these values
        into the respective fields for editing or viewing. The ID is also stored in 'self.selected_id'
        for further use (e.g., deletion or update operations).

        Args:
            event: The event object associated with the Treeview widget interaction. 
                This is required for event handling but is not directly used in this function.

        Note:
            It is assumed that the Treeview widget 'self.stars_table' contains columns in the 
            following order: ID, Name, Catalog, Constellation, Spectral, Distance, Radius, Mass, Visibility.
        """
        cursor_row = self.stars_table.focus()
        content = self.stars_table.item(cursor_row)
        row = content['values']
        self.selected_id = row[0]
        self.name.set(row[1])
        self.catalog.set(row[2])
        self.constellation.set(row[3])
        self.spectral.set(row[4])
        self.distance.set(row[5])
        self.radius.set(row[6])
        self.mass.set(row[7])
        self.visibility.set(row[8])

    def add_stars(self):
        """
        Adds a new star record to the database with the details provided in the form fields.

        This method performs the following steps:
        1. Validates that all required fields are filled.
        2. Connects to the MySQL database and ensures the 'Stars' table exists, creating it if necessary.
        3. Inserts a new record into the 'Stars' table with the values from the form fields.
        4. Commits the transaction and updates the Treeview widget with the new data.
        5. Clears the form fields for the next entry.
        6. Closes the database connection.

        If any required field is empty, an error message is shown. On successful insertion, a success message is displayed.

        Note:
            The 'Stars' table is created with a predefined schema if it does not already exist. This schema includes fields for 
            ID, name, catalog, constellation, spectral type, distance, radius, mass, and visibility.
        """
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
        """
        Clears all the form fields and resets the selected record ID.

        This method performs the following actions:
        1. Resets the values of the form fields (name, catalog, constellation, spectral, distance, radius, mass, visibility) to empty strings.
        2. Sets the `selected_id` attribute to `None` to indicate that no record is currently selected.

        The purpose of this method is to prepare the form for a new entry or to clear any existing data from the fields after an operation.
        """
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
        """
        Updates an existing record in the database with new values from the form fields.

        This method performs the following actions:
        1. Checks if a record ID (`selected_id`) has been selected for updating. If no record is selected, it shows an error message and exits.
        2. Establishes a connection to the MySQL database and creates a cursor object for executing SQL queries.
        3. Executes an SQL `UPDATE` statement to modify the existing record in the `stars` table based on the provided ID.
        4. If the update is successful (i.e., at least one row is affected), it refreshes the displayed data and clears the form fields.
        5. Displays a success message if the record was updated, or a warning if no record was found with the provided ID.
        6. Handles any database errors by showing an error message.
        7. Ensures the database connection is closed after the operation.

        The purpose of this method is to allow modification of an existing record in the database based on user input from the form fields.
        """
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
        """
        Searches for records in the `stars` table based on user input and displays the results in a table.

        This method performs the following actions:
        1. Establishes a connection to the MySQL database and creates a cursor object for executing SQL queries.
        2. Constructs and executes a SQL `SELECT` statement to search for records in the `stars` table where the specified column matches the search criteria.
        3. The search criteria are determined by the user's input from `self.search_by` (the column to search) and `self.search_txt` (the search term).
        4. If matching records are found, it clears the existing records from the table and inserts the search results into the table.
        5. Displays an informational message if no records are found that match the search criteria.
        6. Closes the database connection after the search operation is complete.

        This method allows users to search for specific records in the database by filtering results based on the selected column and search term.
        """
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
        """
        Validates whether the provided input value is a valid float or an empty string.

        This method performs the following checks:
        1. If the input `value` is an empty string, it is considered valid and the method returns `True`.
        2. Otherwise, it checks if the `value` can be interpreted as a valid floating-point number by allowing a single period (.) in the string.
        3. Returns `True` if the `value` is a valid float or an empty string; otherwise, it returns `False`.

        This method helps in validating user input to ensure that it conforms to the expected format for floating-point numbers, 
        such as when entering values for distance, radius, mass, or visibility in the application.

        Args:
            value (str): The input value to be validated.

        Returns:
            bool: `True` if the input value is a valid float or empty string, otherwise `False`.
        """
        if value == "" or value.replace('.', '', 1).isdigit():
            return True
        return False
    
    def plot_distribution(self):
        """
        Fetches data from the database and plots a scatter plot showing the distribution of a specified parameter.

        This method performs the following actions:
        1. Connects to a MySQL database and retrieves the specified parameter data (e.g., Mass, Radius, Distance, Visibility) from the `stars` table.
        2. Checks if the parameter is valid and if there is data to plot.
        3. Creates a scatter plot of the data using Matplotlib and displays it in a new window.
        4. Provides a "Close" button to close the plot window.

        This method is intended to help visualize the distribution of a specific attribute of stars, using their IDs as the x-axis and the selected parameter as the y-axis.

        Returns:
            None: This method creates and displays a plot in a new window but does not return any value.
        """
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        
        parameter = self.search_by.get()
        
        if parameter not in ('Mass', 'Radius', 'Distance', 'Visibility'):
            messagebox.showwarning("Parameter Error", "Invalid parameter selected.")
            return
        
        my_cursor.execute(f"SELECT id, {parameter} FROM stars")
        data = my_cursor.fetchall()
        conn.close()
        
        if not data:
            messagebox.showinfo("Info", "No data to plot.")
            return
        
        ids, values = zip(*data)
        
        plot_window = Toplevel(self.root)
        plot_window.title(f'{parameter} Distribution')
        plot_window.geometry("800x600")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(ids, values, alpha=0.7, edgecolors='w')
        ax.set_title(f'Distribution of {parameter} Values')
        ax.set_xlabel('Star ID')
        ax.set_ylabel(parameter)
        ax.grid(True)
        
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=1)
        
        close_btn = Button(plot_window, text="Close", command=plot_window.destroy)
        close_btn.pack(pady=10)

    def export_data(self):
        """
        Exports data from the 'stars' table in the database to a CSV file.

        This method performs the following actions:
        1. Connects to a MySQL database and retrieves all records from the `stars` table.
        2. Retrieves column names from the database cursor's description attribute.
        3. Opens a file dialog for the user to choose a location and filename to save the CSV file.
        4. Writes the data to the specified CSV file, including column headers.
        5. Handles exceptions related to file I/O and database operations.

        If the data export is successful, a success message is displayed; otherwise, an error message is shown.

        Returns:
            None: This method does not return any value but provides user feedback through message boxes.
        """
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()

        try:
            my_cursor.execute("SELECT * FROM stars")
            data = my_cursor.fetchall()
            
            column_names = [desc[0] for desc in my_cursor.description]
            
            filetypes = (
                ('CSV files', '*.csv'),
                ('All files', '*.*')
            )
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=filetypes,
                title="Save data as"
            )

            if filename:
                try:
                    with open(filename, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(column_names)
                        writer.writerows(data)
                    messagebox.showinfo("Success", f"Data saved as {filename}")
                except IOError as e:
                    messagebox.showerror("Error", f"Error saving file: {e}")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error fetching data: {err}")
        finally:
            conn.close()

    def show_statistics(self):
        """
        Retrieves and displays statistical information for a selected parameter from the 'stars' table.

        This method performs the following actions:
        1. Connects to a MySQL database and retrieves data for the selected parameter.
        2. Checks if the selected parameter is valid. If not, displays an error message.
        3. Calculates statistical measures (mean, median, standard deviation) for the selected parameter.
        4. Displays the calculated statistics in a message box if data is available.
        5. Handles exceptions related to data retrieval and provides appropriate error messages.

        Returns:
            None: This method does not return any value but provides user feedback through message boxes.
        """
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        
        parameter = self.search_by.get()
        
        if parameter not in ('Mass', 'Radius', 'Distance', 'Visibility'):
            messagebox.showwarning("Parameter Error", "Invalid parameter selected.")
            return

        try:
            my_cursor.execute("SELECT " + parameter + " FROM stars")
            data = [row[0] for row in my_cursor.fetchall()]
            
            if data:
                mean = np.mean(data)
                median = np.median(data)
                std_dev = np.std(data)
                
                stats_msg = (
                    f"Statistics for {parameter}:\n"
                    f"Mean: {mean:.2f}\n"
                    f"Median: {median:.2f}\n"
                    f"Standard Deviation: {std_dev:.2f}"
                )
                messagebox.showinfo("Statistics", stats_msg)
            else:
                messagebox.showinfo("Info", "No data available for statistics.")
        except Exception as e:
            messagebox.showerror("Error", f"Error retrieving statistics: {e}")
        finally:
            conn.close()
        
    def generate_report(self):
        """
        Generates a PDF report containing data and statistics from the 'stars' table in the database.

        This method performs the following actions:
        1. Connects to the MySQL database and retrieves all data from the 'stars' table.
        2. Calculates statistical information (count, average, minimum, maximum) for the parameters 'Mass', 'Radius', 'Distance', and 'Visibility'.
        3. Calls the `create_pdf` method to generate and save a PDF report containing both the data and the calculated statistics.

        Returns:
            None: This method does not return any value but generates a PDF report file.
        """
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        
        my_cursor.execute("SELECT * FROM stars")
        self.data = my_cursor.fetchall()

        stats = {}
        for param in ('Mass', 'Radius', 'Distance', 'Visibility'):
            my_cursor.execute(f"SELECT {param} FROM stars")
            values = [row[0] for row in my_cursor.fetchall() if row[0] is not None]
            stats[param] = {
                'count': len(values),
                'average': sum(values) / len(values) if values else 0,
                'min': min(values) if values else 0,
                'max': max(values) if values else 0
            }

        conn.close()
        self.create_pdf(self.data, stats)

    def create_pdf(self, data, stats):
        """
        Creates and saves a PDF report with the provided data and statistics.

        This method performs the following actions:
        1. Opens a file dialog to select the location and name of the PDF file to save.
        2. Generates a PDF containing:
        - General information including the date and time of report generation.
        - A table of star data (excluding the ID column).
        - Statistical information (count, average, min, max) for each parameter.
        3. Saves the PDF to the specified file path.

        Args:
            data (list of tuples): List of tuples containing star data from the database.
            stats (dict): Dictionary containing statistical information for 'Mass', 'Radius', 'Distance', and 'Visibility'.

        Returns:
            None: This method does not return any value but saves a PDF file.
        """
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=filetypes,
            title="Save PDF as",
            initialfile="star_catalog_report.pdf"
        )
        
        if filename:
            try:
                pdf = FPDF()
                pdf.add_page()
                
                # Información general
                pdf.set_font("Arial", size=10)
                pdf.cell(0, 10, f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
                pdf.ln(10)
                
                # Agregar tabla de datos
                pdf.set_font("Arial", 'B', 10)
                column_widths = [25, 40, 25, 25, 20, 25, 15, 20]  # Ancho de las columnas
                
                headers = ['Name', 'Catalog', 'Constellation', 'Spectral', 'Distance', 'Radius', 'Mass', 'Visibility']
                pdf.set_font("Arial", 'B', 10)
                for i, header in enumerate(headers):
                    pdf.cell(column_widths[i], 10, header, border=1, align='C')
                pdf.ln()

                pdf.set_font("Arial", size=9)
                for row in data:
                    for i, item in enumerate(row[1:]):  # Omitir la primera columna (ID)
                        pdf.cell(column_widths[i], 10, str(item), border=1)
                    pdf.ln()
                
                pdf.ln(10)
                pdf.set_font("Arial", 'B', 10)
                pdf.cell(0, 10, 'Statistics', ln=True)
                pdf.set_font("Arial", size=9)
                
                for param, stat in stats.items():
                    pdf.cell(0, 10, f"{param} - Count: {stat['count']}, Average: {stat['average']:.2f}, Min: {stat['min']}, Max: {stat['max']}", ln=True)
                
                pdf.output(filename)
                messagebox.showinfo("Success", f"Report saved as {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error saving PDF: {e}")

    def export_pdf(self):
        """
        Exports the star data to a PDF file.

        This method performs the following actions:
        1. Opens a file dialog to select the location and name of the PDF file to save.
        2. Creates a PDF containing:
        - Title of the report.
        - Date and time of report generation.
        - General data including total number of records.
        - All records from the star data.
        3. Saves the PDF to the specified file path.

        Returns:
            None: This method does not return any value but saves a PDF file.
        """
        if not self.data:
            messagebox.showwarning("Error", "No data available to export.")
            return
        
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=filetypes,
            title="Save PDF as",
            initialfile="star_data_report.pdf"
        )
        
        if filename:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                pdf.cell(200, 10, txt="Star Catalog Data Report", ln=True, align='C')

                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                pdf.cell(200, 10, txt=f"Date and Time: {date_time}", ln=True)

                pdf.cell(200, 10, txt="General Data:", ln=True)
                pdf.cell(200, 10, txt=f"Total Records: {len(self.data)}", ln=True)

                pdf.cell(200, 10, txt="Data:", ln=True)
                for row in self.data:
                    pdf.cell(200, 10, txt=str(row), ln=True)

                pdf.output(filename)
                messagebox.showinfo("Success", f"Data saved as {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error saving PDF: {e}")
root = Tk()
object = StarCatalog(root)
root.mainloop()
