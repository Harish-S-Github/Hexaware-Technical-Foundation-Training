class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def get_grade(self):
        if(self.marks>90):
            return "A"
        elif self.marks>75 and self.marks<89:
            return "B"
        else:
            return "C"      
m1=Student("Harish",101,89)
print(m1.get_grade())
