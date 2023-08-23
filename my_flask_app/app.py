"""FLASK kullanarak  bir API URL oluşturulmuştur
bir todo app sayfasının istek yapabilmesini sağlar"""
from typing import Union, Dict, Any
from flask import Flask, request, jsonify, render_template, json

app = Flask(__name__)
def load_data(filename: str) ->Any:
    """bu fonksiyon data dosyasını okuma işlemi yapar"""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except Exception as exc:
        raise exc
    return data

def save_data(data: Union[Dict[str,Any], int], filename: str) ->None:
    """bu fonksiyon data dosyasına yazma işlevi yapar yeni gelen verileri kaydeder"""
    try:
        with open(filename, "w", encoding="utf-8" ) as json_file:
            json.dump(data, json_file,indent=4)
    except Exception as exc:
        raise exc

DATA_FILE: str = "contacts.json"
todos= load_data(DATA_FILE)

@app.route("/", methods=["GET"])
def index() -> str:
    """bu url yolunda ana html sayfası görünür GET isteği atar"""
    return render_template("index.html")

@app.route("/todo", methods=["GET"])
def api_all() -> Any:
    """belirlenen url yoluna json dosyasındaki verileri getirir"""
    return jsonify(todos)

@app.route("/todo/<int:todo_id>", methods=["GET"])
def api_get(todo_id: int) ->Any:
    """url yolunda belirli bir id ye sahip veriyi getirir"""
    todo =  request.json

    todolist=[todo for todo in todos if todo["id"]== todo_id]
    if len(todolist)==0:
        return jsonify({"todo": "Not Found"}, 404)
    return jsonify({"todo":todo})

@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def api_delete(todo_id: int) ->Any:
    """belirlenen id nin silinmesi için DELETE isteği atar"""
    todolist=[todo for todo in todos if todo["id"]== todo_id]
    print(type(todolist))
    if len(todolist)==0:
        return jsonify({"todo": "Not Found"}), 404
    todos.remove(todolist[0])
    save_data(todos, DATA_FILE)
    return jsonify({"result": True})

@app.route("/todo", methods=["POST"])
def api_post() ->Any:
    """yeni veri eklemek için POST isteği atar"""
    if not todos:
        new_id=1
    else:
        new_id=todos[-1]["id"]+1
    todo = request.get_json()

    newtodo={
        'id': new_id,
        'todo':todo.get("todo", ""),
        'completed':todo.get("completed", False)
    }
    todos.append(newtodo)
    save_data(todos, DATA_FILE)
    return jsonify({'todo': newtodo}),201

@app.route("/todo/<int:todo_id>", methods=["PUT"])
def api_put(todo_id: int) ->Any:
    """belirlenen id deki veriyi güncellemek için PUT isteği atar"""
    todo = request.get_json()
    todolist:Dict[str, Any] = next((item for item in todos if item["id"] == todo_id), {})
    print(type(todolist))
    todolist["todo"] = todo.get("todo", todolist["todo"])
    todolist["completed"] = todo.get("completed", todolist["completed"])

    save_data(todos, DATA_FILE)
    return jsonify({"todo": todolist}), 200

if __name__ == "__main__":
    app.run(debug=True)
