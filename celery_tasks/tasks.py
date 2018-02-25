from __future__ import absolute_import
from celery_tasks.celery import app
import time
import requests
from pymongo import MongoClient


@app.task(bind=True, default_retry_delay=10)
def fetch_url_content(self, url, scheme='http'):
    client = MongoClient('172.25.0.70', 27017)
    db = client.crawled_urls
    collection = db.results

    try:
        r = requests.get(scheme + '://' + url.strip())
        collection.insert({
            'url': url,
            'scheme': 'http',
            'status': r.status_code,
            "create_time": time.time(),
            "result": r.text
        })
    except Exception as exc:
        raise self.retry(exc=exc)

    client.close()
    return True
