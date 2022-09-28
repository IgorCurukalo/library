import requests
from library.celery import app

@app.task() #bind=True, name='update_novelties_set'
def inform_new():
    print('111')