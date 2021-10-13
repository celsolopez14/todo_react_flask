from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)