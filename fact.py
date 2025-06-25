a= [1,2,3,[2,[5,6,[7,8]]]]
def flatten(n):
    final_list = []
    for i in n:
        if type(i) == list:
            final_list.extend(flatten(i))
        else:
            final_list.append(i)
    return final_list
print(flatten(a))