from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Toplevel
import mysql.connector


class Employee :
 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x850+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")

        #Variable
        self.var_department= StringVar()
        self.var_position=StringVar()
        self.var_year=StringVar()
        self.var_shift=StringVar()
        self.var_employee_id =StringVar()
        self.var_employee_name=StringVar()
        self.var_gender =StringVar()
        self.var_product_category=StringVar()
        self.var_phone =StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_verification_id =StringVar()
        self.var_radiobtn1=StringVar()
        #self.var__take_photo_btn =StringVar()
       

         # Set background color
        self.root.configure(bg="thistle")

        # First Image 
       
        img = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img = img.resize((500, 110), Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Second Image   
        
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

         # Set background color
        self.root.configure(bg="thistle")

        

     # Frame 
        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=5,y=130,width=1530,height=880)

    # Left Frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text = "Employee Details",font=("times new roman",12,"bold" ))
        left_frame.place(x=5,y=5,width = 730,height=630)

    # left Image
        img_left  = Image.open(r"C:\Users\91639\OneDrive\Desktop\scan.jpg")
        img_left = img_left.resize((550, 130), Image.BICUBIC)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=70,y=175,width=600,height=110) 

    #work Information 
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text = "Work Details",font=("times new roman",12,"bold" ))
        current_course_frame.place(x=5,y=135,width = 680,height=110) 


    #Department 
        dep_label = Label(current_course_frame, text ="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column =0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        dep_combo["values"] =("Select Department","Finance and Accounting","Operations","Sales and Marketing","Customer Service","Research and Development","Administration","Project Management","Business Development")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx =2,pady=10,sticky=W)

    #Position 
        pos_label = Label(current_course_frame, text ="Position",font=("times new roman",12,"bold"))
        pos_label.grid(row=0,column =2,padx=10)

        pos_combo = ttk.Combobox(current_course_frame,textvariable=self.var_position,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        pos_combo["values"] =("Select Position","Chief Executive Officer","Chief Technology Office","Operations Manager","Sales Manager","Software Engineer/Developer","Administrative Assistant","Graphic Designer","Financial Analyst")
        pos_combo.current(0)
        pos_combo.grid(row=0,column=3,padx =2,pady=10,sticky=W)
        
    #Year 
        ye_label = Label(current_course_frame, text ="Year",font=("times new roman",12,"bold"))
        ye_label.grid(row=1,column =0,padx=10)

        ye_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        ye_combo["values"] =("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        ye_combo.current(0)
        ye_combo.grid(row=1,column=1,padx =2,pady=10,sticky=W)

    #Shift
        shi_label = Label(current_course_frame, text ="Shift",font=("times new roman",12,"bold"))
        shi_label.grid(row=1,column =2,padx=10)

        shi_combo = ttk.Combobox(current_course_frame,textvariable=self.var_shift,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        shi_combo["values"] =("Select Shift","Day","Night")
        shi_combo.current(0)
        shi_combo.grid(row=1,column=3,padx =2,pady=10,sticky=W)   

    #Employee Information 
        Employee_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text = "Employee Details",font=("times new roman",12,"bold" ))
        Employee_course_frame.place(x=5,y=250,width = 680,height=200)

    #Employee_ID
        Employee_ID_label = Label(Employee_course_frame, text ="Employee ID :",font=("times new roman",12,"bold"))
        Employee_ID_label.grid(row=0,column =0,padx=10,sticky=W)

        Employee_ID_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_employee_id,width=20,font=("times new roman",12,"bold")) 
        Employee_ID_entry.grid(row = 0,column=2,padx=5,pady=5,sticky=W)
    #Employee Name
        Employee_Name_label = Label(Employee_course_frame, text ="Employee Name :",font=("times new roman",12,"bold"))
        Employee_Name_label.grid(row=0,column =3,pady=5,padx=10,sticky=W)

        Employee_Name_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_employee_name,width=20,font=("times new roman",12,"bold")) 
        Employee_Name_entry.grid(row = 0,column=4,padx=10,pady=5,sticky=W) 
    #Gender
       

        Gender_label = Label(Employee_course_frame, text="Gender", font=("times new roman", 12, "bold"))
        Gender_label.grid(row=1, column=0, padx=1,pady=5,sticky=W)


        Gender_combo = ttk.Combobox(Employee_course_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        Gender_combo["values"] =("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=1,column=2,padx =2,pady=10,sticky=W)

    #Product Category
        Product_label = Label(Employee_course_frame, text ="Product Category :",font=("times new roman",12,"bold"))
        Product_label.grid(row=1,column =3,pady=5,padx=10,sticky=W)

        Product_entry  = ttk.Entry(Employee_course_frame,textvariable=self.var_product_category,width=20,font=("times new roman",12,"bold")) 
        Product_entry.grid(row = 1,column=4,padx=10,pady=5,sticky=W)
    #Phone
        Phone_label= Label(Employee_course_frame, text ="Phone Number :",font=("times new roman",12,"bold"))
        Phone_label.grid(row=2,column =0,pady=5,padx=10,sticky=W)

        Phone_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold")) 
        Phone_entry.grid(row = 2,column=2,padx=10,pady=5,sticky=W)
    #Email
        Email_label = Label(Employee_course_frame, text ="Email :",font=("times new roman",12,"bold"))
        Email_label.grid(row=2,column =3,pady=5,padx=10,sticky=W)

        Email_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold")) 
        Email_entry.grid(row = 2,column=4,padx=10,pady=5,sticky=W)
          
    #Address
        Address_label = Label(Employee_course_frame, text ="Address :",font=("times new roman",12,"bold"))
        Address_label.grid(row=3,column =0,pady=5,padx=10,sticky=W)

        Address_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold")) 
        Address_entry.grid(row = 3,column=2,padx=10,pady=5,sticky=W)

    #Verification_ID
        Verification_label = Label(Employee_course_frame, text ="Verification ID :",font=("times new roman",12,"bold"))
        Verification_label.grid(row=3,column =3,pady=5,padx=10,sticky=W)
        Verification_entry = ttk.Entry(Employee_course_frame,textvariable=self.var_verification_id,width=20,font=("times new roman",12,"bold")) 
        Verification_entry.grid(row = 3,column=4,padx=10,pady=5,sticky=W)
    
     # Radio_Button 
       
        #radiobtn1 = ttk.Radiobutton(Employee_course_frame , text="Take a Photo Sample", value="YES")
        #radiobtn1.place(x=20,y=145)

        #radiobtn2 =ttk.Radiobutton(Employee_course_frame,text="NO photo sample",value="NO")
        #radiobtn2.place(x=220,y=145)


# Button_Frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white") 
        btn_frame.place(x=1, y=500, width=725, height=38)

        save_button = Button(btn_frame, text="Save",command=self.add_data,width=17, font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        save_button.grid(row=1, column=0)


        update_btn =Button(btn_frame,text="Update", command=self.update_data,width=17,font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        update_btn.grid(row=1, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        delete_btn.grid(row=1, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17,command=self.reset_data, font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        reset_btn.grid(row=1, column=3)

       # btn_frame1 = Frame(left_frame, bd=2, relief=RIDGE, bg="white") 
        #btn_frame1.place(x=0, y=537, width=725, height=38)
        
        #take_photo_btn= Button(btn_frame1, text="Take Photo Sample",width=37, font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        #take_photo_btn.grid(row=2,column=0)

        #update_photo_btn= Button(btn_frame1, text="Update Photo Sample", width=37, font=("times new roman", 13, "bold"), bg="light coral", fg="white")
       #update_photo_btn.grid(row=2, column=1)



    # Right Frame 
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text = "Employee Details",font=("times new roman",12,"bold" ))
        Right_frame.place(x=775,y=10,width=760,height=630)

    #Right Image
        img_right  = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img_right = img_right.resize((500, 130), Image.BICUBIC)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=840,y=178,width=600,height=130) 

        #Search System
        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text = "Search System",font=("times new roman",12,"bold" ))
        Search_frame.place(x=5,y=140,width = 730,height=70)

        search_label= Label(Search_frame, text =" Search By:",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column =0,pady=5,padx=10,sticky=W)

        

        search_combo = ttk.Combobox(Search_frame,font=("times new roman",12,"bold"), state = "readonly",width = 17)
        search_combo["values"] =("Select","Employee ID","Employee Name","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx =2,pady=10,sticky=W)

        
        search_entry = ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold")) 
        search_entry.grid(row =0,column=2,padx=10,pady=5,sticky=W)


        search_btn = Button(Search_frame, text="Search", width=12  , font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        search_btn.grid(row=0, column=3,padx=2)

        showAll_btn = Button(Search_frame, text="Show All", width=12,  font=("times new roman", 13, "bold"), bg="light coral", fg="white")
        showAll_btn.grid(row=0, column=4,padx=2)

        #Table Frame
        table_frame = Frame(Right_frame,bd=2,bg="White",relief=RIDGE)
        table_frame.place(x=5,y=220,width = 600,height=350)
   
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
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()
#Function Decration
    def add_data(self):
     if self.var_department.get() == "Select Department" or self.var_employee_id.get() == "" or self.var_employee_name.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                              (self.var_department.get(),
                               self.var_shift.get(),
                               self.var_position.get(),
                               self.var_year.get(),
                               self.var_employee_id.get(),
                               self.var_employee_name.get(),
                               self.var_gender.get(),
                               self.var_product_category.get(),
                               self.var_phone.get(),
                               self.var_email.get(),
                               self.var_address.get(),
                               self.var_verification_id.get()
                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data has been added successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM employee")
        data = my_cursor.fetchall()



    # Clear existing data in the Treeview
        self.employee_table.delete(*self.employee_table.get_children())

    # Insert retrieved data into the Treeview
        for record in data:
          self.employee_table.insert("", "end", values=record)
        conn.close()



#Get cursor 
    def get_cursor(self, event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0])
        self.var_position.set(data[1])
        self.var_year.set(data[2])
        self.var_shift.set(data[3])
        self.var_employee_id.set(data[4])
        self.var_employee_name.set(data[5])
        self.var_gender.set(data[6])
        self.var_product_category.set(data[7])
        self.var_phone.set(data[8])
        self.var_email.set(data[9])
        self.var_address.set(data[10])
        self.var_verification_id.set(data[11])
        self.var_radiobtn1.set(data[12])



# update photo function
    def update_data(self):
    # Check if all required fields are filled
     if (self.var_department.get() == "Select Department" or 
        self.var_employee_name.get() == "" or 
        self.var_employee_id.get() == ""):
        
        messagebox.showerror("Error", "All fields are required", parent=self.root)
        return
    
    # Confirm update operation
     confirmed = messagebox.askyesno("Update", "Do you want to update the employee details?", parent=self.root)
     if not confirmed:
       return
    
    # Attempt to update the data
     try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="8005",
            database="copppppp"
        )
        cursor = conn.cursor()

        # Prepare the SQL query
        query = """UPDATE employee 
                   SET department=%s, position=%s, year=%s, shift=%s, 
                       employee_name=%s, gender=%s, product_category=%s, 
                       phone=%s, email=%s, address=%s, verification_id=%s 
                   WHERE employee_id=%s"""

        # Execute the query
        cursor.execute(query, (
            self.var_department.get(),
            self.var_position.get(),
            self.var_year.get(),
            self.var_shift.get(),
            self.var_employee_name.get(),
            self.var_gender.get(),
            self.var_product_category.get(),
            self.var_phone.get(),
            self.var_email.get(),
            self.var_address.get(),
            self.var_verification_id.get(),
            self.var_employee_id.get()
        ))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Employee detail successfully updated")
        
        # Refresh the data
        self.fetch_data()

     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}", parent=self.root)

     

    

   


    
#Delete function 
    def delete_data(self):
     selected_item = self.employee_table.focus()
     if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete.", parent=self.root)
     else:
            confirmed = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?", parent=self.root)
            if confirmed:
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
                    my_cursor = conn.cursor()

                    # Iterate through all columns to find the employee_id
                    item_id = None
                    for value in self.employee_table.item(selected_item)["values"]:
                        try:
                            item_id = int(value)
                            break  # Once employee_id is found, exit loop
                        except ValueError:
                            pass  # Continue to next value if not an integer

                    if item_id is None:
                        raise ValueError("Employee ID not found or invalid format")

                    # Execute the SQL query to delete the record with the identified ID
                    my_cursor.execute("DELETE FROM employee WHERE employee_id = %s", (item_id,))

                    conn.commit()

                    # Remove the deleted item from the table
                    self.employee_table.delete(selected_item)

                    messagebox.showinfo("Success", "Record deleted successfully.", parent=self.root)

                    conn.close()

                except Exception as e:
                    messagebox.showerror("Error", f"Error occurred: {str(e)}", parent=self.root)




        

#Reset Function
    def reset_data(self):
        self.var_department.set("Select Department"),
        self.var_position.set("Select Position"),
        self.var_year.set("Select Year"),
        self.var_shift.set("Select Shift"),
        self.var_employee_name.set(""), 
        self.var_gender.set(""),
        self.var_product_category.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_verification_id.set(""),
        self.var_radiobtn1.set(""),
        self.var_employee_id.set("") 
      
              


 

# Take Photo Sample
    '''def generate_dataset(self):
        if self.var_department.get() == "Select Department" or self.var_employee_name.get() == "" or self.var_employee_id.get() == "":
          messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
         try:
               conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
               my_cursor = conn.cursor()
               my_cursor.execute("SELECT * FROM student")
               myresult = my_cursor.fetchall()
               id = 0

               for x in myresult:
                id += 1

                my_cursor.execute("UPDATE employee SET department=%s, position=%s, year=%s, shift=%s, employee_name=%s, gender=%s, product_category=%s, phone=%s, email=%s, address=%s, verification_id=%s WHERE employee_id=%s", (
                        self.var_department.get(),
                        self.var_position.get(),
                        self.var_year.get(),
                        self.var_shift.get(),
                        self.var_employee_name.get(),
                        self.var_gender.get(),
                        self.var_product_category.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_verification_id.get(),
                        self.var_employee_id.get()==id+1
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

         except mysql.connector.Error as e:
            print("Error: ", e)
            messagebox.showerror("Database Error", f"An error occurred while updating the database: {e}", parent=self.root)
    def generate_dataset(self):
        if self.var_department.get() == "Select Department" or self.var_employee_name.get() == "" or self.var_employee_id.get() == "":
          messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
         try:
            conn = mysql.connector.connect(host="localhost", user="root", password="8005", database="copppppp")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE employee SET department=%s, position=%s, year=%s, shift=%s, employee_name=%s, gender=%s, product_category=%s, phone=%s, email=%s, address=%s, verification_id=%s WHERE employee_id=%s", (
                self.var_department.get(),
                self.var_position.get(),
                self.var_year.get(),
                self.var_shift.get(),
                self.var_employee_name.get(),
                self.var_gender.get(),
                self.var_product_category.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_verification_id.get(),
                self.var_employee_id.get()
            ))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Uncomment the detect_and_crop_face function call
            # self.detect_and_crop_face()
         except mysql.connector.Error as e:
            print("Error: ", e)
            messagebox.showerror("Database Error", f"An error occurred while updating the database: {e}", parent=self.root)

    
                

        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


#Function to detect and crop face
        def detect_and_crop_face(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            cropped_faces = []

            for(x,y,w,h)in faces:
              face_cropped=img[y:y+h,x:x+w]
              cropped_faces.append(face_cropped)
            return cropped_faces
        try:
            cap = cv2.VideoCapture(0)
            img_id=0

            while True:
                ret,my_frame =cap.read()
                faces =detect_and_crop_face(my_frame)


                #if len(faces)>0:
                img_id+=1
                for idx, face in enumerate(faces):
                   for idx, face in enumerate(faces):
                    try:
                      face_resized = cv2.resize(face, (450, 450))
                      face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                      file_name_path = f"data/user.{img_id}.{idx}.jpg"
                      cv2.imwrite(file_name_path, face_gray)
                      cv2.putText(face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                      cv2.imshow(f"Cropped Face {idx}", face_resized)
                    except Exception as e:
                       print("Error saving image:", e)  
             
                if cv2.waitKey(1)==1 or img_id==100:
                   break 
               
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data sets completed")
        except Exception as es:
          messagebox.showerror("Error", f"Due To: {str(es)}")'''     
       
       

             
       
          


if __name__ == "__main__":
   root = Tk() 
   obj = Employee(root)
   obj.fetch_data()  # Fetch data before entering the mainloop
   root.mainloop()


if __name__ == "__main__":
    root = Tk() 
    obj = Employee(root)
    root.mainloop() 
    
