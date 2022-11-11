from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask App Start</h1>"

if __name__=='__main__':
    app.run(debug=True)