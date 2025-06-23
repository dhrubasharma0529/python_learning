# for i in range(11):
#     print(f'2 * {i} ={2*i}')
people = [
    {
        "name":"sudan",
        "dob":"06-11"
    },
    {
        "name":"Madan",
        "dob":"01-06",
    },
    {
        "name":"suman",
        "dob":"01-06"
    },
    {
        "name":"sandeep",
        "dob":"01-07"
    }
]
current_date = "01-06"
for i in people:
    if i['dob'] == current_date:
        print("happy birthday",i['name'])
for i in range(10,1,-1):
    print(i)
    
