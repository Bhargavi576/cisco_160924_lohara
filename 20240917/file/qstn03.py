my_list=input('enter integers').split()
int_list=(int(i) for i in my_list)
my_tuple=tuple(my_list)
my_set=set(my_list)
my_fset=frozenset(my_set)
my_dict={key:key*2 for key in int_list}
print(my_dict)