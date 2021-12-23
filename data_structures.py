from collections import deque
# Data structures
# ---------------------------- LISTS ------------------- #
lists = [1, 2, 3, 4, 5, 6, 7, 8]

# append
lists.append('biscoito')
# insert given a position
lists = [1, 2, 3, 4, 5, 6, 7, 8]
lists.insert(len(lists), 'mais biscoito')
# remove passing value
lists.remove('mais biscoito')
# pop remove the item given a position
lists.pop(2)  # removes 3
print(list)

# removes all items
new_list = lists[:]
new_list.clear()
print(new_list)

# return the number of times x appears in the list
lists = lists+[3, 3, 3, 3, 3, 3]
count = lists.count(3)
print(count)

# sort lists
# lists.sort()
# ---------------------------- QUEUES ------------------- #
queue = deque(['Daniel', 'Ingrid', 'Lulu'])
queue.append('Meg')
queue.popleft()  # The first to arrive now leaves
print(queue)

# ---------------------------- TUPLES ------------------- #
# tuple object does not support item assignment
t = 12345, 54321, 'hello!'

# ---------------------------- SETS ------------------- #
# A set is an unordered collection with no duplicate elements
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# ---------------------------- DICTIONARIES ------------------- #
# Are sometimes found in other languages as “associative memories” or “associative arrays”.
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

# dict comprehensions
print({x: x**2 for x in (2, 4, 6)})

# ---------------------------- LOOPING TECHNIQUES ------------------- #
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# ITEMS
for k, v in knights.items():
    print(k, v)

# The position index and corresponding value can be retrieved at the same time using
# enumerate() function
tictactoe_list = ['tick', 'tack', 'toe']
for i, v in enumerate(tictactoe_list):
    print(i, v)

# To loop over two or more sequences at the same time:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))

# reversed
for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
