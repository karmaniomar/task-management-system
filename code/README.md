```markdown
# Task Manager Application

The **Task Manager** is a Python-based command-line application designed to help users manage tasks and user registrations efficiently. It provides features for adding tasks, viewing tasks, registering new users, and performing administrative tasks such as deleting users and displaying statistics.

---

## Features

- **User Authentication**:
  - Secure login with username and password.
  - Admin and regular user roles with differentiated access.
- **Task Management**:
  - Add new tasks with details like title, description, due date, and assigned user.
  - View all tasks or tasks assigned to the current user.
- **User Management**:
  - Register new users (admin-only feature).
  - Delete users (admin-only feature).
- **Statistics**:
  - Display the total number of tasks and users (admin-only feature).
- **Error Handling**:
  - Robust error handling for file operations, invalid inputs, and edge cases.
  - User-friendly error messages for better troubleshooting.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.13.0** installed on your system.
- Basic familiarity with command-line operations.

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Create Required Files**:
   - Create a `user.txt` file to store user credentials. The file should contain at least one admin user in the following format:
     ```
     admin, admin123
     ```
   - Create a `tasks.txt` file to store tasks. The file can be empty initially.

3. **Run the Application**:
   ```bash
   python task_manager.py
   ```

---

## Usage

### Login
- Upon running the application, you will be prompted to enter your username and password.
- Use the default admin credentials (`admin, admin123`) to access admin features.

### Main Menu
The main menu provides the following options based on the user's role:

- **Admin Options**:
  - `r`: Register a new user.
  - `d`: Delete a user.
  - `s`: Display statistics (total number of tasks and users).

- **General Options**:
  - `a`: Add a new task.
  - `va`: View all tasks.
  - `vm`: View tasks assigned to the current user.
  - `e`: Exit the application.

### Adding a Task
- When adding a task, you will be prompted to enter:
  - The username of the person the task is assigned to.
  - The title and description of the task.
  - The due date in `YYYY-MM-DD` format.

### Viewing Tasks
- Use `va` to view all tasks or `vm` to view tasks assigned to you.
- Tasks are displayed with details such as title, description, assigned date, due date, and completion status.

### Registering a User
- Admins can register new users by providing a username and password.
- Passwords must match during confirmation.

### Deleting a User
- Admins can delete users by entering the username of the user to delete.
- The admin user cannot be deleted.

### Displaying Statistics
- Admins can view the total number of tasks and users.

---

## File Structure

- `task_manager.py`: The main Python script containing the application logic.
- `user.txt`: Stores user credentials in the format `username, password`.
- `tasks.txt`: Stores task details in the format `username, title, description, assigned_date, due_date, completed`.

---

## Error Handling

The application handles the following errors gracefully:
- **File Not Found**: If `user.txt` or `tasks.txt` is missing, the program will notify the user and exit.
- **Invalid Input**: Errors such as invalid date formats, mismatched passwords, or non-existent usernames are caught and displayed.
- **Unexpected Errors**: Any unexpected errors are caught and displayed with a user-friendly message.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear and concise messages.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please reach out to:
- **Omar Karmani**  
- **Email**: omar.karmani93@gmail.com  
- **GitHub**: [karmaniomar](https://github.com/karmaniomar)

---

## Acknowledgments

- This project was created as part of a Python programming exercise.
- Special thanks to the Python community for their invaluable resources and support.
```# task-management-system
