from inspect import EndOfBlock
import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL, data= json_data)
    data = r.json()
    print (data)

def create_data():
    data = {
        'id' : 5,
        'name' : 'Tng',
        'roll' : 104,
        'city' : 'Athmandu'
    }
    json_data = json.dumps(data)
    r = requests.post(url= URL, data = json_data)
    data = r.json()
    print(data)

def update_data():
    data = {
        'id' : 4,
        'name': 'blank',
        'roll' : 108,
        'city' : 'kavre'
    }
    json_data = json.dumps(data)
    r = requests.put(url= URL, data = json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {'id':6}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, data = json_data)
    data = r.json()
    print(data)

print("1: READ \n2: CREATE \n3: UPDATE \n4: DELETE")
a = int(input('Pick one: '))
if a==1:
    z = int(input('id pls (0 for all):'))
    if z==0:
        get_data()
    else:    
        get_data(z)
elif a==2:
    create_data()
elif a==3:
    update_data()
else:
    delete_data()