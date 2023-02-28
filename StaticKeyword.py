class Student:
    insttute="kODNest"

 def __init__(self):
     self.name="sachine"
     Student.course="MCP1"

 @static_method
 def static_method():
     print("Inside the static Method")
     Student.fee=25000
     Student.tech="Python"

 @classmethod
 def class_method(cls):
     print("Inside the static Method")
     Student.goal="job"
     cls.age=25

def main():
    s=Student()
    s.static_method()
    s.class_method()
    print(Student.institute)
    print(s.name)
    print(Student.course)
    print(Student.fee)
    print(Student.tech)
    print(Student.goal)
    print(Student.age)
        
