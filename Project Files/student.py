# This is student.py for Muhammad Rizwan's Final Project for COMPUTING I
# Implements the StudentModule class for handling student-related functionalities

from data_handler import load_users_from_csv, load_enrollments_from_csv, load_courses_from_csv;  # Import necessary functions from data_handler

class StudentModule:  # Define the StudentModule class
    def __init__(self):  # Constructor for the StudentModule class
        self.students = load_users_from_csv('student_data.csv');  # Load student data from CSV
        self.enrollments = load_enrollments_from_csv('enrollment_data.csv');  # Load enrollment data from CSV

    def login(self):  # Method for student login
        max_attempts = 5;  # Set the maximum number of login attempts
        attempts = 0;  # Initialize attempts counter

        while attempts < max_attempts:  # Loop until max attempts are reached
            entered_username = input("Enter student username: ");  # Get entered username
            entered_password = input("Enter student password: ");  # Get entered password

            for student in self.students:  # Loop through student data
                if student['username'] == entered_username and student['password'] == entered_password:  # Check if credentials match
                    print("Student authentication successful!");  # Print authentication success message
                    return entered_username;  # Return the entered username indicating successful login

            print("Invalid student credentials. Please try again.");  # Print invalid credentials message
            attempts += 1;  # Increment attempts counter

        print("Too many invalid attempts. Exiting Student Module.");  # Print message for too many invalid attempts
        return None;  # Return None indicating login failure

    def view_enrolled_courses(self, student_username):  # Method for viewing enrolled courses
        print(f"Enrolled courses for {student_username}:");  # Print header for enrolled courses
        for enrollment in self.enrollments:  # Loop through enrollments
            if enrollment['student_username'] == student_username:  # Check if enrollment matches student username
                course_number = enrollment['course_number']; # Get course number from enrollment
                course = self.get_course_by_number(course_number);  # Get course information by course number
                if course:  # Check if course information is available
                    print(f"Course Number: {course_number}, Title: {course['title']}");  # Print course information

    def get_course_by_number(self, course_number):  # Method for getting course information by course number
        courses = load_courses_from_csv('course_data.csv');  # Load course data from CSV
        for course in courses:  # Loop through courses
            if course['course_number'] == course_number:  # Check if course number matches
                return course;  # Return course information
        return None;  # Return None if course information is not found

    def run_student_module(self):  # Method for running the student module
        entered_username = self.login();  # Perform student login
        if not entered_username:  # Check if login fails
            return;  # Exit the function if login fails

        self.view_enrolled_courses(entered_username);  # View enrolled courses for the logged-in student
