from celery import Celery

app = Celery('tasks', backend='amgp', broker='amgp://')
