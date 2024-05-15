fastapi-celery-results

uvicorn src.main:app --reload
celery -A src.celery_app worker -l info
celery -A src.celery_app beat -l info
