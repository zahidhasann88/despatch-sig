from pymongo import MongoClient
from threading import Lock

'''

client = pymongo.MongoClient("mongodb+srv://sigcen:<password>@cluster0.vubjfjb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# passwd: sigcen1234
# database name: sigcen

'''

# Singleton Class
class Database:
    db = None
    instance = None
    lock = Lock()

    def __init__(self, online=True):
        if online:
            # MONGODB_URI = "mongodb://csclassroomfeed:mlab123@ds231643.mlab.com:31643/upgbrac"
            # MONGODB_URI = 'mongodb://localhost:27017/upgbrac'
            ########## https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
            MONGODB_URI = "mongodb+srv://sigcen:sigcen1234@cluster0.vubjfjb.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(MONGODB_URI, connectTimeoutMS=30000, retryWrites=False)
            self.db = client.get_database("sigcen")
        else:
            client = MongoClient('localhost', 27017)
            self.db = client.sigcen

    @staticmethod
    def get_instance(online):
        Database.lock.acquire()
        if Database.instance is None:
            Database.instance = Database(online)
        Database.lock.release()
        return Database.instance


# Database Connection Online
database = Database.get_instance(online=True).db
print("Database Connected")
# print(database)
collection = database["users"]
x =  collection.find()
# print(x)
for data in x:
    print(data)

# uname = 'admin'
# print("searching admin")
# user_found = database["users"].find({'username': uname})
# if user_found:
#     user = user_found[0]
#     print(user['passwd'], user['role'], user['status'])


# Database Connection Offline
'''
db = Database.get_instance(online=False).db
'''