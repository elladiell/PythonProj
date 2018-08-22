import json
from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

config = json.loads(open('C:/Users/shevc/PycharmProjects/praktika/data.json').read())

@app.route('/excel/chem/json', methods = ['GET'])
def get_elem(): return jsonify(config)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug = True)
