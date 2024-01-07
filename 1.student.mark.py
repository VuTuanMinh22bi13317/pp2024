students = []
courses = []

num_students = int(input("Enter the number of students in this class: "))
for i in range(num_students):
    id = input(f"Enter the ID of student {i+1}: ")
    name = input(f"Enter the name of student {i+1}: ")
    dob = input(f"Enter the date of birth of student {i+1} (in YYYY-MM-DD format): ")
    students.append((id, name, dob, {}))

if len(students) == 0:
    print("There is currently no student")

def add_students(student_list):
    id = input(f"Enter the ID of student : ")
    name = input(f"Enter the name of student : ")
    dob = input(f"Enter the date of birth of student (in YYYY-MM-DD format): ")
    students.append((id, name, dob, {}))

def display_student_info(students_list):
    student_id = input("ID of the student: ")
    for student in students_list:
        if student[0] == student_id:
            print(f"Student ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Date of Birth: {student[2]}")
            break
    else:
        print(f"No student found with ID {student_id}")

num_courses = int(input("Enter the number of courses: "))
for i in range(num_courses):
    id = input(f"Enter the ID of course {i+1}: ")
    name = input(f"Enter the name of course {i+1}: ")
    courses.append((id, name))

def add_course(course_list):
    id = input(f"Enter the ID of the course: ")
    name = input(f"Enter the name of the course: ")
    courses.append((id, name))

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
    """)
    try:
        option = int(input("Your choice: "))
    except ValueError:
        print("Invalid input, please enter a valid option.")
        continue
    if option == 0:
        break
    elif option == 1:
        student_id = input("Enter the ID of the student: ")
        course_id = input("Enter the ID of the course: ")
        mark = float(input("Enter the mark for the student in this course: "))
        for student in students:
            if student[0] == student_id:
                student[3][course_id] = mark
    elif option == 2:
         add_students(students)# Replace with appropriate logic or function
    elif option == 3:
         display_student_info(students)
    elif option == 4:
        print("Here is the student list: ")
        for i, student in enumerate(students):
            print(f"{i+1}. {student[0]} - {student[1]} - {student[2]}")
    elif option == 5:
        print("Here is the course list: ")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course[0]} - {course[1]}")
    elif option == 6:
        add_course(courses)
    elif option == 7:
        student_id = input("Enter the ID of the student: ")
        course_id = input("Enter the ID of the course: ")
        for student in students:
            if student[0] == student_id:
                mark = student[3].get(course_id)
                if mark is None:
                    print(f"No marks found for student {student_id} in course {course_id}")
                else:
                    print(f"Student {student_id} scored {mark} in course {course_id}")
                    print(f"Student {student_id} - {student[1]} - {student[2]}")
                break
        else:
            print(f"No student found with ID {student_id}")
            
