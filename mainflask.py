from flask import Flask
from flask import send_from_directory, make_response, jsonify

app = Flask(__name__)

@app.route('/vendor/<path:path>')
def serve_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/')
def serve_index():
    return make_response(open('static/index.html').read())

@app.route('/rest/greet/<name>')
def greet(name):
    return jsonify(message='Hello From Flask Angular {}'.format(name))

if __name__ == "__main__":
    app.run(debug=True)
