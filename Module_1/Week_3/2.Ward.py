

class Student():
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        return f'Student - name: {self.name}, yob: {self.yob}, grade: {self.grade} '


class Doctor():
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        return f'Doctor - name: {self.name}, yob: {self.yob}, specialist: {self.specialist}'


class Teacher():
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        return f'Teacher - name: {self.name}, yob: {self.yob}, subject: {self.subject}'


class Ward():
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        descriptions = [person.describe() for person in self.people]
        return f"Ward: {self.name}\n" + "\n".join(descriptions)

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        total_teacher = sum(
            1 for person in self.people if isinstance(person, Teacher))
        total_yob_teacher = sum(
            person.yob for person in self.people if isinstance(person, Teacher))
        if total_teacher == 0:
            return 0

        return total_yob_teacher / total_teacher


ward1 = Ward("Ward1")

student = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
teacher2 = Teacher("teacherB", 1995, "History")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")

ward1.add_person(student)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

print(ward1.describe())
print(f'\nNumber of doctor: {ward1.count_doctor()}')

ward1.sort_age()

print("\nAfter sorting Age of Ward1 people")
print(ward1.describe())

print(
    f"\naverage of teachers: {ward1.compute_average()}")
