import requests
from time import sleep
from celery import current_task
from src.celery_app import celery_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import News
from datetime import datetime


@celery_app.task()
def scheduled_task() -> str:
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "category": "business",
        "apiKey": "3254b2f75aab47038636a6772c093c02"
    }
    response = requests.get(url, params=params)
    news_data = response.json()

    engine = create_engine("mysql+pymysql://root@localhost/mydb")
    Session = sessionmaker(bind=engine)
    session = Session()

    for article in news_data["articles"]:
        news = News(
            source_id=article.get('source').get('id'),
            source_name=article.get('source').get('name'),
            author=article.get('author'),
            title=article.get('title'),
            description=article.get('description'),
            url=article.get('url'),
            urlToImage=article.get('urlToImage'),
            published_at=datetime.strptime(article.get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ"),
            content=article.get('content')
        )
        session.add(news)
    session.commit()
    session.close()

    return "Completed..."

