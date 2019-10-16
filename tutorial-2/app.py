from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5432/flask_tutorial'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=True)
    email=db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username=username
        self.email=email

    def __repr__(self):
        return '<User {}>'.format(self.username)

@app.route('/')
def index():
    # return jsonify({'message':'hello world'})
    return render_template('add_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    # print(request.form)
    user=User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)