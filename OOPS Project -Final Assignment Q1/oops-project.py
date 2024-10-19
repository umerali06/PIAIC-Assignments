# Base University Class
class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_info(self):
        print(f"\n{'-'*10} University Info {'-'*10}")
        print(f"University Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"{'-'*35}\n")


# Human Class inheriting University
class Human(University):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_labor = []
        self.list_of_teacher = []
        self.list_of_student = []
        self.list_of_librarian = []

    def add_labor(self, labor):
        self.list_of_labor.append(labor)

    def add_teacher(self, teacher):
        self.list_of_teacher.append(teacher)

    def add_student(self, student):
        self.list_of_student.append(student)

    def add_librarian(self, librarian):
        self.list_of_librarian.append(librarian)

    def remove_student(self, student):
        if student in self.list_of_student:
            self.list_of_student.remove(student)

    def show_human_resources(self):
        print(f"\n{'-'*10} Human Resources {'-'*10}")
        print(f"Labor: {', '.join(self.list_of_labor)}")
        print(f"Teachers: {', '.join(self.list_of_teacher)}")
        print(f"Students: {', '.join(self.list_of_student)}")
        print(f"Librarians: {', '.join(self.list_of_librarian)}")
        print(f"{'-'*35}\n")


# Assets Class inheriting University
class Assets(University):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_bus = []
        self.list_of_room = []
        self.list_of_AC = []
        self.list_of_computer = []

    def add_bus(self, bus):
        self.list_of_bus.append(bus)

    def add_room(self, room):
        self.list_of_room.append(room)

    def add_AC(self, AC):
        self.list_of_AC.append(AC)

    def add_computer(self, computer):
        self.list_of_computer.append(computer)

    def show_assets(self):
        print(f"\n{'-'*10} University Assets {'-'*10}")
        print(f"Buses: {', '.join(self.list_of_bus)}")
        print(f"Rooms: {', '.join(self.list_of_room)}")
        print(f"ACs: {', '.join(self.list_of_AC)}")
        print(f"Computers: {', '.join(self.list_of_computer)}")
        print(f"{'-'*35}\n")


# Campus Class inheriting University
class Campus(University):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_campus = []

    def add_campus(self, campus_name):
        self.list_of_campus.append(campus_name)

    def show_campuses(self):
        print(f"\n{'-'*10} University Campuses {'-'*10}")
        print(f"Campuses: {', '.join(self.list_of_campus)}")
        print(f"{'-'*35}\n")


# Department Class inheriting Campus
class Department(Campus):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_departments = []

    def add_department(self, department_name):
        self.list_of_departments.append(department_name)

    def remove_department(self, department_name):
        if department_name in self.list_of_departments:
            self.list_of_departments.remove(department_name)

    def show_departments(self):
        print(f"\n{'-'*10} Department Info {'-'*10}")
        print(f"Departments: {', '.join(self.list_of_departments)}")
        print(f"{'-'*35}\n")


# Library Class inheriting Department
class Library(Department):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_books = []
        self.list_of_categories = []

    def add_book(self, book_name):
        self.list_of_books.append(book_name)

    def add_category(self, category_name):
        self.list_of_categories.append(category_name)

    def show_library(self):
        print(f"\n{'-'*10} Library Info {'-'*10}")
        print(f"Books: {', '.join(self.list_of_books)}")
        print(f"Categories: {', '.join(self.list_of_categories)}")
        print(f"{'-'*35}\n")


# Courses Class inheriting Department
class Course(Department):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.list_of_courses = []

    def add_course(self, course_name):
        self.list_of_courses.append(course_name)

    def show_courses(self):
        print(f"\n{'-'*10} Course Info {'-'*10}")
        print(f"Courses: {', '.join(self.list_of_courses)}")
        print(f"{'-'*35}\n")


# Hostel Class inheriting University
class Hostel(University):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.hostel_name = name
        self.students = []

    def add_student_to_hostel(self, student_name):
        self.students.append(student_name)

    def show_hostel_info(self):
        print(f"\n{'-'*10} Hostel Info {'-'*10}")
        print(f"Hostel Name: {self.hostel_name}")
        print(f"Students: {', '.join(self.students)}")
        print(f"{'-'*35}\n")


# Student Class inheriting Course
class Student(Course):
    def __init__(self, student_name, student_roll_no, student_subject, student_teacher, student_CR=False):
        super().__init__(student_name, student_subject)
        self.student_name = student_name
        self.student_roll_no = student_roll_no
        self.student_subject = student_subject
        self.student_teacher = student_teacher
        self.student_CR = student_CR

    def show_student_info(self):
        cr_status = "Yes" if self.student_CR else "No"
        print(f"\n{'-'*10} Student Info {'-'*10}")
        print(f"Student Name: {self.student_name}")
        print(f"Roll No: {self.student_roll_no}")
        print(f"Subject: {self.student_subject}")
        print(f"Teacher: {self.student_teacher}")
        print(f"Class Representative: {cr_status}")
        print(f"{'-'*35}\n")


# Teacher Class inheriting Course
class Teacher(Course):
    def __init__(self, teacher_name, teacher_number, teacher_subject, teacher_of_classes, teacher_head_of_department=False):
        super().__init__(teacher_subject, teacher_subject)
        self.teacher_name = teacher_name
        self.teacher_number = teacher_number
        self.teacher_subject = teacher_subject
        self.teacher_of_classes = teacher_of_classes
        self.teacher_head_of_department = teacher_head_of_department

    def show_teacher_info(self):
        hod_status = "Yes" if self.teacher_head_of_department else "No"
        print(f"\n{'-'*10} Teacher Info {'-'*10}")
        print(f"Teacher Name: {self.teacher_name}")
        print(f"Teacher Number: {self.teacher_number}")
        print(f"Subject: {self.teacher_subject}")
        print(f"Classes: {', '.join(self.teacher_of_classes)}")
        print(f"Head of Department: {hod_status}")
        print(f"{'-'*35}\n")





# -------------------------------------------------------------------------

# Creating a University instance
uni = University("University of Agriculture", "Faisalabad")
uni.show_info()

# Creating Human resources
human = Human("University Of Agriculture", "Faisalabad")
human.add_labor("Tanveer - Lab Attendent")
human.add_teacher("Dr. Qamar Nawaz - Web Programming")
human.add_student("Umer Ali - Roll No: 8051")
human.add_librarian("Sarah - Head Librarian")
human.show_human_resources()

# Adding assets
assets = Assets("University of agriculture", "faisalabad")
assets.add_bus("Bus 101")
assets.add_room("10")
assets.add_AC("AC 3000")
assets.add_computer("Dell XPS")
assets.show_assets()

# Adding Campuses
campus = Campus("UAF Main Campus", "Faisalabad")
campus.add_campus("Main Campus")
campus.add_campus("City Campus")
campus.show_campuses()

# Adding Departments
dept = Department("University of Agriculture", "Faisalabad")
dept.add_department("Computer Science")
dept.add_department("IT Department")
dept.show_departments()

# Adding Books to Library
library = Library("University of Agriculture", "Faisalabad")
library.add_book("Introduction to AI")
library.add_book("Advanced Mathematics")
library.add_category("Science")
library.add_category("Engineering")
library.show_library()

# Adding Courses
course = Course("University of Agriculture", "Faisalabad")
course.add_course("Python Programming")
course.add_course("Machine Learning")
course.show_courses()

# Adding students to Hostel
hostel = Hostel("Jinnah Hall B UAF", "Faisalabad")
hostel.add_student_to_hostel("Umer Ali")
hostel.add_student_to_hostel("M Sohaib")
hostel.show_hostel_info()

# Creating and showing a Student
student = Student("Umer Ali", "8051", "Computer Science", "Dr. Hassan Tariq", student_CR=True)
student.show_student_info()

# Creating and showing a Teacher
teacher = Teacher("Dr. Hassan Tariq", "T001", "Machine Learning", ["Class 1", "Class 2"], teacher_head_of_department=False)
teacher.show_teacher_info()

