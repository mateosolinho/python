from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class StarCatalog:
    def __init__(self, root):
        self.root = root
        self.root.title("Star Catalog")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        # Definir las variables de instancia
        self.sl_var = StringVar()
        self.name_var = StringVar()
        self.class_var = StringVar()
        self.batch_var = StringVar()
        self.adate_var = StringVar()
        self.mob_var = StringVar()
        self.pmob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Título
        lbltitle = Label(self.root, bd=6, relief=GROOVE, text="STAR MANAGEMENT SYSTEM", fg="white", bg="blue", font=("Algerian", 30, "bold"))
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
        txtName = Entry(DataframeLeft, textvariable=self.name_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtName.grid(row=1, column=1, pady=10, padx=5, sticky='w')

        lblCatalog = Label(DataframeLeft, text="Catalog", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblCatalog.grid(row=2, column=0, pady=10, padx=40, sticky='w')
        txtCatalog = Entry(DataframeLeft, textvariable=self.class_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtCatalog.grid(row=2, column=1, pady=10, padx=5, sticky='w')

        lblConst = Label(DataframeLeft, text="Constelation", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblConst.grid(row=3, column=0, pady=10, padx=40, sticky='w')
        txtConst = Entry(DataframeLeft, textvariable=self.batch_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtConst.grid(row=3, column=1, pady=10, padx=5, sticky='w')

        lblEspectral = Label(DataframeLeft, text="Spectral Type", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblEspectral.grid(row=4, column=0, pady=10, padx=40, sticky='w')
        txtEspectral = Entry(DataframeLeft, textvariable=self.adate_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtEspectral.grid(row=4, column=1, pady=10, padx=5, sticky='w')

        lblDistance = Label(DataframeLeft, text="Distance", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblDistance.grid(row=5, column=0, pady=10, padx=40, sticky='w')
        txtDistance = Entry(DataframeLeft, textvariable=self.mob_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtDistance.grid(row=5, column=1, pady=10, padx=5, sticky='w')

        lblRadius = Label(DataframeLeft, text="Radius", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblRadius.grid(row=6, column=0, pady=10, padx=40, sticky='w')
        txtRadius = Entry(DataframeLeft, textvariable=self.pmob_var, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtRadius.grid(row=6, column=1, pady=10, padx=5, sticky='w')

        lblMass = Label(DataframeLeft, text="Mass", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblMass.grid(row=7, column=0, pady=10, padx=40, sticky='w')
        txtMass = Entry(DataframeLeft, textvariable=self.search_txt, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtMass.grid(row=7, column=1, pady=10, padx=5, sticky='w')

        lblVisibility = Label(DataframeLeft, text="Visibility", bg="light blue", fg="black", font=("times new roman", 18, 'bold'))
        lblVisibility.grid(row=8, column=0, pady=10, padx=40, sticky='w')
        txtVisibility = Entry(DataframeLeft, textvariable=self.search_txt, font=('times new roman', 14), bd=2, relief=GROOVE)
        txtVisibility.grid(row=8, column=1, pady=10, padx=5, sticky='w')

        # ButtonFrame
        Buttonframe = Frame(DataframeLeft, bd=4, relief=RIDGE, bg='white')
        Buttonframe.place(x=10, y=500, width=425)

        btnAdd = Button(Buttonframe, text="Add", width=10)
        btnAdd.grid(row=0, column=0, padx=10, pady=10)
        btnUpdate = Button(Buttonframe, text="Update", width=10)
        btnUpdate.grid(row=0, column=1, padx=10, pady=10)
        btnDelete = Button(Buttonframe, text="Delete", width=10)
        btnDelete.grid(row=0, column=2, padx=10, pady=10)
        btnClear = Button(Buttonframe, text="Clear", width=10)
        btnClear.grid(row=0, column=3, padx=10, pady=10)

        # DataframeRight
        DataframeRight = Label(self.root, bd=4, relief=RIDGE, bg='light blue')
        DataframeRight.place(x=500, y=70, width=825, height=580)

        lblSearch = Label(DataframeRight, text="Search By", bg="light blue", fg="black", font=("times new roman", 16, 'bold'))
        lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        comboSearch = ttk.Combobox(DataframeRight, width=10, textvariable=self.search_by, font=("times new roman", 12, 'bold'), state='readonly')
        comboSearch['values'] = ("Name", "Catalog", "Constelation", "Espectral Type", "Distance", "Radius", "Mass", "Visibility")
        comboSearch.current(0)
        comboSearch.grid(row=0, column=1, pady=10, padx=20)

        txtSearch = Entry(DataframeRight,width=30,textvariable=self.search_txt,font=('times new roman',14),bd=2,relief=GROOVE)
        txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(DataframeRight,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(DataframeRight,text="Show All",width=10).grid(row=0,column=4,padx=10,pady=10)

        # =================================Table=================================

        FrameTable = Frame(DataframeRight,bd=2,relief=RIDGE,bg='light blue')
        FrameTable.place(x=10,y=80,width=785,height=480)

        scroll_x = Scrollbar(FrameTable,orient="horizontal")
        scroll_y = Scrollbar(FrameTable,orient="vertical")
        self.stars_table = ttk.Treeview(FrameTable,columns=("name","catalog","constelation","spectral","distance","radius","mass","visibility"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.stars_table.xview)
        scroll_y.config(command=self.stars_table.yview)

        self.stars_table.heading("name",text="Name")
        self.stars_table.heading("catalog",text="Catalog")
        self.stars_table.heading("constelation",text="Constelation")
        self.stars_table.heading("spectral",text="Spectral Type")
        self.stars_table.heading("distance",text="Distance")
        self.stars_table.heading("radius",text="Radius")
        self.stars_table.heading("mass",text="Mass")
        self.stars_table.heading("visibility",text="Visibility")

        self.stars_table['show']='headings'

        self.stars_table.column("name",width=80)
        self.stars_table.column("catalog",width=80)
        self.stars_table.column("constelation",width=80)
        self.stars_table.column("spectral",width=80)
        self.stars_table.column("distance",width=80)
        self.stars_table.column("radius",width=80)
        self.stars_table.column("mass",width=80)
        self.stars_table.column("visibility",width=80)
        self.stars_table.pack(fill=BOTH,expand=1)
        # self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

# Crear la ventana principal y ejecutar la aplicación
root = Tk()
object = StarCatalog(root)
root.mainloop()
