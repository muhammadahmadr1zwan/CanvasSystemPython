# This is user.py for Muhammad Rizwan's Final Project for COMPUTING I
# Defines User, Admin, and Student classes for representing users in the system

class User:  # Class representing a generic user
    def __init__(self, first_name, last_name, username, password): # Constructor for the User class
        self.first_name = first_name;  # User's first name
        self.last_name = last_name;    # User's last name
        self.username = username;      # User's username
        self.password = password;     # User's password

class Admin(User):  # Class representing an admin, inheriting from User
    def __init__(self, first_name, last_name, username, password, admin_id): # Constructor for the Admin class
        if not isinstance(admin_id, int) or admin_id <= 0:  # Add error checking for admin_id
            raise ValueError("admin_id must be a positive integer.");  # Raise an error if admin_id is not a positive integer

        super().__init__(first_name, last_name, username, password); # Call the constructor of the parent class (User)
        self.admin_id = admin_id;  # Admin's unique identifier

class Student(User):  # Class representing a student, inheriting from User
    def __init__(self, first_name, last_name, username, password, student_id): # Constructor for the Student class
        if not isinstance(student_id, int) or student_id <= 0:  # Add error checking for student_id
            raise ValueError("student_id must be a positive integer.");  # Raise an error if student_id is not a positive integer

        super().__init__(first_name, last_name, username, password);  # Call the constructor of the parent class (User)
        self.student_id = student_id;  # Student's unique identifier
