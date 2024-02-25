import json


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class Student:
    row_id = 0

    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        Student.row_id += 1
        self.row_id = Student.row_id

    def calculate_grade(self):
        if self.mark >= 91:
            return 'A'
        elif self.mark >= 81:
            return 'B'
        elif self.mark >= 71:
            return 'C'
        else:
            return 'D'

#აქ ვქმნი მისამართების ეგზემპლარებს
addresses = [
    Address("Tbilisi", "Saburtalo"),
    Address("Tbilisi", "Gldani-7-11-4-93"),
    Address("Tbilisi", "Gldani-7-11-4-93"),
    Address("Tbilisi", "Gldani-7-11-4-93"),
    Address("Tbilisi", "Leselidzs str. 25"),
    Address("Tbilisi", "Varketili IV 407-5-123")
]
#აქ კი სტუდენტების
students = [
    Student("Paata", 87, addresses[0]),
    Student("Demetre", 100, addresses[1]),
    Student("Alexander", 100, addresses[2]),
    Student("Teona", 92, addresses[3]),
    Student("Nino", 99, addresses[4]),
    Student("Andria", 87, addresses[5])
]


#აქ ვინახავ სტუდენტებს jsonის დახმარებით
def save_students(filename, students):
    with open(filename, 'w') as f:
        json.dump([vars(student) for student in students], f, indent=2)

#ვკითხულობ შენახულ მონაცემებს
def read_students(filename):
    with open(filename, 'r') as f:
        return json.load(f)


# ვცვლი
def modify_students(students):
    for student in students:
        student['grade'] = Student.calculate_grade(student)
    return students


#შეცვლლილი მონაცემები ისევ შევინახე ფაილში
def save_modified_students(filename, students):
    with open(filename, 'w') as f:
        json.dump(students, f, indent=2)


