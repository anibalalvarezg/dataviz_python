from pymongo import MongoClient

nobel_winners = [{'category': 'Physics', 'name': 'Albert Einstein', 'nationality': 'Swiss', 'sex': 'male', 'year': 1921},
{'category': 'Physics', 'name': 'Paul Dirac', 'nationality': 'British', 'sex': 'male', 'year': 1933},
{'category': 'Chemistry', 'name': 'Marie Curie', 'nationality': 'Polish', 'sex': 'female','year': 1911}]

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    """ Get named database from MongoDB with/out authentication """
    # make Mongo connection with/out authentication
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%\
        (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    
    return conn[db_name]

db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]

# coll.insert_many(nobel_winners)

res = coll.find({'category':'Chemistry'})
print(list(res))

# Greater than
res = coll.find({'year': {'$gt': 1930}})
list(res)

# Boolean expression
res = coll.find({'$or':[{'year': {'$gt': 1930}},\
{'sex':'female'}]})
print(list(res))


def mongo_coll_to_dicts(dbname='test', collname='test', query={}, del_id=True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))
    if del_id:
        for r in res:
            r.pop('_id')
    return res

res = mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS)
print(res)