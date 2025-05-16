import mysql.connector
import getpass
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
   return executeStatement(createConnection(username, password), statement)

def getTeacherSchedule(teacher_ID):
   return


# anti owen code
username = getpass.getpass("Enter your username: ")
password = getpass.getpass("What is your password: ")
answer = input("Are you a student or a teacher? ")
answer = answer.lower()
if answer == "student" | answer == "s":
   student_ID = input("Enter your studentID: ")
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

elif answer == "teacher" | answer == "t":
   teacher_ID = input("Enter your studentID: ")
   teacherInfo = getTeacherSchedule(teacher_ID)
   for info in teacherInfo:
      roomNumber = info[3]
      courseName = info[2]
      period = info[1]
      print("Period: " + str(period))
      print("Course: " + courseName)
      print("Room Number: " + roomNumber)
      print()
