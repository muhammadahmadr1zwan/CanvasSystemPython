# This is data_handler.py for Muhammad Rizwan's Final Project for COMPUTING I
# Implements functions for handling data loading and saving

import csv; # import csv

def load_users_from_csv(filename): # define load_user_from_csv with filename as a parameter
    users = [];  # Initialize an empty list to store user data
    try: # try for error checking
        with open(filename, newline='') as csvfile:  # Open the CSV file
            reader = csv.DictReader(csvfile);  # Create a CSV reader
            for row in reader:  # Iterate through each row in the CSV
                users.append({'username': row.get('username', ''), 'password': row.get('password', '')});  # Append user data to the list
    except FileNotFoundError: # exception
        print(f"Error: File '{filename}' not found."); # print error message
    except Exception as e: # exception
        print(f"Error loading users from '{filename}': {e}"); # print erro message
    return users;  # Return the list of user data

def load_courses_from_csv(file_path): # define load_courses_from_csv with file_path as a parameter
    courses = [];  # Initialize an empty list to store course data
    try: # try for error checking
        with open(file_path, mode='r') as file:  # Open the CSV file
            reader = csv.DictReader(file);  # Create a CSV reader
            for row in reader:  # Iterate through each row in the CSV
                courses.append({'course_number': row.get('course_number', ''), 'title': row.get('title', '')});  # Append course data to the list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.");
    except Exception as e:
        print(f"Error loading courses from '{file_path}': {e}");
    return courses;  # Return the list of course data

def load_enrollments_from_csv(file_path): # define load_enrollments_from_csv with file_path as a parameter
    enrollments = [];  # Initialize an empty list to store enrollment data
    try: # try for error checking
        with open(file_path, mode='r') as file:  # Open the CSV file
            reader = csv.DictReader(file);  # Create a CSV reader
            for row in reader:  # Iterate through each row in the CSV
                enrollments.append({'student_username': row.get('student_username', ''), 'course_number': row.get('course_number', '')});  # Append enrollment data to the list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.");
    except Exception as e:
        print(f"Error loading enrollments from '{file_path}': {e}");
    return enrollments;  # Return the list of enrollment data

def save_users_to_csv(users, file_path, username_col='username', password_col='password'): # define save_users_to_csv with users, file_path, username_col='username', password_col='password' as parameters
    try: # try for error checking
        with open(file_path, mode='w', newline='') as file:  # Open the CSV file for writing
            writer = csv.DictWriter(file, fieldnames=[username_col, password_col]);  # Create a CSV writer
            writer.writeheader();  # Write the header to the CSV file
            for user in users:  # Iterate through each user in the list
                writer.writerow({username_col: user.get('username', ''), password_col: user.get('password', '')});  # Write user data to the CSV file
    except Exception as e: # exception 
        print(f"Error saving users to '{file_path}': {e}"); # print error message

def save_courses_to_csv(courses, file_path): # define save_courses_to_csv with courses and file_path as parameters
    try: # try for error checking
        with open(file_path, mode='w', newline='') as file:  # Open the CSV file for writing
            writer = csv.DictWriter(file, fieldnames=['course_number', 'title']);  # Create a CSV writer
            writer.writeheader();  # Write the header to the CSV file
            for course in courses:  # Iterate through each course in the list
                writer.writerow({'course_number': course.get('course_number', ''), 'title': course.get('title', '')});  # Write course data to the CSV file
    except Exception as e: # exception
        print(f"Error saving courses to '{file_path}': {e}"); # print error message

def save_enrollments_to_csv(enrollments, file_path): # define save_enrollments_to_csv with enrollments and file_path as parameters
    try: # try for error checking
        with open(file_path, mode='w', newline='') as file:  # Open the CSV file for writing
            writer = csv.DictWriter(file, fieldnames=['student_username', 'course_number']);  # Create a CSV writer
            writer.writeheader();  # Write the header to the CSV file
            for enrollment in enrollments:  # Iterate through each enrollment in the list
                writer.writerow({'student_username': enrollment.get('student_username', ''), 'course_number': enrollment.get('course_number', '')});  # Write enrollment data to the CSV file
    except Exception as e: # exception 
        print(f"Error saving enrollments to '{file_path}': {e}"); # print error message
