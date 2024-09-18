my_lst=input(('enter words')).split()
my_tuple=tuple(my_lst)
print(my_lst)
print(my_tuple)
with open('qstn01.txt','w') as data_file:
    data_file.write(f'list:{my_lst}\n')
    data_file.write(f'tuple:{my_tuple}')
print('data written to file')

with open('qstn01.txt','r') as data_file:
    line_list=data_file.readline()
    line_tuple=data_file.readline()
    print(line_list)
    print(line_tuple)















    