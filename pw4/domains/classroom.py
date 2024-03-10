

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []

        #curses initialize
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

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

        sorted_students = sorted(self.students, key=lambda student: student.average_gpa(), reverse=True)

    def list_courses(self):
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.course_id} - {course.name}")

    def add_mark(self, student_id, course_id, mark):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student is None:
            raise ValueError(f"No student found with ID {student_id}")
        for course in self.courses:
            if course.course_id == course_id:
                credits = course.credits
                break
        else:
            raise ValueError(f"No course found with ID {course_id}")
        
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