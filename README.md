# Simple Site Crawler


## Pre-requisites

- [Docker](https://docs.docker.com/install/#supported-platforms)
- [Docker Compose](https://docs.docker.com/compose/install/#prerequisites)

## Getting started

There are at least three containers running at any given time. A [RabbitMQ](https://www.rabbitmq.com/) message broker,
[MongoDB](https://docs.mongodb.com/) data store and task worker. The crawler makes use of [Celery](http://www.celeryproject.org/),
the distributed task queue library, it's use of which is more apparent when you scale multiple workers.

To get started, run the following command

```bash
make start_containers
```

Before starting the crawl you may wish to increase the number of worker containers, which by default is one.

```bash
docker scale worker=[NUMBER_OF_WORKERS]
```

Once things are up and running you can start a crawl of all the urls found in the crawlable_urls.txt file.

```bash
make start_crawl
```

The results of the crawl are saved into Mongo. You can connect to MongoDB from your host using the address `localhost:27018`.

## Thanks

- Tony Wang and the article ['How to build a scaleable crawler...'](https://medium.com/@tonywangcn/how-to-build-a-scaleable-crawler-to-crawl-million-pages-with-a-single-machine-in-just-2-hours-ab3e238d1c22) for which the code base is originally based upon.
- DomCop for the [link to the Open PageRank data](https://www.domcop.com/top-10-million-websites) used in lieu of the Alexa top million.