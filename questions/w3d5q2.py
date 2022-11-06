'''Q2. Create a Circle class and initialize it with radius. Make two methods
getArea and getCircumference inside this class.
(Easy) (5 marks)'''



class Circle:
    def __init__(self,r):
        self.radius = r

    def areas(self,r):
        self.radius = r
        area = 22/7*r**2
        print(f"area of your circle with radius <{self.radius}> is {area} sq metres")


    def circumfrences(self,r):
        self.radius = r
        circum = 2*22/7*r
        print(f"circumfrence of your circle with radius <{self.radius}> is {circum} metres")



#driver code
catcircle = Circle(34)
catcircle.areas(34)
catcircle.circumfrences(34)