from celery import shared_task
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import News
from datetime import datetime


@shared_task
def fetch_and_store_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "category": "business",
        "apiKey": "3254b2f75aab47038636a6772c093c02"
    }
    response = requests.get(url, params=params)
    news_data = response.json()

    engine = create_engine("mysql://root@localhost/mydb")
    Session = sessionmaker(bind=engine)
    session = Session()

    for article in news_data["articles"]:
        news = News(
            title=article["title"],
            description=article["description"],
            source=article["source"]["name"],
            published_at=datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
        )
        session.add(news)
    session.commit()
    session.close()

