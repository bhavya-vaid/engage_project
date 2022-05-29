from ast import Import
import os
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train 
from face_recognition import Face_recognition
import os
from train import Train
from attendance import Attendance


class Face_recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recog sys")

        #firstimg
        img=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img)     

        f_lb=Label(self.root,image=self.photo1)
        f_lb.place(x=0,y=0,width=500,height=130)

        
        #secimg
        img1=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\xyz.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img1)     

        f_lb=Label(self.root,image=self.photo2)
        f_lb.place(x=500,y=0,width=500,height=130)

         #thrdimg
        img2=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img2)     

        f_lb=Label(self.root,image=self.photo3)
        f_lb.place(x=1000,y=0,width=500,height=130)

         #bgimg
        img3=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img3)     

        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",33,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        #studentbutton
        img4=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img4)   

        b1=Button(bg_img,image=self.photo4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=180,height=180) 

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        b1.place(x=100,y=280,width=180,height=40) 
        
         #facedetectstudentbutton
        img5=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img5=img5.resize((1530,710),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img5)   

        b1=Button(bg_img,image=self.photo4,cursor="hand2",command=self.Face_data)
        b1.place(x=300,y=100,width=180,height=180) 

        b1=Button(bg_img,text="Face detector",cursor="hand2",command=self.Face_data,font=("times new roman",15,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        b1.place(x=300,y=280,width=180,height=40) 

         #Attendance
        img6=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img6=img6.resize((1530,710),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img6)   

        b1=Button(bg_img,image=self.photo4,cursor="hand2",command=self.attendance_data)
        b1.place(x=500,y=100,width=180,height=180) 

        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        b1.place(x=500,y=280,width=180,height=40) 

        #Train Face
        img7=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img7=img7.resize((1530,710),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img7)   

        b1=Button(bg_img,image=self.photo4,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=400,width=180,height=180) 

        b1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        b1.place(x=100,y=580,width=180,height=40) 

        #Photos
        img8=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face6.jpg")
        img8=img8.resize((1530,710),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img8)   

        b1=Button(bg_img,image=self.photo4,cursor="hand2",command=self.open_img)
        b1.place(x=300,y=400,width=180,height=180) 

        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        b1.place(x=300,y=580,width=180,height=40) 

        
        
    def open_img(self):
      os.startfile("data")

        
        #***************funtion buttons***************
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)

    
    def Face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_recognition(self.new_window)

    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)

 
         
         
    

         

         
         
if __name__ =="__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()
