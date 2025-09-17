from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/todos.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(200), nullable=False)

# Create database within app context
with app.app_context(): 
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST']) 
def add_task(): 
    task_content = request.form.get('task') 
    if task_content: 
        new_task = Task(content=task_content) 
        db.session.add(new_task) 
        db.session.commit() 
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id): 
    task = Task.query.get_or_404(task_id) 
    db.session.delete(task) 
    db.session.commit() 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
    
    