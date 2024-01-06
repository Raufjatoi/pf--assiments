empty_list = []
lst = [1,2,3,4,5,5,6]
for i in lst:
    if i not in empty_list:
        empty_list.append(i)
lst.clear()
print(empty_list)