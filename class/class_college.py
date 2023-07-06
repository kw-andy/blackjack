class Student:

    number_of_students = 0
    school = 'Online School'

    def __init__(self, first_name: object, last_name: object, major: object) -> object:
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def greetings(self):
        return f"Hello I am {self.first_name} {self.last_name}"

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major

    def greetings(self):
        return f"{self.first_name} is a college student"


class NonCollegeStudent(Student):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__(first_name, last_name)
        self.future_adult_job = future_adult_job

    def grow_up(self):
        return f"When I grow up, I want to be {self.future_adult_job}"


new_student = "Adil.Yamzei.English"
student3 = Student.split_students(new_student)

print(student3.major)



