from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        self.root.resizable(False, False)

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =================================Dataframe=================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1540, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # =================================Buttonsframe=================================
        
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1540, height=70)
        
        # =================================Detailsframe=================================
        
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1540, height=190)

        # ================================================================================
        # =================================Dataframe Left=================================

        lblNameTablet = Label(DataframeLeft, text="Name Of Tablet: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("arial", 12, "bold"), width=33)
        comNameTablet["values"] = ("Nolotil", "Paracetamol", "Ibuprofeno", "Ventolin", "Lexatin", "Orfidal")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, text="Reference No: ", font=("arial", 12, "bold"), padx=2, pady=4)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose: ", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, text="No Of Tablets: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, text="Lot: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, text="Issue Date: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.IssueDate, width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, text="Exp Date: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)
        
        lblDailyDose = Label(DataframeLeft, text="Daily Dose: ", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, text="Side Effect: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.SideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataframeLeft, text="Further Information: ", font=("arial", 12, "bold"), padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.FurtherInformation, width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataframeLeft, text="Blood Presure: ", font=("arial", 12, "bold"), padx=2)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, text="Storage Advice: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, text="Medication: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientID = Label(DataframeLeft, text="Patient ID: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientID, width=35)
        txtPatientID.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, text="NHS Number: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.NHSNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, text="Patient Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, text="Date Of Birth: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, text="Patient Address: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # =================================Dataframe Right=================================
        self.textPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0)

        # =====================================Buttons====================================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.update)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # =====================================Table========================================
        # =====================================ScrollBar====================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftable", "ref", "dose", "nooftables", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftables", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftables", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.NHSNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Name_of_tablets=%s,dose=%s,NumberofTablets=%s,lot=%s,issueDate=%s,expDate=%s,dailyDose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientAddress=%s where Reference_No=%s",(
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.NHSNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get(),
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

root = Tk()
object = Hospital(root)
root.mainloop()
