import csv

def add_student_to_csv(id, name, age, grade, subject_name, marks):
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, grade, subject_name, marks])
    print("Student added successfully to CSV.")

# magalitad
add_student_to_csv(1, 'John', 20, 'A', 'Math', 90)
add_student_to_csv(2, 'Alice', 22, 'B', 'English', 85)

import csv

def read_all():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def read_single_student_info(id):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == str(id):
                print(f"Student Information for ID {id}: {row}")
                return
        print(f"Student with ID {id} not found.")

#magalitad
read_all()
student_id_to_read = int(input("Enter the student ID to view details: "))
read_single_student_info(student_id_to_read)


import csv

def change_student_grade():
    id = int(input("Enter the student ID: "))
    subject_name = input("Enter the subject name: ")
    new_grade = input("Enter the new grade: ")

    data = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == str(id) and row[4] == subject_name:
                row[3] = new_grade
            data.append(row)

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Grade for student with ID {id} in subject {subject_name} changed to {new_grade}.")

change_student_grade()
#rata vnaxot shecvlili file
read_all()