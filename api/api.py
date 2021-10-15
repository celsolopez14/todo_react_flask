from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable = False)

    def __str__(self):
        return f'{self.id} {self.content}'

def todo_serializer(t):

    return{

        'id': t.id,
        'content': t.content
    }

@app.route('/api', methods = ['GET'])
def index():
    
    return jsonify([*map(todo_serializer, Todo.query.all())])

@app.route('/api/add', methods = ['POST'])
def add():

    request_data = json.loads(request.data)
    todo = Todo(content = request_data['content'])
    db.session.add(todo)
    db.session.commit()

    return {'201': 'data added succesfully'}

@app.route('/api/delete', methods = ['DELETE'])
def delete():

    request_data = json.loads(request.data)
    Todo.query.filter_by(id= request_data['id']).delete()
    db.session.commit()

    return{'201':'data removed'}

if __name__ == '__main__':
    app.run(debug=True)