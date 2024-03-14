

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