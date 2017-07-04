"""
$ sudo rabbitmqctl add_user pin pinpin
$ sudo rabbitmqctl add_vhost pinvh
$ sudo rabbitmqctl set_user_tags pin pintag
$ sudo rabbitmqctl set_permissions -p pinvh pin ".*" ".*" ".*"
"""
from celery import Celery

app = Celery('tasks', broker='amqp://pin:pinpin@localhost/pinvh')

@app.task
def add(x, y):
    return x + y
