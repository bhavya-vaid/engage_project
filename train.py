from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face recog sys")

        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman",33,"bold"),bg="WHITE",fg="CORNFLOWER BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photo_top=ImageTk.PhotoImage(img_top)     

        f_lb=Label(self.root,image=self.photo_top)
        f_lb.place(x=0,y=55,width=1530,height=325)

        #button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_Classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="cornflower blue",fg="white")
        b1.place(x=0,y=380,width=1530,height=60) 


        
        img_bottom=Image.open(r"C:\Users\ABC\Desktop\facerecog\college_images\face4.jpg")
        img_bottom=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photo_bottom=ImageTk.PhotoImage(img_bottom)     

        f_lb=Label(self.root,image=self.photo_bottom)
        f_lb.place(x=0,y=440,width=1530,height=325)

    def train_Classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #grayscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #************Train the classifier**************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")


if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

