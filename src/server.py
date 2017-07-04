from flask import Flask
from tasks import make_celery
app = Flask(__name__)

# celery config
app.config.update(
    CELERY_BROKER_URL='amqp://pin:pinpin@localhost/pinvh',
    CELERY_RESULT_BACKEND='amqp://pin:pinpin@localhost/pinvh'
)
celery = make_celery(app)
#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])  
#celery.conf.update(app.config)  

@app.route('/')
def hello_world():
    return 'Hello, World!'


@celery.task()
def schedule_post(self, path):  
    return result

if __name__ == '__main__':  
    app.run(port=8889, debug=True)
