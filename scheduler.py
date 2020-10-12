import requests
import json
import time
import pymongo
import json


def get_product_details_collection():
    try:
        database_auth_file = open('database_auth.json', 'rb')
        key = json.load(database_auth_file)
    except:
        print("ERROR : database_auth.json file not found")
        exit(0)
    client = pymongo.MongoClient(
        "mongodb+srv://"+key['username']+":"+key['password']+"@cluster0.unos1.mongodb.net/pricy?retryWrites=true&w=majority")
    db = client.pricy
    collection = db['product_details']
    database_auth_file.close()
    return collection


def update_prices():
    collection = get_product_details_collection()
    try:
        api_cred_file = open("api_cred.json", "rb")
        api_cred = json.load(api_cred_file)
    except:
        print("ERROR : api_cred.json file not found")
        exit(0)
    for product in collection.find():
        tries = 0
        items = []
        url = api_cred['url'] + product['link']
        start_time = time.time()
        while(not items):
            if (tries):
                print("Trying again : "+str(tries))
                tries += 1
            try:
                response = requests.get(url)
                items = response.json()['items']
            except:
                pass
        print(items)
        print("Time taken" + str(time.time()-start_time))
        print('\n\n\n')


if __name__ == 'main':
    update_prices()
