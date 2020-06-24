class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + self.birth_year


name_ = input()
last_name_ = input()
birth_year_ = input()

student = Student(name_, last_name_, birth_year_)
print(student.id)
