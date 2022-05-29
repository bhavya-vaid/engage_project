from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recog sys")

        #*************Variable****************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_year=StringVar()

        #firstimg
        img=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img)     

        f_lb=Label(self.root,image=self.photo1)
        f_lb.place(x=0,y=0,width=500,height=130)

        
        #secimg
        img1=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\student.jpg")
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
        img3=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\four.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img3)     

        bg_img=Label(self.root,image=self.photo4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Student Details", font=("times new roman",33,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #leftlabelframe
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photo_left=ImageTk.PhotoImage(img_left)     

        f_lb=Label(Left_frame,image=self.photo_left)
        f_lb.place(x=5,y=0,width=720,height=130)

        #current course info
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course info",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","comp","IT","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select year","2020-21","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","1","2","3")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student info",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #Student Id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #Student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #classdivison
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=20)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

         #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

         #DOB
        dob_label=Label(class_student_frame,text="dob:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Address
        address_no_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_no_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_no_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_rb1=StringVar()
        rb1=ttk.Radiobutton(class_student_frame,variable=self.var_rb1,text="take photo sample",value="Yes")
        rb1.grid(row=6,column=0)

        rb2=ttk.Radiobutton(class_student_frame,variable=self.var_rb1,text="no photo sample",value="No")
        rb2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        #savebtn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #updatebtn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #deletebtn
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #resetbtn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        
        #button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=715,height=35)

        #take_photo_btn
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        #update_photo_btn
        update_photo_btn=Button(btn_frame1,text="update photo sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        

        
        

         #Rightlabelframe
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img_right=img_right.resize((500,130),Image.ANTIALIAS)
        self.photo_right=ImageTk.PhotoImage(img_right)     

        f_lb=Label(Right_frame,image=self.photo_right)
        f_lb.place(x=5,y=0,width=720,height=130)

        #************searchsystem**********
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Student Details")
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(Search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        year_combo["values"]=("Select","Roll_No","Phone_No")
        year_combo.current(0)
        year_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("course",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #**************funtion declaration***************

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror('Error',"All filed required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_std_id.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_rb1.get()
                                                            
                                                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
  
    #*************fetch data************

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #****************get cursor*************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_rb1.set(data[14])


    #update func
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror('Error',"All filed required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","do u want to update details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_rb1.get(),
                                                            self.var_std_id.get()
                                                        ))
                else:  

                    if not Update:
                        return
                messagebox.showinfo("success", "student details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      


    #delete func
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do u want to delete student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Delete","suuccefuly deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  



    #reset func  
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select sdivision")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_rb1.set("")
        
        

        



    #******************GENERATE DATA SET/PHOTO SAMPLE*******************

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror('Error',"All filed required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_rb1.get(),
                                                            self.var_std_id.get()==id+1
                                                        ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
            


                #********** load predefined data on face fronatls from opencv**********
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)  
                            cv2.imshow("cropped face",face)

                            if cv2.waitKey(1)==13 or int(img_id)==100:
                                break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genreating data sets done")                  
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      
 
                                              
                     
if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

