import json

data ='''
{
    "name" : "Satya",
    "phone" : {
        "type" : "home",
        "number" : "+12345678"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

infor = json.loads(data)
print('Name:', infor["name"])
print('Hide:', infor["email"]["hide"])