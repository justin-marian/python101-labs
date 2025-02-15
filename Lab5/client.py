import requests

# The base URL for the server
url = "http://127.0.0.1:5000/"
# A set to keep track of used task IDs
used_task_ids = set()

##################################################################################################

def add_task(task_data):
    '''Add a task to the server.'''
    response = requests.post(url + "add", json=task_data)
    print(response.text)

def delete_task(task_id):
    '''Delete a task from the server by its ID.'''
    response = requests.delete(url + "delete/" + task_id)
    print(response.text)

def update_task(task_id, update_data):
    '''Update a task's status or assignee.'''
    if 'status' in update_data:
        response = requests.post(url + "update/" + task_id, json=update_data)
    elif 'name' in update_data:
        response = requests.post(url + "update/" + task_id + "/name", json=update_data)
    print(response.text)

def print_tasks(endpoint=""):
    '''Print tasks, optionally filtered by an endpoint.'''
    response = requests.get(url + endpoint) # NO FILTER
    print(response.text)

def delete_all_tasks():
    '''Delete all tasks from the server.'''
    response = requests.delete(url + "delete/all")
    print(response.text)

def save_tasks():
    '''Save tasks from the database to the server.'''
    response = requests.post(url + "save")
    print(response.text)

def load_tasks():
    '''Load tasks from the server into the database.'''
    response = requests.post(url + "load")
    print(response.text)

##################################################################################################

while True:
    command = input("Enter command: ")

    # Check the server's status
    if command == "Sanity check":
        response = requests.get(url)
        print(response.status_code)

    # Add tasks to the server
    elif command == "Add":
        task_id = input("Enter task ID: ")
        task_name = input("Enter task name: ")
        task_priority = input("Enter task priority: ")
        task_description = input("Enter task description: ")

        new_task = {
            "id": task_id,
            "name": task_name,
            "priority": task_priority,
            "description": task_description,
            "status": "not done"
        }

        add_task(new_task)
        used_task_ids.add(task_id)

    # Print all tasks in the server
    elif command == "Print":
        print_tasks()

    # Print tasks of a specific employee
    elif command == "Print Employee Tasks":
        employee_name = input("Enter employee name: ")
        print_tasks("print/" + employee_name)

    # Print all pending tasks in the server
    elif command == "Print Pending Tasks":
        print_tasks("print/pending")

    # Print all completed tasks in the server
    elif command == "Print Completed Tasks":
        print_tasks("print/completed")

    # Delete a task from the server
    elif command == "Delete":
        task_id = input("Enter task ID to delete: ")
        delete_task(task_id)

    # Delete all tasks from the server
    elif command == "Delete All":
        delete_all_tasks()

    # Complete a task in the server
    elif command == "Complete Task":
        task_id = input("Enter task ID to complete: ")
        update_task(task_id, {"status": "completed"})

    # Uncomplete a task in the server
    elif command == "Change Task Assignee":
        task_id = input("Enter task ID: ")
        new_assignee = input("Enter new assignee name: ")
        update_task(task_id, {"name": new_assignee})

    # Save all tasks in the server
    elif command == "Save":
        save_tasks()

    # Load all tasks from the server
    elif command == "Load":
        load_tasks()

    # Exit the program
    elif command == "Exit":
        break
