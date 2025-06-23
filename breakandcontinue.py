a = [1,2,3,4,5,6]
# break loop tei banda huncha
# continue 
for i in a:
    if i == 3:
        break # yei break huncha ra yo vanda
    # tala chai jana paudaina.
    print(i)

print('....................')

for i in a:
    if i == 3:
        continue
    # yo vanda tala chai jadaina 
    # feri mathi loop ma nai jancha.
    print(i)

b = [1,2,3,"test",4.0,2.8,"testing world"]
new_list=[]
for i in b:
    if type(i) != str: 
        new_list.append(i)
print(new_list)
# isinstance(value,int float str)
# type compare garya matra ho 

# data = [1,2,2,2,None,None,5,5,None,"data"]
# new_data=[]
# for i in data:
#     if isinstance(i,None):
#         print(True)
#         continue
#     new_data.append(i)
# print(new_data)

# nested for loop
data1=[10,50,3,5,6,7,8]
def multiplication(data):
    for i in data:
        for j in range(1,11):
            print(f'{i} * {j} = {i*j}')
        print('----------------------')
data = [10,50,3,5,6,7,8,50,13,65,8,10]
new_data = set(data)
multiplication(data1)
multiplication(new_data)

# is and is not operator is used to 
# handle the None.
new_even=[]
for i in range(50,100):
    if i % 2 == 0:
        new_even.append(i)
print(new_even)
