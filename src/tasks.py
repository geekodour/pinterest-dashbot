"""
$ sudo rabbitmqctl add_user pin pinpin
$ sudo rabbitmqctl add_vhost pinvh
$ sudo rabbitmqctl set_user_tags pin pintag
$ sudo rabbitmqctl set_permissions -p pinvh pin ".*" ".*" ".*"
"""
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

# app = Celery('tasks', broker='amqp://pin:pinpin@localhost/pinvh')
"""
@app.task
def add(x, y):
    return x + y"""
