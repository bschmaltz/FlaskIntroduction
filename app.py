from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    # Send request to MISE container
    # TODO: actually send request and use response
    url = "http://localhost:8080/validatetoken"
    token = request.form["token"]
    headers = {}
    data = {}
    # r = requests.post(url = url, headers = headers, data = data)
    # if r.status_code == 200:

    # return response based on response from validator
    if True:
        return jsonify({
            "success": True,
            "inputToken": token
        })
    else:
        return jsonify({
            "success": False,
            "inputToken": token
        })

if __name__ == "__main__":
    app.run(debug=True)
