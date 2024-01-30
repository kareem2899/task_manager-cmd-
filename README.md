


# Taskaty: Simple Command Line Task Manager

Taskaty is a lightweight, easy-to-use task manager that operates directly from your command line. It's built in Python and provides basic functionalities such as adding, removing, checking, and resetting tasks. 

## Installation

Before you begin, ensure you have Python installed on your system. Then, follow these steps to set up Taskaty:

1. **Install Required Libraries**: Taskaty requires `tabulate` and `setuptools` to function correctly. Install them using pip:

    ```
    pip install tabulate setuptools
    ```

2. **Convert to Executable**:
    - Navigate to the 'project' directory where Taskaty is located.
    - Run the following command to convert Taskaty into an executable that can be run from the command line:

    ```
    pip install -e .
    ```

## Usage

Taskaty is designed to be intuitive and straightforward to use from the command line. Here's how you can interact with it:

### Adding a Task

To add a new task, use the `add` command followed by your task description in quotes:

```
taskaty add "new task"
```

### Removing a Task

To remove a task, use the `remove` command followed by `-t` and the task number:

```
taskaty remove -t 1
```

### Resetting Tasks

To reset and clear all tasks, use the `reset` command:

```
taskaty reset
```

### Checking a Specific Task

To check the details of a specific task, use the `check` command followed by `-t` and the task number:

```
taskaty check -t 2
```

## Support

For support, questions, or feedback, please [open an issue](#) on our GitHub repository.

---

