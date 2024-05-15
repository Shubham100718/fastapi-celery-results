from celery import Celery


celery_app = Celery("worker",
                    backend="db+mysql+pymysql://root@localhost/mydb",
                    broker="redis://localhost:6379/0",
                    include=['src.worker'])

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'src.worker.scheduled_task',
        'schedule': 30.0,
    },
}

celery_app.conf.update(task_track_started=True)
