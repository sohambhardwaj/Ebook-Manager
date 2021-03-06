from ebook_management import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_reader(reader_id):
    return reader.query.get(int(reader_id))

class reader_books(db.Model) :
	__tablename__ = 'Reader_Books'
	reader_id=db.Column('reader_id',db.Integer,db.ForeignKey('reader.reader_id'),primary_key=True)
	book_id=db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'),primary_key=True)
	content=db.Column('content',db.Text,nullable=True)

class reader_books_review(db.Model):
    __tablename__='Reader_Books_Review'
    reader_id=db.Column('reader_id',db.Integer,db.ForeignKey('reader.reader_id'),primary_key=True)
    book_id=db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'),primary_key=True)
    content=db.Column('content',db.Text,nullable=True)

class reader(db.Model,UserMixin):
    reader_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(20),nullable=False)
    name=db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    books_reading=db.relationship('books',secondary='Reader_Books',backref=db.backref('readers',lazy='dynamic'))
    review_done=db.relationship('books',secondary='Reader_Books_Review',backref=db.backref('reviewers',lazy='dynamic'))
    def get_id(self):
        return (self.reader_id)
    def __repr__(self):
        return f"reader('{self.username}','{self.email}','{self.name}','{self.password}')"


class books(db.Model):
    book_id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.Integer,nullable=False)
    title=db.Column(db.String(20))
    category=db.Column(db.String(20))
    link=db.Column(db.Text)
    path=db.Column(db.Text)
    author_id=db.Column(db.Integer,db.ForeignKey('author.auth_id'))
    desc=db.Column(db.Text,default="There's a truth that adapts itself with every aestheticism of art and that's why tales are told by moonlight. Thus, in the search for something real, we try to push through limits, at the detriment of the motif-like holes that the bullets of African scepticism, and languid unease designs on our...")
    year=db.Column(db.Integer)
    # readers=db.relationship('reader',secondary='Reader_Books',backref=db.backref('books_reading',lazy='dynamic'))

    def __repr__(self):
    	return f"books('{self.isbn}','{self.title}','{self.category}')"


class Author(db.Model):
    auth_id=db.Column(db.Integer,primary_key=True)
    author_name=db.Column(db.String(20))
    author_books=db.relationship('books',backref='author')