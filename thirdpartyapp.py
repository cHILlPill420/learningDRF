from inspect import EndOfBlock
import requests
import json

URL = "http://127.0.0.1:8000/sturead/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL, data= json_data)
    data = r.json()
    print (data)



URL2 ="http://127.0.0.1:8000/stucreate/"

def create_data():
    data = {
        'name' : 'lang',
        'roll' : 103,
        'city' : 'Lalitpur'
    }
    json_data = json.dumps(data)
    r = requests.post(url= URL2, data = json_data)
    data = r.json()
    print(data)

URL3 = "http://127.0.0.1:8000/stuupdate/"

def update_data():
    data = {
        'id' : 4,
        'roll' : 104,
        'city' : 'kavre'
    }
    json_data = json.dumps(data)
    r = requests.put(url= URL3, data = json_data)
    data = r.json()
    print(data)

URL4 = "http://127.0.0.1:8000/studelete/"

def delete_data():
    data = {'id':4}
    json_data = json.dumps(data)
    r = requests.delete(url= URL4, data = json_data)
    data = r.json()
    print(data)

print("1: READ \n2: CREATE \n3: UPDATE \n4: DELETE")
a = int(input('Pick one: '))
if a==1:
    get_data()
elif a==2:
    create_data()
elif a==3:
    update_data()
else:
    delete_data()