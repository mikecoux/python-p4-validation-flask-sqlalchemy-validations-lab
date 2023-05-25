from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name', 'phone_number')
    def validate_author(self, key, field):
        if key == 'name':
            if not field:
                raise ValueError("Author must have a name.")
            # elif field in [author.name for author in Author.query.all()]:
            #     raise ValueError("No two authors can have the same name!")
        elif key == 'phone_number':
            if len(field) != 10:
                raise ValueError("Phone number must be 10 digits.")

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title', 'content', 'summary', 'category')
    def validate_post(self, key, field):
        if key == 'title':
            clickbait = ["Won't Believe", "Secret", "Top", "Guess"]

            if not field:
                raise ValueError("Posts must have a title.")
            # Super sick generator exp
            elif not any(x in field for x in clickbait):
                raise ValueError("Post titles must be clickbaity.")
        
        elif key == 'content':
            if len(field) < 250:
                raise ValueError("Posts must be at least 250 characters long.")
            
        elif key == 'summary':
            if len(field) >= 250:
                raise ValueError("Summary cannot be longer than 250 characters.")
            
        elif key == 'category':
            if field not in ['Fiction', 'Non-Fiction']:
                raise ValueError("Category must be fiction or non-fiction.")


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
