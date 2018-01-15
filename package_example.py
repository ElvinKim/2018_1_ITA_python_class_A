import root_package.sub_package1.module1
import root_package.sub_package2.module3

root_package.sub_package2.module3.print_module3()
root_package.sub_package1.module1.print_module1()

from root_package.sub_package1.module1 import print_module1
print_module1()

from root_package.sub_package2 import *

module3.print_module3()

import random
lotto_lst = []
while len(lotto_lst) < 6:
    random_num = random.randint(1, 45)
    if random_num not in lotto_lst:
        lotto_lst.append(random_num)
print(lotto_lst)


import random
lotto_lst = []
while len(set(lotto_lst)) < 6:
    lotto_lst.append(random.randint(1, 45))
print(list(set(lotto_lst)))










