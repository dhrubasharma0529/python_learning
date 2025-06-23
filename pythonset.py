def adding_elements(A):
    print(A)
    b = []
    for i in range (A):
        b.append((int(input())))
    b= set(b)
    return b
  
a = adding_elements(A=int(input()))
N = int(input())
def print_function(name,length):
    print(f"{name}{' '}{length}")
print_function(name='intersection_update', length = 10)
c=adding_elements(10)
f=a.intersection_update(c)
print(f)
print_function(name='update', length = 2)
d=adding_elements(A=int(input()))
print(d)
g=f.update(d)
print_function(name='symmetric_difference_update', length = 5)
e=adding_elements(A=int(input()))
h=g.symmetric_difference_update(e)
print_function(name ='difference_update', length = 7)
f=adding_elements(A=int(input()))
i=h.difference_update(f)