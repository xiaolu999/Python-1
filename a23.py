class Person:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
class Stu(Person):
    def __init__(self,name,sex,score):
        super().__init__(name,sex,)
        self.score = score
students = Stu('jack','math',90)
print('学生的名字{0},学生的科目{1},学生的成绩{2}'.format(students.name,students.sex,students.score))