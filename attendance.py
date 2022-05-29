from platform import release
from pyexpat import features
from this import d
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX, CascadeClassifier, VideoCapture, destroyAllWindows, putText, waitKey
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recog sys")

        #****************variables***************
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        #firstimg
        img=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img)     

        f_lb=Label(self.root,image=self.photo1)
        f_lb.place(x=0,y=0,width=800,height=200)

        
        #secimg
        img1=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img1)     

        f_lb=Label(self.root,image=self.photo2)
        f_lb.place(x=800,y=0,width=800,height=200)

        #bgimg
        img3=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\four.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img3)     

        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE DETAILS", font=("times new roman",33,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #leftlabelframe
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        
        img_left=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photo_left=ImageTk.PhotoImage(img_left)     

        f_lb=Label(Left_frame,image=self.photo_left)
        f_lb.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #*******Labels and entry***************
        #attendance Id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label=Label(left_inside_frame,text="Roll:",font="comicsab=nsbs 11 bold")
        roll_label.grid(row=0,column=2)

        roll_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsab=nsbs 11 bold")
        roll_entry.grid(row=0,column=3,pady=8)

        #Name
        name_label=Label(left_inside_frame,text="Name::",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8)

        #Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        #Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=4)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,pady=8)

        #Attendancce
        attendancelabel=Label(left_inside_frame,text="Attendance Status:",font="comicsansns 11 bold",bg="white")
        attendancelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsaans 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        #importcsvbtn
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #exportcsvbtn
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #updatebtn
        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #resetbtn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)








    







         #Rightlabelframe
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details")
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #************scroll bar table******************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)        

    #***************fetch data**************************

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

     #immportcsv   
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
            self.fetchData(mydata)

    #exportcsv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("no data","no data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i) 
                messagebox.showinfo("data export","your data exported to"+os.path.basename(fln)+"succesfuly")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_rolll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")











        
      

if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
