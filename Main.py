import mysql.connector
import getpass
import os
def createConnection(username, password):
   connection = mysql.connector.connect(user=username,
                                        password=password,
                                        host='10.8.37.226',
                                        database=username + "_db")
   return connection

def executeStatement(connection, query):
   cursor = connection.cursor()
   cursor.execute(query)
   studentList = []

   for row in cursor:
       studentList.append(row)

   cursor.close()
   connection.close()
   return studentList

def getStudentSchedule(student_ID):
   statement = "CALL getStudentClasses(" + student_ID + ")"
   # PROCEDURE getStudentClasses(ID integer) SELECT * FROM studentClassInfo WHERE StudentID = ID;
   # CREATE VIEW studentClassInfo AS -> SELECT StudentID, Period, CourseName, RoomNumber, Name FROM (SELECT StudentID, Period, CourseName, RoomNumber, TeacherID FROM (SELECT Courses.CourseID, ClassID, TeacherID, Period, RoomNumber, CourseName, CourseTypeID FROM Classes INNER JOIN Courses ON Classes.CourseID = Courses.CourseID) AS Chud INNER JOIN Rosters ON Rosters.ClassID = Chud.ClassID) AS finalList INNER JOIN Teachers ON Teachers.TeacherID = finalList.TeacherID;
   return executeStatement(createConnection(username, password), statement)

def getTeacherSchedule(teacher_ID):
   statement = "SELECT * FROM teacherClasses WHERE teacherID=" + teacher_ID + ""
   # CREATE VIEW teacherClasses AS SELECT info.TeacherID, Period, CourseName, RoomNumber, ClassID, Name FROM (SELECT TeacherID, Period, CourseName, RoomNumber, ClassID FROM Classes INNER JOIN Courses ON Classes.CourseID = Courses.CourseID) as info INNER JOIN Teachers ON Teachers.TeacherID = info.TeacherID;
   return executeStatement(createConnection(username, password), statement)

def getStudentGrades(student_ID):
   statement = "SELECT * FROM getGrades WHERE studentID=" + student_ID + ""
   # CREATE VIEW getGrades AS SELECT info.TeacherID, Period, CourseName, RoomNumber, ClassID, Name FROM (SELECT TeacherID, Period, CourseName, RoomNumber, ClassID FROM Classes INNER JOIN Courses ON Classes.CourseID = Courses.CourseID) as info INNER JOIN Teachers ON Teachers.TeacherID = info.TeacherID;
   return executeStatement(createConnection(username, password), statement)

def printStudentSchedule():
   studentInfo = getStudentSchedule(student_ID)
   for info in studentInfo:
      teacherName = info[4]
      roomNumber = info[3]
      courseName = info[2]
      period = info[1]
      print("Period: " + str(period))
      print("Course: " + courseName)
      print("Room Number: " + roomNumber)
      print("Teacher: " + teacherName)
      print()

def printTeacherSchedule():
   teacherInfo = getTeacherSchedule(teacher_ID)
   teacherName = teacherInfo[0][5]
   os.system('cls')
   print("Welcome " + teacherName + "!")
   for info in teacherInfo:
      classID = info[4]
      roomNumber = info[3]
      courseName = info[2]
      period = info[1]
      print("Period: " + str(period))
      print("Course: " + courseName)
      print("Room Number: " + roomNumber)
      print("ClassID: " + str(classID))
      print()

def something(ID):
   return


# anti owen code
username = getpass.getpass("Enter your username for the database: ")
password = getpass.getpass("What is your password for the database: ")
os.system('cls')
answer = input("Are you a student or a teacher? ")
answer = answer.lower()

if answer == "student" or answer == "s":
   student_ID = input("Enter your studentID: ")
   while True:
      os.system('cls')
      print("What would you like to do?")
      print("1) See your schedule")
      print("2) See your grades")
      print("3) Quit ")
      ans = input()
      os.system('cls')
      if ans == "1":
         printStudentSchedule()
         input("Enter anything to return")
      elif ans == "2":
         print("C")
      elif ans == "3":
         print("GOODBYE !!!")
         break


elif answer == "teacher" or answer == "t":
   teacher_ID = input("Enter your teacherID: ")
   while True:
      os.system('cls')
      print("What would you like to do?")
      print("1) See your schedule")
      print("2) Check your rosters/classes")
      print("3) Check student grades")
      print("4) Add an assignment")
      print("5) Edit grades")
      print("6) Quit ")
      ans = input()
      os.system('cls')
      if ans == "1":
         printTeacherSchedule()
         input("Enter anything to return")
      elif ans == "2":
         print("Cool")
      elif ans == "3":
         print("GOODBYE !!!")
         break

elif answer == "ADMIN" or answer == "admin":
   print("Hello Admin")