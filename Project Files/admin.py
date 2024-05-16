# This is admin.py for Muhammad Rizwan's Final Project for COMPUTING I
# Implements the AdminModule class for handling admin-related functionalities

from data_handler import load_users_from_csv, load_courses_from_csv, load_enrollments_from_csv, save_users_to_csv, save_courses_to_csv, save_enrollments_to_csv;  # Import necessary functions from data_handler

class AdminModule:  # Define the AdminModule class
    def __init__(self):  # Constructor for the AdminModule class
        # Load data from CSV files during initialization
        self.admins = load_users_from_csv('admin_data.csv');  # Load admin data
        self.students = load_users_from_csv('student_data.csv');  # Load student data
        self.courses = load_courses_from_csv('course_data.csv');  # Load course data
        self.enrollments = load_enrollments_from_csv('enrollment_data.csv');  # Load enrollment data

    def login(self):  # Method for admin login
        # Authenticate admin login with a maximum number of attempts
        max_attempts = 5;  # Set the maximum number of login attempts
        attempts = 0;  # Initialize attempts counter

        while attempts < max_attempts:  # Loop until max attempts are reached
            entered_username = input("Enter admin username: ");  # Get entered username
            entered_password = input("Enter admin password: ");  # Get entered password

            for admin in self.admins:  # Loop through admin data
                if admin['username'] == entered_username and admin['password'] == entered_password:  # Check if credentials match
                    print("Admin authentication successful!");  # Print authentication success message
                    return True;  # Return True indicating successful login

            print("Invalid admin credentials. Please try again.");  # Print invalid credentials message
            attempts += 1;  # Increment attempts counter

        print("Too many invalid attempts. Exiting Admin Module.");  # Print message for too many invalid attempts
        return False;  # Return False indicating login failure

    def add_new_student(self):  # Method for adding a new student
        # Get input for adding a new student
        first_name = input("Enter student's first name: ");  # Get first name
        last_name = input("Enter student's last name: ");  # Get last name
        username = input("Enter student's unique username: ");  # Get username
        password = input("Enter student's password: ");  # Get password

        # Error checking for username uniqueness
        while any(student['username'] == username for student in self.students):  # Check for duplicate usernames
            print("Username already exists. Please choose another.");  # Print error message
            username = input("Enter student's unique username: ");  # Get a new username

        # Error checking for non-empty inputs
        if not first_name or not last_name or not username or not password:  # Check for empty input fields
            print("Please provide valid input. All fields must be non-empty.");  # Print error message
            return;  # Return, indicating error

        # Create a new student and save to CSV
        new_student = {'first_name': first_name, 'last_name': last_name, 'username': username, 'password': password};  # Create a new student
        self.students.append(new_student);  # Append the new student to the list
        save_users_to_csv(self.students, 'student_data.csv');  # Save the updated list to CSV

        print("New student added successfully!");  # Print success message

    def add_new_course(self):  # Method for adding a new course
        # Get input for adding a new course
        course_number = input("Enter unique course number: ");  # Get course number
        course_title = input("Enter course title: ");  # Get course title

        # Error checking for course number uniqueness
        while any(course['course_number'] == course_number for course in self.courses):  # Check for duplicate course numbers
            print("Course number already exists. Please choose another.");  # Print error message
            course_number = input("Enter unique course number: ");  # Get a new course number

        # Error checking for non-empty inputs
        if not course_number or not course_title:  # Check for empty input fields
            print("Please provide valid input. Both fields must be non-empty.");  # Print error message
            return;  # Return, indicating error

        # Create a new course and save to CSV
        new_course = {'course_number': course_number, 'title': course_title};  # Create a new course
        self.courses.append(new_course);  # Append the new course to the list
        save_courses_to_csv(self.courses, 'course_data.csv');  # Save the updated list to CSV

        print("New course added successfully!");  # Print success message

    def add_course_enrollment(self):  # Method for adding a new course enrollment
        # Get input for adding a new course enrollment
        student_username = input("Enter student's username: ");  # Get student username
        course_number = input("Enter course number: ");  # Get course number

        # Error checking for duplicate enrollments
        if any(enrollment['student_username'] == student_username and enrollment['course_number'] == course_number for enrollment in self.enrollments):  # Check for duplicate enrollments
            print("Enrollment already exists. Duplicate enrollments are not allowed.");  # Print error message
            return;  # Return, indicating error

            if not student_username or not course_number:  # Check for empty input fields
                print("Please provide valid input. Both fields must be non-empty.");  # Print error message
            return;  # Return, indicating error

        # Add a new course enrollment and save to CSV
        new_enrollment = {'student_username': student_username, 'course_number': course_number};  # Create a new enrollment
        self.enrollments.append(new_enrollment);  # Append the new enrollment to the list
        save_enrollments_to_csv(self.enrollments, 'enrollment_data.csv');  # Save the updated list to CSV

        print("Course enrollment added successfully!");  # Print success message

    def view_all_students(self):  # Method to view information for all students
        for student in self.students:  # Loop through students
            print(f"Name: {student['first_name']} {student['last_name']}, Username: {student['username']}");  # Print student information

    def view_all_courses(self):  # Method to view information for all courses
        for course in self.courses:  # Loop through courses
            print(f"Course Number: {course['course_number']}, Title: {course['title']}");  # Print course information

    def view_all_enrollments(self):  # Method to view information for all course enrollments
        for enrollment in self.enrollments:  # Loop through enrollments
            print(f"Student Username: {enrollment['student_username']}, Course Number: {enrollment['course_number']}");  # Print enrollment information

    def run_admin_module(self):  # Method to run the admin module with a menu of options
        while self.login():  # Continue running as long as login is successful
            print("\nAdmin Module Options:");  # Print admin module options
            print("a. Add a new student");  # Print option to add a new student
            print("b. Add a new course");  # Print option to add a new course
            print("c. Add a course enrollment");  # Print option to add a course enrollment
            print("d. View all student information");  # Print option to view all student information
            print("e. View all course information");  # Print option to view all course information
            print("f. View all enrollment information");  # Print option to view all enrollment information
            print("x. Exit Admin Module");  # Print option to exit the admin module

            option = input("Enter your choice: ").lower();  # Get user input for the chosen option

            if option == 'a':  # If option is 'a', add a new student
                self.add_new_student();
            elif option == 'b':  # If option is 'b', add a new course
                self.add_new_course();
            elif option == 'c':  # If option is 'c', add a new course enrollment
                self.add_course_enrollment();
            elif option == 'd':  # If option is 'd', view all student information
                self.view_all_students();
            elif option == 'e':  # If option is 'e', view all course information
                self.view_all_courses();
            elif option == 'f':  # If option is 'f', view all enrollment information
                self.view_all_enrollments();
