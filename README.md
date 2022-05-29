# engage_project
made using: Python OpenCV
Steps to run the project:
1) connect to a database using MySQL workbench using localhost, user='root' and password='Test@123', create table 

![image](https://user-images.githubusercontent.com/79753464/170882251-f4d78f58-958c-408e-b47a-8f977f6073ca.png)
![image](https://user-images.githubusercontent.com/79753464/170882510-8d1f3de0-c674-45be-a6af-eac88b3fdaf9.png)


2) run main.py on vscode
3) Go to student details, add details, click take photo sample radio button and click save
4) check existing folder 'data' or create new, now click take photo sample button to capture images
5) go to train face option from main.py window
6) click train data to train the model with the photo data set, a classifier.xml file will be created on success
7) go to face detector option from main.py window
8) check for existing attendance.csv file or create and empty one
9) click face recognition button
10) go to attendance option from main.py window
11) import the attendance.csv file to show attendance in frontend
