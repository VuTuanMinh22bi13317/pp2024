import curses
from domains.student import Student
from domains.course import Course
from domains.classroom import Classroom
from input import get_input
from output import display_output

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor
    display_output("Enter the number of students in this class: ")

    classroom = Classroom()

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
        display_output("There is currently no student")
    else:
        with open('students.txt', 'w') as f:
            for student in classroom.students:
                f.write(f"{student.student_id},{student.name},{student.dob}\n")

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
        display_output("There is currently no course")
    else:
        with open('courses.txt', 'w') as f:
            for course in classroom.courses:
                f.write(f"{course.course_id},{course.name}\n")

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

    # Write marks to marks.txt
    if classroom.students:
        with open('marks.txt', 'w') as f:
            for student in classroom.students:
                for course_id, mark in student.marks.items():
                    f.write(f"{student.student_id},{course_id},{mark}\n")

    # Calculate and display student GPAs
    course_credits = []
    for _ in range(num_courses):
        course_credits.append(float(get_input(f"Enter the credit for course {_ + 1}: ")))

    classroom.calculate_student_gpas(course_credits)
    classroom.sort_students_by_gpa()

    display_output("Students sorted by GPA:")
    for i, student in enumerate(classroom.students):
        display_output(f"{i + 1}. {student.name} - GPA: {student.gpa}")

    stdscr.getch()

curses.wrapper(main)