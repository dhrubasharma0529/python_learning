# dictionary key and value 
user_info = {
    "name": "Dhruba Sharma",
    "age" : 21,
    "test" : [1,2,3,4,5]
}
print(type(user_info))

# accessing the data in dict.
# on the basis of key.
print(user_info['name'])
print(user_info['age'])
print(user_info['test'][0])
user_info['age'] = 27
user_info ['city'] = 'Pokhara'
print(user_info)

user_info2 = {
    "role":"developer",
    "address":"dang",
    "age":25
}
user_info.update(user_info2)
print(user_info)
print(len(user_info))
print(user_info.get('ball')) # searching the key.

# remove method from the dictionary
test ={
    "name":"hello",
    "greet":"hi",
    "age" : 27
}
# del test['name']
test.pop("name")
print(test)
test.popitem()
print(test)

user = {
    "name": "sudan",
    "phone": [{
        "type": "Ntc",
        "number": 98449
    },
    {
        "type" : "Ncell",
        "number" : 98062
    }
    ]
}
z=user.get("phone")
print(z[0])
print(f"{z[0]['type']} is {z[0]['number']}")
print(f"phone number is {z[1]['type']}")

user_info3 = {
    "name":"Sudan",
    "details":{
        "address" : 'dang',
        "age" : 27
    }
}