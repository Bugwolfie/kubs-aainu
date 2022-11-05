''' Q1. Create a Student class and initialize it with name and roll number.
Make methods to :
1. Display - It should display all the information of the
student. 2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
(Easy) (5 marks)'''
class Student():

    def __init__(self,k,r):
        self.name = k
        self.roll_no = r

    def info(self):
        print(f"{self.name}'s roll no is {self.roll_no}")

    def set_age(self):
        current_year = 2022
        age = int(input("enter your birth year = "))
        ages = current_year-age
        print(f"{self.name} your age is {ages}")

    def set_marks(self):
        marks = {}
        marks["eng"] = int(input("enter your marks of english = "))
        marks["hin"] = int(input("enter your marks of hindi = "))
        marks["maths"] = int(input("enter your marks of maths = "))
        print(f"{self.name} \nroll no = {self.roll_no} \n below is your mark sheet \n note: all the marks are out of 100")
        print(marks)
        print("please get it signed by your parents within a week")


    
k = input("enter your name here = ")
r = int(input("enter your shitty roll no here = "))
k = Student(k,r)
k.info()
k.set_age()
k.set_marks()











'''Q2. Create a Circle class and initialize it with radius. Make two methods
getArea and getCircumference inside this class.
(Easy) (5 marks)'''







'''
Q3. Create a Temperature class.
Make two methods :
1. convertFahrenheit - It will take celsius and will print it into
Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into
Celsius.'''


