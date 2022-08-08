from app import db

#create the database table
class BookList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String(500), index=True)
    description = db.Column(db.String(500))
    startdate = db.Column(db.DateTime('%Y-%m-%d'))
    complete = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '{}{}{}{}{}{}'.format(self.id, self.booktitle, self.description, self.startdate, self.complete, self.author_id)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True)
    contact_number = db.Column(db.String(20), index=True)
    books = db.relationship(
        'BookList', backref='author', lazy='dynamic')

    def __repr__(self):
        return '{}{}{}{}'.format(self.id, self.name, self.contact_number, self.books)
    
