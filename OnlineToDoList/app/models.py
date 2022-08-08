from app import db

#create the database table
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tasktitle = db.Column(db.String(500))
    description = db.Column(db.String(500))
    deadline = db.Column(db.DateTime('%Y-%m-%d'))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return self.description
