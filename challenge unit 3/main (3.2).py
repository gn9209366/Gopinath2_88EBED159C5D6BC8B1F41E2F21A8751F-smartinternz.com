class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Use the sorted function with a lambda function as the key to sort by CGPA in ascending order.
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Gopinath", "G06", 9.8),
    Student("Hari", "H07", 9.7),
    Student("Lekha", "L08", 8.7),
    Student("Selvam", "S09", 8.8)
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
