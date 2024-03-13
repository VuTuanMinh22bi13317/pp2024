import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_info(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nDate of Birth: {self.dob}"

    def calculate_gpa(self, course_credits):
        total_credits = sum(course_credits)
        total_weighted_marks = sum(mark * credit for mark, credit in zip(self.marks.values(), course_credits))
        return math.floor((total_weighted_marks / total_credits) * 10) / 10  # Round down to 1 decimal place

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def display_student_info(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student.get_info())
                break
        else:
            print(f"No student found with ID {student_id}")

    def list_students(self):
        for i, student in enumerate(self.students):
            print(f"{i + 1}. {student.student_id} - {student.name} - {student.dob}")

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.course_id} - {course.name}")

    def add_mark(self, student_id, course_id, mark):
        for student in self.students:
            if student.student_id == student_id:
                student.add_mark(course_id, mark)
                break
        else:
            print(f"No student found with ID {student_id}")

    def show_mark(self, student_id, course_id):
        for student in self.students:
            if student.student_id == student_id:
                mark = student.marks.get(course_id)
                if mark is None:
                    print(f"No marks found for student {student_id} in course {course_id}")
                else:
                    print(f"Student {student_id} scored {mark} in course {course_id}")
                    print(student.get_info())
                break
        else:
            print(f"No student found with ID {student_id}")

    def calculate_student_gpas(self, course_credits):
        for student in self.students:
            gpa = student.calculate_gpa(course_credits)
            setattr(student, 'gpa', gpa)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor
    stdscr.addstr(0, 0, "Enter the number of students in this class: ")
    stdscr.refresh()

    classroom = Classroom()

    num_students = int(stdscr.getstr().decode())
    for _ in range(num_students):
        stdscr.addstr(0, 0, "Enter the ID of the student: ")
        stdscr.refresh()
        student_id = stdscr.getstr().decode()

        stdscr.addstr(0, 0, "Enter the name of the student: ")
        stdscr.refresh()
        name = stdscr.getstr().decode()

        stdscr.addstr(0, 0, "Enter the date of birth of the student (in YYYY-MM-DD format): ")
        stdscr.refresh()
        dob = stdscr.getstr().decode()

        student = Student(student_id, name, dob)
        classroom.add_student(student)

    if not classroom.students:
        stdscr.addstr(0, 0, "There is currently no student")
        stdscr.refresh()

    stdscr.addstr(0, 0, "Enter the number of courses: ")
    stdscr.refresh()
    num_courses = int(stdscr.getstr().decode())
    for _ in range(num_courses):
        stdscr.addstr(0, 0, "Enter the ID of the course: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()

        stdscr.addstr(0, 0, "Enter the name of the course: ")
        stdscr.refresh()
        name = stdscr.getstr().decode()

        course = Course(course_id, name)
        classroom.add_course(course)

    while True:
        stdscr.addstr(0, 0, """===============================================
        0. Exit
        1. Add marks for a student in a course
        2. Add student
        3. Student info
        4. List students
        5. List courses
        6. Add course
        7. Show marks for a student in a course
        """)
        stdscr.refresh()

        stdscr.addstr(0, 0, "Your choice: ")
        stdscr.refresh()
        option = int(stdscr.getstr().decode())

        if option == 0:
            break
        elif option == 1:
            stdscr.addstr(0, 0, "Enter the details (StudentID CourseID Mark): ")
            stdscr.refresh()
            student_id, course_id, mark = stdscr.getstr().decode().split()
            classroom.add_mark(student_id, course_id, float(mark))
        elif option == 2:
            stdscr.addstr(0, 0, "Enter the details (ID Name DOB): ")
            stdscr.refresh()
            student_id, name, dob = stdscr.getstr().decode().split()
            student = Student(student_id, name, dob)
            classroom.add_student(student)
        elif option == 3:
            stdscr.addstr(0, 0, "ID of the student: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode()
            classroom.display_student_info(student_id)
        elif option == 4:
            classroom.list_students()
        elif option == 5:
            classroom.list_courses()
        elif option == 6:
            stdscr.addstr(0, 0, "Enter the details (ID Name): ")
            stdscr.refresh()
            course_id, name = stdscr.getstr().decode().split()
            course = Course(course_id, name)
            classroom.add_course(course)
        elif option == 7:
            stdscr.addstr(0, 0, "Enter the details (StudentID CourseID): ")
            stdscr.refresh()
            student_id, course_id = stdscr.getstr().decode().split()
            classroom.show_mark(student_id, course_id)
        else:
            stdscr.addstr(0, 0, "Invalid input. Please try again!")
            stdscr.refresh()

    # Calculate and display student GPAs
    course_credits = []
    for _ in range(num_courses):
        stdscr.addstr(0, 0, f"Enter the credit for course {_ + 1}: ")
        stdscr.refresh()
        course_credits.append(float(stdscr.getstr().decode()))

    classroom.calculate_student_gpas(course_credits)
    classroom.sort_students_by_gpa()

    stdscr.addstr(0, 0, "Students sorted by GPA:")
    stdscr.refresh()
    for i, student in enumerate(classroom.students):
        stdscr.addstr(i + 1, 0, f"{i + 1}. {student.name} - GPA: {student.gpa}")
        stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)