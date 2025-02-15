#!/usr/bin/python3


a = "abc"
b = 12
c = {"first": [1, 2, 3], "second": [4, 5, 6]}
d = ['a', 'b', 'c']

print(type(a))  # str
print(type(b))  # int
print(type(c))  # dict
print(type(d))  # list

lst = [1, 2, 3, 4, 5]
it = iter(lst)  # Create an iterator object

while True:
    try:
        print(next(it))  # Get next element
    except StopIteration:  
        break  # Stop when iterator is exhausted

l = []
it = iter(l)

while len(l) < 20:
    l.append(1)
    print(next(it))  # ❌ This will raise StopIteration

l = []
while len(l) < 20:
    l.append(1)
    print(l[-1])  # ✅ Safely access the last added element

is_even = lambda x: x % 2 == 0
l = filter(is_even, range(3))

print(type(l))  # filter object

for x in l:
    print(x)  # 0, 2

filtered_values = list(filter(lambda x: x % 2 == 0, range(3)))
print(filtered_values)  # [0, 2]

values = [1, 2, 3]
triple = lambda x: x * 3
triple_values = list(map(triple, values))

print(triple_values)  # [3, 6, 9]

triple_values = [x * 3 for x in values]
print(triple_values)  # [3, 6, 9]
