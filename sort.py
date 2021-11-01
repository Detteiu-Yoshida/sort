import random

start = input('Please input list')
sort_list = str(start).split(',')
loop = input('Please input number to sort')
loop_int = int(loop)
for i in range(0,loop_int):
    a = random.randint(0,len(sort_list)-1)
    print(sort_list[a])
