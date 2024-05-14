from celery import Celery
from celery.schedules import crontab


celery_app = Celery("tasks",
                    broker="redis://localhost:6379/0",
                    backend="db+mysql://root@localhost/mydb",
                    include=['tasks']
                )

# celery_app.conf.timezone = 'UTC'

# celery_app.autodiscover_tasks(["tasks"])

celery_app.conf.beat_schedule = {
    'fetch-news-every-minute': {
        'task': 'tasks.fetch_and_store_news',
        'schedule': crontab(minute='*'),
    },
}

