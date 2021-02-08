from extensions import db

class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column('fname', db.String(50))
    
    def __init__(self, fname):
        self.fname = fname
