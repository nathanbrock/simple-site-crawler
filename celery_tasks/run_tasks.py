from celery_tasks.tasks import fetch_url_content

if __name__ == '__main__':
    print('Starting tasks...')

    urls_file = open("crawable_urls.txt", "r")
    urls = urls_file.readlines()

    httpScheme = 'http'

    for url in urls:
        print('Requesting content for', httpScheme + '://' + url)
        result = fetch_url_content.delay(url, httpScheme)

    urls_file.close()
