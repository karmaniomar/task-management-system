# ==============================================================================
# Title: Task Manager
# Description: A simple task manager program that allows users to register, add
# tasks, view tasks, and display statistics.
# Author: Omar Karmani
# ==============================================================================

import datetime


def read_user_credentials():
    """
    Reads the user credentials from the 'user.txt' file.

    Returns:
        dict: A dictionary where keys are usernames and values are passwords.

    Raises:
        FileNotFoundError: If 'user.txt' does not exist.
        Exception: If any other error occurs while reading the file.
    """
    user_credentials = {}
    try:
        with open("user.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(", ")
                user_credentials[username] = password
    except FileNotFoundError:
        print("Error: 'user.txt' file not found. Please ensure the file exists.")
        exit()
    except Exception as e:
        print(f"An error occurred while reading 'user.txt': {e}")
        exit()
    return user_credentials


def write_user_credentials(username, password):
    """
    Writes a new username and password to the 'user.txt' file.

    Args:
        username (str): The username to be added.
        password (str): The password to be added.

    Raises:
        Exception: If there is an error writing to the file.
    """
    try:
        with open("user.txt", "a") as file:
            file.write(f"\n{username}, {password}")
    except Exception as e:
        print(f"An error occurred while writing to 'user.txt': {e}")


def read_tasks():
    """
    Reads tasks from the 'tasks.txt' file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a task.

    Raises:
        FileNotFoundError: If 'tasks.txt' does not exist.
        Exception: If any other error occurs while reading the file.
    """
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(", ")
                task = {
                    "username": task_data[0],
                    "title": task_data[1],
                    "description": task_data[2],
                    "assigned_date": task_data[3],
                    "due_date": task_data[4],
                    "completed": task_data[5],
                }
                tasks.append(task)
    except FileNotFoundError:
        print("Error: 'tasks.txt' file not found. Please ensure the file exists.")
        exit()
    except Exception as e:
        print(f"An error occurred while reading 'tasks.txt': {e}")
        exit()
    return tasks


def write_task(task):
    """
    Writes a new task to the 'tasks.txt' file.

    Args:
        task (dict): A dictionary containing task details.

    Raises:
        Exception: If there is an error writing to the file.
    """
    try:
        with open("tasks.txt", "a") as file:
            file.write(", ".join(task.values()) + "\n")
    except Exception as e:
        print(f"An error occurred while writing to 'tasks.txt': {e}")


def display_menu(is_admin):
    """
    Displays the main menu based on the user's role.

    Args:
        is_admin (bool): True if the user is an admin, False otherwise.
    """
    print("\nPlease select one of the following options:")
    if is_admin:
        print("r - Register a user")
        print("d - Delete a user")
    print("a - Add a task")
    print("va - View all tasks")
    print("vm - View my tasks")
    if is_admin:
        print("s - Display statistics")
    print("e - Exit")


def register_user():
    """
    Registers a new user by prompting for a username and password.
    The new user is written to 'user.txt'.

    Raises:
        ValueError: If the username already exists or passwords do not match.
        Exception: If any other error occurs during registration.
    """
    try:
        user_credentials = read_user_credentials()
        print("Existing users:")
        for user in user_credentials:
            if user != "admin":
                print(user)

        username = input("Enter a new username: ")
        if username in user_credentials:
            raise ValueError(
                "Username already exists. Please choose a different username."
            )

        password = input("Enter a new password: ")
        confirm_password = input("Confirm the password: ")

        if password != confirm_password:
            raise ValueError("Passwords do not match. User registration failed.")

        write_user_credentials(username, password)
        print("User registered successfully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred during registration: {e}")


def add_task():
    """
    Adds a new task by prompting for task details.
    The new task is written to 'tasks.txt'.

    Raises:
        ValueError: If the assigned username does not exist or the date format is invalid.
        Exception: If any other error occurs while adding the task.
    """
    try:
        username = input("Enter the username of the person the task is assigned to: ")
        if username not in read_user_credentials():
            raise ValueError("Username does not exist. Please enter a valid username.")

        title = input("Enter the title of the task: ")
        description = input("Enter a description of the task: ")
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

        # Validate the due date format
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        assigned_date = datetime.datetime.now().strftime("%Y-%m-%d")

        task = {
            "username": username,
            "title": title,
            "description": description,
            "assigned_date": assigned_date,
            "due_date": due_date,
            "completed": "No",
        }

        write_task(task)
        print("Task added successfully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred while adding the task: {e}")


def view_all_tasks():
    """
    Displays all tasks in an easy-to-read format.

    Raises:
        Exception: If any error occurs while viewing tasks.
    """
    try:
        tasks = read_tasks()
        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            print("\nTask Details:")
            print(f"Assigned to: {task['username']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Assigned Date: {task['assigned_date']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: {task['completed']}")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")


def view_my_tasks(current_user):
    """
    Displays tasks assigned to the current user in an easy-to-read format.

    Args:
        current_user (str): The username of the current user.

    Raises:
        Exception: If any error occurs while viewing tasks.
    """
    try:
        tasks = read_tasks()
        user_tasks = [task for task in tasks if task["username"] == current_user]

        if not user_tasks:
            print("No tasks assigned to you.")
            return

        for task in user_tasks:
            print("\nTask Details:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Assigned Date: {task['assigned_date']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Completed: {task['completed']}")
    except Exception as e:
        print(f"An error occurred while viewing your tasks: {e}")


def display_statistics():
    """
    Displays the total number of tasks and users in a user-friendly manner.

    Raises:
        Exception: If any error occurs while displaying statistics.
    """
    try:
        tasks = read_tasks()
        users = read_user_credentials()

        print(f"\nTotal number of tasks: {len(tasks)}")
        print(f"Total number of users: {len(users)}")
    except Exception as e:
        print(f"An error occurred while displaying statistics: {e}")


def delete_user():
    """
    Deletes a user by prompting for a username.
    The user is removed from 'user.txt'.

    Raises:
        ValueError: If the username does not exist or if attempting to delete admin.
        Exception: If any other error occurs while deleting the user.
    """
    try:
        user_credentials = read_user_credentials()
        print("Existing users:")
        for user in user_credentials:
            if user != "admin":
                print(user)

        username = input("Enter the username to delete: ")

        if username == "admin":
            raise ValueError("Cannot delete the admin user.")
        if username not in user_credentials:
            raise ValueError("Username does not exist. Please enter a valid username.")

        del user_credentials[username]

        with open("user.txt", "w") as file:
            for user, password in user_credentials.items():
                file.write(f"{user}, {password}\n")

        print("User deleted successfully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred while deleting the user: {e}")


def main():
    """
    Main function to handle user login and menu navigation.

    Raises:
        Exception: If any unexpected error occurs during execution.
    """
    try:
        user_credentials = read_user_credentials()

        # Login process
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in user_credentials and user_credentials[username] == password:
                print("Login successful!")
                break
            else:
                print("Invalid username or password. Please try again.")

        is_admin = username == "admin"

        # Main menu loop
        while True:
            display_menu(is_admin)
            choice = input("Enter your choice: ").lower()

            if choice == "r" and is_admin:
                register_user()
            elif choice == "d" and is_admin:
                delete_user()
            elif choice == "a":
                add_task()
            elif choice == "va":
                view_all_tasks()
            elif choice == "vm":
                view_my_tasks(username)
            elif choice == "s" and is_admin:
                display_statistics()
            elif choice == "e":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
