from factory import create_celery_app
from celery.signals import task_prerun
from flask import g
from extensions import db
import os

class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column('fname', db.String(50))
    
    def __init__(self, fname):
        self.fname = fname

celery = create_celery_app()

@task_prerun.connect
def celery_prerun(*args, **kwargs):
    #print g
    with celery.app.app_context():
    #   # use g.db
        print(db)
        print(g)

#@celery.task(base=celery.Task)
@celery.task(name='celery_example.insert')
def insert(path):
    with celery.app.app_context():
        for i in os.listdir(path):
            fname = i.split('.')[0]
            result = Results(fname=fname)
            db.session.add(result)
        db.session.commit()
        return 'File names inserted in Results table!'

