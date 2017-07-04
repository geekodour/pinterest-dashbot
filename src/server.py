from flask import Flask
app = Flask(__name__)
# celery config
app.config['CELERY_BROKER_URL'] = 'amqp://pin:pinpin@localhost/pinvh'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://pin:pinpin@localhost/pinvh'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])  
celery.conf.update(app.config)  

@app.route('/')
def hello_world():
    return 'Hello, World!'


@celery.task()
def schedule_post(self, path):  
    return result
