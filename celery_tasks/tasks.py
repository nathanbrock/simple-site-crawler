from __future__ import absolute_import
from celery_tasks.celery import app
import time
import requests
from pymongo import MongoClient
from reppy.robots import Robots
from requests import RequestException


@app.task(bind=True, default_retry_delay=10)
def fetch_url_content(self, url, scheme='http'):
	client = MongoClient('172.25.0.70', 27017)
	db = client.crawled_urls
	collection = db.results
	stripped_url = url.strip()

	try:
		robots = Robots.fetch(scheme + '://' + stripped_url + '/robots.txt')
	except RequestException:
		return 'FAILURE: ' + stripped_url + ' : Unable to fetch robots.txt'

	if not robots.allowed(stripped_url, 'just-some-user-agent'):
		return 'FAILURE: ' + stripped_url + ' : Robots say no'

	try:
		r = requests.get(scheme + '://' + stripped_url)

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
	return 'SUCCESS: ' + stripped_url
