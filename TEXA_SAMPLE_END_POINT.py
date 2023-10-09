from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the ToDo API'})

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Get a single task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    return jsonify({'task': task[0]})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if 'title' not in request.json:
        return jsonify({'message': 'Title is missing'})
    
    task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', '')
    }
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'})

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    return jsonify({'message': 'Task updated successfully'})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    
    tasks.remove(task[0])
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)