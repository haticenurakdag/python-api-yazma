from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except Exception as exc:
        print(exc)
        data=[]
    return data

def save_data(data, filename):
    try:
        with open(filename, "w", encoding="utf-8" ) as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as exc:
        print(exc)

data_file= "contacts.json"
todos= load_data(data_file)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
   
@app.route("/todo", methods=["GET"])
def api_all():
    return jsonify(todos)
   
@app.route("/todo/<int:todo_id>", methods=["GET"])
def api_get(todo_id):
    todo =  request.json 
    todolist=[todo for todo in todos if todo["id"]== todo_id]
    if len(todolist)==0:
        return jsonify({"todo": "Not Found"}, 404)
    return jsonify({"todo":todo})


@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def api_delete(todo_id):
    todolist=[todo for todo in todos if todo["id"]== todo_id]
    if len(todolist)==0:
        return jsonify({"todo": "Not Found"}), 404
    todos.remove(todolist[0])
    save_data(todos, data_file)
    return jsonify({"result": True})

@app.route("/todo", methods=["POST"])
def api_post():
    todo =  request.json
    if not todos:
        new_id=1
    else:
        new_id=todos[-1]["id"]+1

    newtodo={
        'id': new_id,
        'todo':todo["todo"],
        'completed':todo["completed"]
    }
    todos.append(newtodo)
    save_data(todos, data_file)
    return jsonify({'todo': newtodo}),201
    
@app.route("/todo/<int:todo_id>", methods=["PUT"])
def api_put(todo_id):
    todo = request.get_json()
    todolist = next((item for item in todos if item["id"] == todo_id), None)

    todolist["todo"] = todo.get("todo", todolist["todo"])  
    todolist["completed"] = todo.get("completed", todolist["completed"]) 
    
    save_data(todos, data_file)
    return jsonify({"todo": todolist}), 200

        
if __name__ == "__main__":
    app.run(debug=True) 
      
