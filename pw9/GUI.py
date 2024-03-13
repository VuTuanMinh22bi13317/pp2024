import tkinter as tk
from tkinter import messagebox
from domains.student import Student
from domains.course import Course
from domains.classroom import Classroom
from input import get_student_input, get_course_input, get_mark_input
from output import display_student_info, list_students, list_courses

class SchoolManagementGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Management System")
        self.classroom = Classroom()
        self.create_widgets()

    def create_widgets(self):
        # Define and layout your Tkinter GUI widgets here
        # For example:
        self.label = tk.Label(self, text="Welcome to School Management System")
        self.label.pack()

        self.button_list_students = tk.Button(self, text="List Students", command=self.list_students)
        self.button_list_students.pack()

        self.button_add_student = tk.Button(self, text="Add Student", command=self.add_student)
        self.button_add_student.pack()

    def list_students(self):
        # Define the action for listing students here
        list_students(self.classroom)

    def add_student(self):
        # Define the action for adding a student here
        student_id, name, dob = get_student_input()  # Get input using functions from input.py
        student = Student(student_id, name, dob)
        self.classroom.add_student(student)
        messagebox.showinfo("Success", "Student added successfully!")

if __name__ == "__main__":
    app = SchoolManagementGUI()
    app.mainloop()