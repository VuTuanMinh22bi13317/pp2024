import curses
import os
import gzip
import pickle
import threading
from domains.student import Student
from domains.course import Course
from domains.classroom import Classroom
from input import get_input
from output import display_output

class PersistenceThread(threading.Thread):
    def __init__(self, classroom):
        super().__init__()
        self.classroom = classroom

    def run(self):
        compress_data(self.classroom, 'students.dat')

def compress_data(data, file_name):
    with gzip.open(file_name, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

def decompress_data(file_name):
    with gzip.open(file_name, 'rb') as f:
        return pickle.load(f)

def load_data():
    if os.path.exists('students.dat'):
        return decompress_data('students.dat')
    else:
        return Classroom()

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor

    classroom = load_data()

    display_output("Enter the number of students in this class: ")

    num_students = int(get_input())
    for _ in range(num_students):
        display_output("Enter the ID of the student: ")
        student_id = get_input()

        display_output("Enter the name of the student: ")
        name = get_input()

        display_output("Enter the date of birth of the student (in YYYY-MM-DD format): ")
        dob = get_input()

        student = Student(student_id, name, dob)
        classroom.add_student(student)

    if not classroom.students:
        display_output("There are currently no students")
    else:
        persistence_thread = PersistenceThread(classroom)
        persistence_thread.start()

    display_output("Enter the number of courses: ")
    num_courses = int(get_input())
    for _ in range(num_courses):
        display_output("Enter the ID of the course: ")
        course_id = get_input()

        display_output("Enter the name of the course: ")
        name = get_input()

        course = Course(course_id, name)
        classroom.add_course(course)

    if not classroom.courses:
        display_output("There are currently no courses")
    else:
        persistence_thread = PersistenceThread(classroom)
        persistence_thread.start()

    while True:
        display_output("""===============================================
        0. Exit
        1. Add marks for a student in a course
        2. Add student
        3. Student info
        4. List students
        5. List courses
        6. Add course
        7. Show marks for a student in a course
        """)

        option = int(get_input("Your choice: "))

        if option == 0:
            persistence_thread = PersistenceThread(classroom)
            persistence_thread.start()
            break
        elif option == 1:
            student_id, course_id, mark = get_input("Enter the details (StudentID CourseID Mark): ").split()
            classroom.add_mark(student_id, course_id, float(mark))
        elif option == 2:
            student_id, name, dob = get_input("Enter the details (ID Name DOB): ").split()
            student = Student(student_id, name, dob)
            classroom.add_student(student)
        elif option == 3:
            student_id = get_input("ID of the student: ")
            classroom.display_student_info(student_id)
        elif option == 4:
            classroom.list_students()
        elif option == 5:
            classroom.list_courses()
        elif option == 6:
            course_id, name = get_input("Enter the details (ID Name): ").split()
            course = Course(course_id, name)
            classroom.add_course(course)
        elif option == 7:
            student_id, course_id = get_input("Enter the details (StudentID CourseID): ").split()
            classroom.show_mark(student_id, course_id)
        else:
            display_output("Invalid input. Please try again!")

    stdscr.getch()

curses.wrapper(main)