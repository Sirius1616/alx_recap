#!/usr/bin/env python

from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]




@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    
    return jsonify({'tasks':task[0]})

@app.route('/task/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({'tasks': tasks}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task' : task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])

    return jsonify('result: True')

@auth.get_password
def get_password(username):
    if username == 'john':
        return 'Python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'unauthorized access'}), 401)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})


@app.errorhandler(404)
def not_found(error):
    return (make_response(jsonify({'error' : 'not found'}), 404))

if __name__ == "__main__":
    app.run(debug=True)

