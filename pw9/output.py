def display_student_info(classroom, student_id):
    student = classroom.find_student_by_id(student_id)
    if student:
        print(student.get_info())
    else:
        print(f"No student found with ID {student_id}")

def list_students(classroom):
    for i, student in enumerate(classroom.students):
        print(f"{i + 1}. {student.student_id} - {student.name} - {student.dob}")

def list_courses(classroom):
    for i, course in enumerate(classroom.courses):
        print(f"{i + 1}. {course.course_id} - {course.name}")