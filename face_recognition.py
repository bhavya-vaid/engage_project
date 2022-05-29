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
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recog sys")


        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",33,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #1stimg
        img_top=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\facefinal.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photo_top=ImageTk.PhotoImage(img_top)     

        f_lb=Label(self.root,image=self.photo_top)
        f_lb.place(x=0,y=55,width=650,height=700)

        #2ndimg
        img_bottom=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\four.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photo_bottom=ImageTk.PhotoImage(img_bottom)     

        f_lb=Label(self.root,image=self.photo_bottom)
        f_lb.place(x=650,y=55,width=950,height=700)

         #button
        b1=Button(f_lb,text="Face Recognition",command=self.face_recog,padx=10,pady=10,cursor="hand2",font=("times new roman",18,"bold"),bg="dark blue",fg="white")
        b1.place(x=380,y=590,width=180,height=40) 

    #*************ATTENDANCE************************
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append((entry[0]))
            if((i not in name_list) and (r not in name_list) and (n not in name_list ) and (d not in name_list)):
                  now=datetime.now()
                  d1=now.strftime("%d/%m/%Y")
                  dtString=now.strftime("%H:%M:%S")
                  f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")  

    #*************Face recognition*******************

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Departmetn:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recog",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()



        

        


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
if __name__ =="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
