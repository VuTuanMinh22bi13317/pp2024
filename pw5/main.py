import curses
from domains.student import Student
from domains.course import Course
from domains.classroom import Classroom
from input import get_student_input, get_course_input, get_mark_input
from output import display_student_info, list_students, list_courses

def add_credit(classroom):
    for course in classroom.courses:
        credits = int(input(f"Enter the number of credits for course {course.course_id}: "))
        course.credits = credits

def main():
    classroom = Classroom()

    num_students = int(input("Enter the number of students in this class: "))
    for _ in range(num_students):
        student_id, name, dob = get_student_input()
        student = Student(student_id, name, dob)
        classroom.add_student(student)

    if not classroom.students:
        print("There are currently no students.")

    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id, name = get_course_input()
        credits = int(input(f"Enter the credit for the course {name}: "))  # Prompt for credits
        course = Course(course_id, name, credits)
        classroom.add_course(course)

    while True:
        print("""===============================================
        0. Exit
        1. Add marks for a student in a course
        2. Add student
        3. Student info
        4. List students
        5. List courses
        6. Add course
        7. Show marks for a student in a course
        8. Sort students by GPA
        """)

        option = int(input("Your choice: "))

        if option == 0:
            break
        elif option == 1:
            student_id, course_id, mark = get_mark_input()
            classroom.add_mark(student_id, course_id, mark)
        elif option == 2:
            student_id, name, dob = get_student_input()
            student = Student(student_id, name, dob)
            classroom.add_student(student)
        elif option == 3:
            student_id = input("Enter the ID of the student: ")
            display_student_info(classroom, student_id)
        elif option == 4:
            list_students(classroom)
        elif option == 5:
            list_courses(classroom)
        elif option == 6:
            course_id, name = get_course_input()
            classroom.add_course(Course(course_id, name))
            add_credit(classroom)  # After adding a course, add credits
        elif option == 7:
            student_id, course_id = input("Enter the details (StudentID CourseID): ").split()
            classroom.show_mark(student_id, course_id)
        elif option == 8:
            classroom.sort_students_by_gpa()
            print("Students sorted by GPA:")
            list_students(classroom)
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
