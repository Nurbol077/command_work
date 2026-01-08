print("Start Project")


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


Student = Student('marat', 90)
print(Student.name)
print(Student.score)


