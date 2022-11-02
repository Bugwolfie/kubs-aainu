#q2 Write a program to accept the marks of 6 students and display them in a sorted manner.
marks1 = int(input("enter the  marks of student1  = "))
marks2 = int(input("enter the  marks of student2  = "))
marks3 = int(input("enter the  marks of student3  = "))
marks4 = int(input("enter the  marks of student4  = "))
marks5 = int(input("enter the  marks of student5  = "))
marks6 = int(input("enter the  marks of student6  = "))
myStudentMarksList = [marks1, marks2, marks3, marks4, marks5, marks6]
print(myStudentMarksList)
myStudentMarksList.sort()
print(myStudentMarksList)