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


def main():
    classroom = Classroom()

    num_students = int(input("Enter the number of students in this class: "))
    for _ in range(num_students):
        student_id = input(f"Enter the ID of the student: ")
        name = input(f"Enter the name of the student: ")
        dob = input(f"Enter the date of birth of the student (in YYYY-MM-DD format): ")
        student = Student(student_id, name, dob)
        classroom.add_student(student)

    if not classroom.students:
        print("There is currently no student")

    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input(f"Enter the ID of the course: ")
        name = input(f"Enter the name of the course: ")
        course = Course(course_id, name)
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
        """)
    
        option = int(input("Your choice: "))

        if option == 0:
            break
        elif option == 1:
            classroom.add_mark(*input("Enter the details (StudentID CourseID Mark): ").split())
        elif option == 2:
            classroom.add_student(Student(*input("Enter the details (ID Name DOB): ").split()))
        elif option == 3:
            classroom.display_student_info(input("ID of the student: "))
        elif option == 4:
            classroom.list_students()
        elif option == 5:
            classroom.list_courses()
        elif option == 6:
            classroom.add_course(Course(*input("Enter the details (ID Name): ").split()))
        elif option == 7:
            classroom.show_mark(*input("Enter the details (StudentID CourseID): ").split())
        else:
            print("Invalid input. Please try again!")




if __name__ == "__main__":
    main()
