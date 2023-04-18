# Set up the DB using the following commands:
# $ python
# > from app import db
# > db.create_all()
# > from models import User
# > admin = User(username='admin', email='admin@example.com')
# > db.session.add(admin)
# > db.session.commit()
# > User.query.all()

from app import db                                                        

# Example class
class Paperclip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serialnum = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Paperclip %r>' % self.serialnum
