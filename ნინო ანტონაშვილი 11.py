my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}


def ids(data):
    print("Available Student IDs:", ", ".join(str(student["id"]) for student in data["students"]))

def information(data, student_id):
    student = next((stu for stu in data["students"] if stu["id"] == student_id), None)

    if student:
        print(f"Student Information:")
        print(f"ID: {student['id']}, Name: {student['name'].capitalize()}, Age: {student['age']}")

        print("\nSubject Grades:")
        for subject in data["subjects"]:
            subject_id = str(subject["id"])
            grade = subject["grades"].get(str(student_id), "N/A")
            print(f"Subject: {subject['name']}, Grade: {grade}")

    else:
        print(f"Student with ID {student_id} not found.")

#magalitad
ids(my_dict)
user_input = int(input("Enter a student ID: "))
information(my_dict, user_input)
