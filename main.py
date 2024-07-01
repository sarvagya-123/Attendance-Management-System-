from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x850+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")

        # Set background color
        self.root.configure(bg="lightblue")

        # First Image 
       
        img = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img = img.resize((400, 200), Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Second Image   
        
        img1= Image.open(r"C:\Users\91639\OneDrive\Pictures\ams.jpeg")
        img1 = img1.resize((500, 200), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.grid(row=0, column=1, padx=80, pady=10)

        # Third Image 

        img2 = Image.open(r"C:\Users\91639\OneDrive\Desktop\attendance system.png")
        img2 = img2.resize((400, 200), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.grid(row=0, column=3, padx=0, pady=30)

        #title_label = Label(self.root, text=" ATTENDANCE SYSTEM", font=("times new roman", 35, "italic"), bg="white", fg="red")
       # title_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Employee Management Button
        img3 = Image.open(r"C:\Users\91639\OneDrive\Desktop\one.jpeg")
        img3 = img3.resize((220,220), Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        

        b1 = Button(self.root,image=self.photoimg3,command=self.employee_details,cursor="star")
        b1.place(x=90,y=350,width=270,height=180)

        b1_1 = Button(self.root,text=" Employee Details",command=self.employee_details,cursor="spider",font=("times new roman", 20, "italic"), bg="white", fg="red")
        b1_1.place(x=92,y=550 ,width=265,height=40)

       # Face Detection
        
        #img4 = Image.open(r"C:\Users\91639\OneDrive\Desktop\app.jpg")
        #img4 = img4.resize((220,220), Image.BICUBIC)
        #self.photoimg4 = ImageTk.PhotoImage(img4)
        #b2 = Button(self.root,image=self.photoimg3,cursor="star")
        #b2.place(x=620,y=250,width=270,height=180)

        #b2_2 = Button(self.root,text="Face Detector",cursor="spider",font=("times new roman", 20, "italic"), bg="white", fg="red")
        #b2_2.place(x=620,y=435 ,width=265,height=40)
          
        #Attendance Button 
        img5 = Image.open(r"C:\Users\91639\OneDrive\Pictures\employee.jpeg")
        img5 = img5.resize((220,220), Image.BICUBIC)
        self.photoimg5= ImageTk.PhotoImage(img3)

        b1 = Button(self.root,image=self.photoimg5,command=self.attendance_detail,cursor="star")
        b1.place(x=600,y=350,width=270,height=180)

        b1_1 = Button(self.root,text=" Attendance",cursor="spider",command=self.attendance_detail,font=("times new roman", 20, "italic"), bg="white", fg="red")
        b1_1.place(x=600,y=550 ,width=265,height=40)
        
        #Train Button 
        #img6 = Image.open(r"C:\Users\91639\OneDrive\Desktop\download.jpg")
        #img6 = img6.resize((220,220), Image.BICUBIC)
        #self.photoimg6 = ImageTk.PhotoImage(img6)
        

        #b1 = Button(self.root,image=self.photoimg6,cursor="star")
       #b1.place(x=90,y=530,width=270,height=180)

        #b1_1 = Button(self.root,text="Train Data",cursor="spider",font=("times new roman", 20, "italic"), bg="white", fg="red")
        #b1_1.place(x=90,y=720 ,width=265,height=40)

        #Scan Face
        #img7 = Image.open(r"C:\Users\91639\OneDrive\Desktop\download.jpg")
        #img7 = img7.resize((220,220), Image.BICUBIC)
       # self.photoimg7 = ImageTk.PhotoImage(img7)
        

        #b1 = Button(self.root,image=self.photoimg7,cursor="star")
        #b1.place(x=620,y=530,width=270,height=180)

        #b1_1 = Button(self.root,text=" Scan ",cursor="spider",font=("times new roman", 20, "italic"), bg="white", fg="red")
        #b1_1.place(x=620,y=720 ,width=265,height=40)

        #Exit 
        img8= Image.open(r"C:\Users\91639\OneDrive\Desktop\download.jpg")
        img8 = img8.resize((220,220), Image.BICUBIC)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        

        b1 = Button(self.root,image=self.photoimg8,cursor="star",command=self.exit_app)
        b1.place(x=1200,y=350,width=270,height=180)

        b1_1 = Button(self.root,text=" Exit",cursor="spider",font=("times new roman", 20, "italic"), bg="white", fg="red",command=self.exit_app)
        b1_1.place(x=1200,y=550 ,width=265,height=40)

    #Function button 
    def employee_details(self):
        self.new_window =Toplevel(self.root)
        self.app =Employee(self.new_window)  
    
    def exit_app(self):
        self.root.destroy()

    def attendance_detail(self):
        self.new_window =Toplevel(self.root)
        self.app =Attendance(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

