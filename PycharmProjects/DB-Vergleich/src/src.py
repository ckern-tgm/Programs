import psycopg2
from pymongo import MongoClient
import time

if __name__ == '__main__':
    pgtime = []
    mongotime = []


    for i in range(10):

        tstart = time.time()
        mClient = MongoClient('localhost',27017)
        db = mClient['test']
        tend = time.time()
        mongotime += [tend-tstart]

        pgtstart = time.time()
        conn = psycopg2.connect(dbname="test", user="postgres", password="admin", host='localhost')
        pgtend = time.time()
        pgtime += [pgtend-pgtstart]

    print("Mongo DB Connection: "+ str(sum(mongotime)/len(mongotime)))
    print("Postgres DB Connection: "+ str(sum(pgtime)/len(pgtime)))


# Mongo Connection
    mClient = MongoClient('localhost',27017)
    db = mClient['test']

# PG Connection
    conn = psycopg2.connect(dbname="test", user="postgres", password="admin", host='localhost')
    cur = conn.cursor()

    mongoi = []
    pgi = []
    for i in range(10):
        minsert = time.time()
        db.test.insert_one({"name" : "Chris"+str(i)})
        minsertEnd = time.time()
        mongoi += [minsertEnd-minsert]


        data = str(i)
        pginsert = time.time()
        cur.execute("INSERT INTO test1 VALUES(%s);", (data,))
        conn.commit()
        pginsertEnd = time.time()
        pgi += [pginsertEnd-pginsert]


    print("\nMongo InsertOne: " + str(sum(mongoi)/len(mongoi)))
    print("Postgres Insert: " + str(sum(pgi)/len(pgi)))




    mongos = []
    pgs = []
    for i in range(1000):
        mselect = time.time()
        db.test.find({})
        mselectEnd = time.time()
        mongos += [mselectEnd-mselect]


        pgselect = time.time()
        cur.execute('SELECT * from test1;')
        pgselectEnd = time.time()
        pgs += [pgselectEnd-pgselect]



    print("\nMongo Select time: "+str(sum(mongos)/len(mongos)))
    print("Postgres Select time: "+str(sum(pgs)/len(pgs)))