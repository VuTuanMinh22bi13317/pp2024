class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_info(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nDate of Birth: {self.dob}\n"

    def average_gpa(self):
        credits = []
        marks = []

        for course_id, mark in self.marks.items():
            course = self.find_course_by_id(course_id)
            if course:
                credits.append(course.credits)
                marks.append(mark)

        if len(credits) == 0:
            return 0.0

        weighted_sum = np.dot(credits, marks)
        total_credits = np.sum(credits)
        average_gpa = weighted_sum / total_credits

         return self.round_down(average_gpa)

    def round_down(self, score):
        return math.floor(score * 10) / 10