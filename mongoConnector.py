import pymongo

def connect():
    mgconnection = pymongo.MongoClient("mongodb+srv://dmarks:Stolik1209!@covid.mvty8a7.mongodb.net/?retryWrites=true&w=majority")
    return mgconnection

def disconnect(mgconnection):
    mgconnection.close()