import os

def write_students(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student.student_id},{student.name},{student.dob}\n")

def write_courses(courses):
    with open("courses.txt", "w") as f:
        for course in courses:
            f.write(f"{course.course_id},{course.name},{course.credits}\n")

def write_marks(students):
    with open("marks.txt", "w") as f:
        for student in students:
            for course_id, mark in student.marks.items():
                f.write(f"{student.student_id},{course_id},{mark}\n")

def write_data(students, courses):
    write_students(students)
    write_courses(courses)
    write_marks(students)

def read_data():
    students = []
    courses = []

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                student_id, name, dob = line.strip().split(",")
                students.append(Student(student_id, name, dob))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                course_id, name, credits = line.strip().split(",")
                courses.append(Course(course_id, name, int(credits)))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                student_id, course_id, mark = line.strip().split(",")
                for student in students:
                    if student.student_id == student_id:
                        student.add_mark(course_id, int(mark))
                        break

    return students, courses