from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk



class Attendance:
    data = None
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM employee")
        self.data = my_cursor.fetchall()
        conn.close()


  

    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x850+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")
        # Frame
        table_frame = Frame(self.root, bd=2)
        table_frame.place(x=5, y=130, width=1530, height=880)
        left_frame = LabelFrame(table_frame, bd=2, relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=5, width=1500, height=630)
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table = ttk.Treeview(table_frame, column=("Department", "Shift", "Position", "Year", "Employee_ID", "Employee_Name", "Gender", "Product Category", "Phone", "Email", "Address", "Verification_ID", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("Department", text="Department")
        self.employee_table.heading("Shift", text="Shift")
        self.employee_table.heading("Position", text="Position")
        self.employee_table.heading("Year", text="Year")
        self.employee_table.heading("Employee_ID", text="Employee_ID") 

        self.employee_table.heading("Employee_Name", text="Employee_Name")
        self.employee_table.heading("Gender", text="Gender")
        self.employee_table.heading("Product Category", text="ProductCategory")
        self.employee_table.heading("Phone", text="Phone")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Address", text="Address")
        self.employee_table.heading("Verification_ID", text="Verification_ID")
        self.employee_table["show"] = "headings"

        #self.employee_table.pack(fill=BOTH,expand=1)

        self.employee_table.column("Department", width=150)
        self.employee_table.column("Shift",width=100)
        self.employee_table.column("Position",width=150)
        self.employee_table.column("Year",width=120)
        self.employee_table.column("Employee_ID", width=120)
        self.employee_table.column("Employee_Name", width=150)
        self.employee_table.column("Gender",width=120)
        self.employee_table.column("Product Category",width=120)
        self.employee_table.column("Phone", width=150)
        self.employee_table.column("Email", width=150)
        self.employee_table.column("Address", width=150)
        self.employee_table.column("Verification_ID", width=150)

        self.employee_table.pack(fill=BOTH,expand=1)
        #self.employee_table.bind("<ButtonRelease",self.get_cursor)
        # self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        


        self.fetch_data()
        for record in self.data:
          self.employee_table.insert("", "end", values=record)

        #First Image
        img = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img = img.resize((500, 110), Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.grid(row=0, column=0, padx=10, pady=10)
        
        #Second Image
        img1= Image.open(r"C:\Users\91639\OneDrive\Desktop\simple.png")
        img1 = img1.resize((500, 110), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Third Image 

        img2 = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img2 = img2.resize((500, 110), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.grid(row=0, column=2, padx=10, pady=10)


        self.root.configure(bg="thistle")






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root) 
    obj.fetch_data()
    root.mainloop()


