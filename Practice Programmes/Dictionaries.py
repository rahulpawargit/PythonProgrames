dict= {1:'rahul', 2:'sandeep', 3:'Ganesh'}
# for key, values in dict.items():
#     print(key, values)

sorted_dict = {key: value for key, value in sorted(dict.items(), key=lambda  item :item[1])}
print(sorted_dict)