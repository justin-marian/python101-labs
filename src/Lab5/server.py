from flask import Flask
from flask import jsonify, request
import json
from task import Task

app = Flask(__name__)
database = {}

#1
@app.route('/', methods=['GET'])
def sanity():
    '''Returns a simple JSON response to confirm that the server is running.'''
    response = jsonify({
        "status_code": 200
    })
    return response

#2
@app.route('/add', methods=['POST'])
def addTask():
    '''Extracts data from the incoming JSON request.'''
    data = request.json
    task_id = data['id']
    
    if task_id in database:
        return jsonify({"status_code": "400"}), 400

    task = Task(data['id'], data['name'], data['description'], data['priority'], data['status'])
    database[task.id] = task.__dict__
    return jsonify({"status_code": "200"}), 200

#3
@app.route('/print', methods=['GET'])
def showTasks():
    '''Returns all tasks in the database in JSON format.'''
    return jsonify(database), 200

#3.1
@app.route('/print/<name>', methods=['GET'])
def showEmployeeTasks(name):
    '''Returns tasks assigned to a specific employee.'''
    employee_tasks = {k: v for k, v in database.items() if v['name'] == name}
    return jsonify(employee_tasks)

#3.2
@app.route('/print/pending', methods=['GET'])
def showPendingTasks():
    '''Returns tasks with the status 'not done'.'''
    pending_tasks = {k: v for k, v in database.items() if v['status'] == 'not done'}
    return jsonify(pending_tasks)

#3.3
@app.route('/print/completed', methods=['GET'])
def showCompletedTasks():
    '''Returns tasks with the status 'completed'.'''
    pending_tasks = {k: v for k, v in database.items() if v['status'] == 'completed'}
    return jsonify(pending_tasks)

#4
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTask(id):
    '''Deletes a task by ID from the database.'''
    if id in database:
        del database[id]
        return jsonify({"status_code": "200"}), 200
    else:
        return jsonify({"status_code": "404"}), 404

#4.1
@app.route('/delete/all', methods=['DELETE'])
def deleteAllTasks():
    '''Clears the entire task database.'''
    database.clear()
    return jsonify({"status_code": "200"}), 200

#5
@app.route('/update/<id>', methods=['POST'])
def updateTaskStatus(id):
    '''Updates the status of a specific task.'''
    data = request.json
    if id in database and 'status' in data:
        database[id]['status'] = data['status']
        return jsonify({"status_code": "200"}), 200
    else:
        return jsonify({"status_code": "404"}), 404

#5.1
@app.route('/update/<id>/name', methods=['POST'])
def updateTaskAssignee(id):
    '''Updates the assignee of a specific task.'''
    data = request.json
    if id in database and 'name' in data:
        database[id]['name'] = data['name']
        return jsonify({"status_code": "200"}), 200
    else:
        return jsonify({"status_code": "404"}), 404

#6
@app.route('/save', methods=['POST'])
def saveTasks():
    '''Saves the current state of the database to a JSON file.'''
    with open('database.json', 'w') as f:
        json.dump(database, f, indent=4, sort_keys=True)
    return jsonify({"status_code" : "200"}), 200


#7
@app.route('/load', methods=['POST'])
def loadTasks():
    '''Loads tasks from a JSON file into the database.'''
    with open('database.json', 'r') as f:
        database.update(json.load(f))
    return jsonify({"status_code" : "200"}), 200
