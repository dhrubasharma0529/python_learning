def test (*data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum
test(1,2,2,5,1,1,12,1,1)

def test2 (**data):
    for key,value in data.items():
        print(value)
test2(name="hello",age=19,role="developer",address="kathmandu")

def test3(*args,**kwargs):
    print(args)
    print(kwargs)
test3(1,2,2,3,4,name="Ram", classes=9)
# 