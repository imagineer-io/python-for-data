# class Student:
#     name = "marco"
#     def say_hi(self):
#         print("hi, this is " + self.name)

# student = Student()
# print(student.name)
# student.say_hi()

class Student:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hi, this is " + self.name)

student = Student("irene")
student.say_hi()
