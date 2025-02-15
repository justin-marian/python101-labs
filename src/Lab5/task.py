import json

class Task:
    """
    Task class to represent a task in the server
    
    Attributes:
        id (str): The task ID
        name (str): The task name
        description (str): The task description
        priority (str): The task priority
        status (str): The task status
    
    Methods:
        toJson: Returns the task as a JSON string
    """
    def __init__(self, id, name, description, priority, status):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status

    def toJson(self):
        return json.dumps(self.__dict__)
