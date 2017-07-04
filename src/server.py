from flask import Flask
from tasks import make_celery
#import  celery.tasks
#from  celery.tasks import tasks
app = Flask(__name__)

# celery config
app.config.update(
    CELERY_BROKER_URL='amqp://pin:pinpin@localhost/pinvh',
    CELERY_RESULT_BACKEND='amqp://pin:pinpin@localhost/pinvh'
)
celery = make_celery(app)


@app.route('/')
def hello_world():
    schedule_post.delay(33)
    return 'Hello, World!'

@celery.task()
def schedule_post(path):  
    return path

if __name__ == '__main__':  
    app.run(port=8889, debug=True,host='0.0.0.0')
