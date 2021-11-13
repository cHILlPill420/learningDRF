from inspect import EndOfBlock
import requests
import json

from requests.api import head

URL = "http://127.0.0.1:8000/studapi/"


def get_data(id=None):
    a = []
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'} #for @api view headers is required
    r = requests.get(url= URL, headers=headers, data= json_data)
    data = r.json()
    print (data)

def create_data():
    data = {
        'id' : 5,
        'name': 'blank',
        'roll' : 105,
        'city' : 'Bhaktapur'
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'} #for @api view headers is required
    r = requests.post(url= URL,headers= headers, data = json_data)
    data = r.json()
    print(data)

def update_data():
    data = {
        'id' : 9,
        'roll' : 106,
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'} #for @api view headers is required
    r = requests.put(url= URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {'id': 9}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'} #for @api view headers is required
    r = requests.delete(url= URL, headers= headers, data = json_data)
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