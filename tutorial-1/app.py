from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# init app
app=Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message':'Hello World'})

# run server
if __name__=='__main__':
    app.run(debug=True)
