import collections
from collections import OrderedDict
import torch
# a = torch.rand(2,3)
# print(a)
# print(id(a))
# a += 1
# print(id(a))
# a = a + 1
# print(a)
# print(id(a))
# print('*'* 100)
# # print(id(a))
# # b = 1
# # print(id(b))
# # c = 1
# # print(id(c))
# a = 2.0
# b = 2.0
# print(id(a))
# print(id(b))

# print('*' * 100)
# d = 1
# print(id(d))
# print(id(1))
# print(id(257))
# print(id(257))
# print(id(1))
# a = OrderedDict()
# a['a'] = 1.
# a['b'] = 2.
# print(a)

# b = dict()
# b['a'] = 3.
# b['b'] = 4.
# print(b)
# a.update(b)
# print(a)
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# print(a is b)

# b += 1
# print(id(b))
# b = b + 1
# print(id(b))
# b = 2
# print(id(b))
# a = 1
# b = 1
# print(id(b))
# b += 1
# print(id(b))
# print(a)

# c = 12.5
# print(id(c))
# c += 1
# print(id(c))

# d = 12.5
# print(id(d))

# a = [1,2,3]
# print('a id:',id(a))

# a += [4]
# print(a)
# print('a id :',id(a))
# print('*' * 100)
# d = [1,2,3,4]
# print('d is:',id(d))
# print('[1,2,3,4] id :',id([1,2,3,4]))

# print('*' * 100)
# print('[1,2,3,4,5] id:', id([1,2,3,4,5]))
# b = [1,2,3,4,5]
# print('b id:', id(b))
# print('*' * 100)

# a = a + [5]
# print('a is:',a)
# print('a id:',id(a))
# print('[1,2,3,4,5] id:', id([1,2,3,4,5]))
# print('[1,2,3,4,5] id:', id([1,2,3,4,5]))
a =1
print(id(a))
a += 1
print(id(a))
a = a +1
print(id(a))