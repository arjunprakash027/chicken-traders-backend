from crud import *

#insert_value('broiler', '2023-04-08', 20, 'sale', 'less quantity')
print(get_all_values())
print(get_value('broiler'))
#update_value('broiler', '2023-04-10', 20, 'purchase', 'less quantity')
#delete_value('Item1')

for i in get_value('broiler'):
    print(i)

#docker test changes