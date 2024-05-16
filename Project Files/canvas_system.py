# This is canvas_system.py for Muhammad Rizwan's Final Project for COMPUTING I
# Entry point to run the admin and student modules

from admin import AdminModule;  # Import the AdminModule class from the admin module
from student import StudentModule;  # Import the StudentModule class from the student module

def main():  # Define the main function
    print("Running the Canvas System");  # Print a message indicating that the Canvas System is running
    print(); # space
    print("Welcome to Canvas! Select your portal to get started: "); # Print a message introducing the Canvas system
    
    while True:  # Start an infinite loop for user interaction
        print("\nSelect Portal:");  # Display portal options
        print("1. Admin Portal"); # Display portal options
        print("2. Student Portal"); # Display portal options
        print("3. Exit"); # Display portal options

        portal_choice = input("Enter your choice (1, 2, or 3): ");  # Get user input for portal choice

        if portal_choice == '1':  # If the user chooses the Admin Portal
            admin_module = AdminModule();  # Create an instance of the AdminModule class
            admin_module.run_admin_module();  # Run the admin module
        elif portal_choice == '2':  # If the user chooses the Student Portal
            student_module = StudentModule();  # Create an instance of the StudentModule class
            student_module.run_student_module();  # Run the student module
        elif portal_choice == '3':  # If the user chooses to exit
            print("Exiting the Canvas System.");  # Print a message indicating system exit
            break;  # Exit the loop and end the program
        else:  # If the user enters an invalid choice
            print("Invalid choice. Please enter 1, 2, or 3.");  # Print an error message

if __name__ == "__main__":  # If the script is executed directly
    try:  # Start a try block to handle potential exceptions
        main();  # Call the main function when the script is executed
    except Exception as e:  # Catch any exception that might occur
        print(f"An error occurred: {e}");  # Print an error message if an exception occurs
