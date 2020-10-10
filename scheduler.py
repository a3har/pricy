import requests
import json
import time
import grequests

urls_file = open('links.json')
links = json.load(urls_file)


for link in links:
    # tries = 0
    items = []
    url = 'http://:9080/crawl.json?spider_name=pricy&url=' + \
        link['link']
    start_time = time.time()
    # while(not items):
    # if (tries):
    #     print("Trying again : "+str(tries))
    response = requests.get(url)
    items = response.json()['items']
    # tries += 1
    try:
        print(response.json()['errors'][0])
    except:
        print(response.json())
    print("Time taken" + str(time.time()-start_time))

    print('\n\n\n')

# rs = (grequests.get(
#     'http://139.59.91.245:9080/crawl.json?spider_name=pricy&url='+u["link"]) for u in links)
# for r in grequests.map(rs):
#     print(r.json())
#     print('\n\n\n')
