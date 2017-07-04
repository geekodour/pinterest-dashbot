from flask import Flask
from tasks import make_celery
app = Flask(__name__)

# celery config
app.config.update(
    CELERY_BROKER_URL='amqp://pin:pinpin@localhost/pinvh',
    CELERY_RESULT_BACKEND='amqp://pin:pinpin@localhost/pinvh'
)
celery = make_celery(app)

@celery.task
def schedule_post(path):  
    return path

@app.route('/')
def hello_world():
    schedule_post(23)
    return 'Hello, World!'

if __name__ == '__main__':  
    app.run(port=8889, debug=True,host='0.0.0.0')
