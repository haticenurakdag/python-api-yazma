from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_data(filename):
    try:
        with open(filename, "r") as json_file:
         data = json.load(json_file)
    except Exception as exc:
        print(exc)
        data=[]
    return data

data_file= "veritabanı.json"
rehber= load_data(data_file)

@app.route("/rehber/all", methods=["GET"])
def api_all():
    return jsonify(rehber) 
if __name__ == "__main__":
        app.run(debug=True)

    
