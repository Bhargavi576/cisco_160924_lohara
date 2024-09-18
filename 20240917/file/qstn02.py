names_list=input('enter student names(seperated by spaces):').split()
names_set=set(names_list)
names_fset=frozenset(names_set)
names_dict={name:len(name) for name in names_fset}
print(f'original list: {names_list}')
print(f'set (no duplicates): {names_set}')
print(f'frozen set: {names_fset}')
print(f'dictionary of name lengths: {names_dict}')
import json
with open('qn02_data.json','w') as names_db:
    json.dump(names_dict,names_db)
print('dictionary written to JSON file')
with open('qn02_data.json','r') as names_db:
    name_dict2=json.load(names_db)
    print(f'reading from JSON file.....\n{name_dict2}')

