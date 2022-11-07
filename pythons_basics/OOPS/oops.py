class Student:
    def __init__(self, n , a, y, s):
        self.name = n
        self.age = a
        self.byear = y
        self.sex = s

    def read(self):
        print(f"student {self.name} is reading")

    def write(self,s):
        if s == "male":
            print(f"student {self.name} is writing war stories")
        else:
            print(f"student {self.name} is writing soft pink poems")

    def test(self,s):
        if s == "male":
            print(f'student {self.name} is giving test unwillingly')
        else:
            print(f'student {self.name} is giving test very happily')



