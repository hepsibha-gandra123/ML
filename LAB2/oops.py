# 12
# class Book:
#     def __init__(self, book_id, title, author):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

#     def __str__(self):
#         status = "Borrowed" if self.is_borrowed else "Available"
#         return f"[{self.book_id}] {self.title} by {self.author} - {status}"


# class Member:
#     def __init__(self, member_id, name):
#         self.member_id = member_id
#         self.name = name
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         if not book.is_borrowed:
#             book.is_borrowed = True
#             self.borrowed_books.append(book)
#             print(f"{self.name} borrowed '{book.title}'")
#         else:
#             print(f"Sorry! '{book.title}' is already borrowed.")

#     def return_book(self, book):
#         if book in self.borrowed_books:
#             book.is_borrowed = False
#             self.borrowed_books.remove(book)
#             print(f"{self.name} returned '{book.title}'")
#         else:
#             print(f"{self.name} did not borrow '{book.title}'")

#     def show_borrowed_books(self):
#         if not self.borrowed_books:
#             print(f"{self.name} has no borrowed books.")
#         else:
#             print(f"{self.name}'s Borrowed Books:")
#             for book in self.borrowed_books:
#                 print(f" - {book.title}")


# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)

#     def add_member(self, member):
#         self.members.append(member)

#     def show_available_books(self):
#         print("\nAvailable Books:")
#         for book in self.books:
#             if not book.is_borrowed:
#                 print(book)


# library = Library()
# book1 = Book(1, "The Alchemist", "Paulo Coelho")
# book2 = Book(2, "Atomic Habits", "James Clear")
# book3 = Book(3, "Python Basics", "John Doe")
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# member1 = Member(101, "Alice")
# member2 = Member(102, "Bob")
# library.add_member(member1)
# library.add_member(member2)
# library.show_available_books()
# member1.borrow_book(book1)
# member2.borrow_book(book1)
# member1.show_borrowed_books()
# member1.return_book(book1)
# library.show_available_books()

# 11
# class BankAcount:
#     def __init__(self, amount):
#         self.balance = amount

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if (amount > self.balance):
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount

#     def get_balance(self):
#         print("your available balance is:", self.balance)


# cust1 = BankAcount(1000)
# cust1.deposit(500)
# cust1.withdraw(200)
# cust1.get_balance()

# 10
# scores = list(
#     map(int, input("Enter student scores separated by space: ").split()))
# sorted_scores = sorted(scores)
# print("Sorted Scores:", sorted_scores)
# unique_scores = list(set(sorted_scores))
# unique_scores.sort()
# print("Scores after removing duplicates:", unique_scores)
# average_score = sum(unique_scores) / len(unique_scores)
# print("Average Score:", average_score)

# 9
# import re
# phone = input("Enter your phone number:")

# pattern = r"^\d{3}-\d{3}-\d{4}$"  # r-raw string
# if re.match(pattern, phone):
#     print("Valid phone number")
# else:
#     print("Invalid phone number")

# import re
# email = input("Enter your email address:")
# pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"  # . means any character

# if re.match(pattern, email):
#     print("Valid email address")
# else:
#     print("Invalid email address")

# 8
# import math


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def circumference(self):
#         return 2 * math.pi * self.radius


# c = Circle(5)
# print("Area:", c.area())
# print("Circumference:", c.circumference())

# 7
# from random import randint


# class Generate:
#     def generate(self, start, end, n):
#         for i in range(n):
#             print(randint(start, end))


# g = Generate()
# g.generate(1, 100, 5)

# 6
# multiple inheritance-multiple parent one child
# multilevel inheritance-one parent one child one grandchild
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Teacher():
#     def __init__(self, subject):
#         self.subject = subject


# class Human(Person, Teacher):
#     def __init__(self, name, age, subject):
#         Person.__init__(self, name, age)
#         Teacher.__init__(self, subject)

#     def info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)


# h = Human("William", 26, "sorceror")
# h.info()

# 5
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Student ID:", self.student_id)


# s = Student("Hepsibha", 19, "N221049")
# s.info()


# 4
# class Student:
#     """class variable and instance variable"""
#     s = "RGUKT"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("College:", Student.s)


# s = Student("Hepsibha", 19)
# print(Student.__name__)
# print(Student.__doc__)
# print(Student.__dict__)  # attributes of class
# print(Student.__bases__)  # parent classes
# print(id(s))

# print(dir(Student))


# 3
# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1
#         print(f"Object created! Total objects: {Counter.count}")
# obj1 = Counter()
# obj2 = Counter()
# obj3 = Counter()

# 2
# class Employee:
#     def __init__(self, emp_id, name, salary, date_of_joining):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary
#         self.date_of_joining = date_of_joining
#     def display(self):
#         print("\nEmployee Details")
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Date of Joining:", self.date_of_joining)
# emp_id = int(input("Enter Employee ID: "))
# name = input("Enter Employee Name: ")
# salary = float(input("Enter Salary: "))
# doj = input("Enter Date of Joining (DD-MM-YYYY): ")
# emp = Employee(emp_id, name, salary, doj)
# emp.display()


# 1
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.percentage = 0

    def calculate_percentage(self):
        self.percentage = sum(self.marks) / len(self.marks)
        return self.percentage

    def calculate_grade(self):
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 75:
            return "B"
        elif self.percentage >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("\nStudent Details")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())


student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
marks = list(map(int, input("Enter marks separated by space: ").split()))
student = Student(student_id, name, marks)
student.display()
