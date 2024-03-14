import math

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