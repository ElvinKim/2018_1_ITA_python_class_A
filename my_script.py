# import my_statistics
#
# print(my_statistics.add(10, 20))

# def func_a():
#     print('a')
#
# func_a()
#
# from my_statistics import *
# add(10, 20)
# func_a()

# import sys
# import random
# sys.exit()
# print('비트코인!!!')
# print(sys.path)
# print(random.random())
# print(random.randint(1, 10))

import my_module
import sys

print(my_module.add(1, 2))


del sys.modules["my_module"]

for name in sys.modules.keys():
    print(name)

print(my_module.add(1, 2))





