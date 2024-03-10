def get_student_input():
    student_id = input("Enter the ID of the student: ")
    name = input("Enter the name of the student: ")
    dob = input("Enter the date of birth of the student (in YYYY-MM-DD format): ")
    return student_id, name, dob

def get_course_input():
    course_id = input("Enter the ID of the course: ")
    name = input("Enter the name of the course: ")
    return course_id, name

def get_mark_input():
    student_id = input("Enter the ID of the student: ")
    course_id = input("Enter the ID of the course: ")
    mark = float(input("Enter the mark for the student in the course: "))
    return student_id, course_id, mark