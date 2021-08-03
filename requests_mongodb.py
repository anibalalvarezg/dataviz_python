import requests
from pymongo import MongoClient

REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"
def REST_country_request(field='all', name=None, params=None):
    headers={'User-Agent': 'Mozilla/5.0'}
    if not params:
        params = {}
    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')
    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL: ' + url)
    response = requests.get(url, params=params, headers=headers)
    if not response.status_code == 200:
        raise Exception('Request failed with status code ' + str(response.status_code))
    return response


def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    """ Get named database from MongoDB with/out authentication """
    # make Mongo connection with/out authentication
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s' % \
                    (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]

response = REST_country_request('currency', 'usd')
print(response.json())


db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data'] # country data collection
# Get all the RESTful country-data
response = REST_country_request()
# Insert the JSON-objects straight to our collection
col.insert_many(response.json())

res = col.find({'currencies':{'$in':['USD']}})
print(list(res))
