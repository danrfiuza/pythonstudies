# Tutorial python

text = 'A quote that says: \"I love python\"'

# string spitting
print(text[0:1])

# lists, lists are immutable
squares = [1, 2, 3, 4, 5]
print(squares[0])

# shallow copy of the list
print(squares[:])

# list concatenation
print(squares+[6, 7, 8])

# list append
squares.append(9)

print(squares)

# nest lists
nested = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(nested)

# fibonacci example
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# printing and concatenating
i = 256 * 265
print('The value of i is:', i)

print(3**2)


# flow controls
x = int(input("Please enter an integer: "))

if x < 0:
    X = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# match ONLY AVAILABLE ON VERSION 3.10 OR NEWER
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# for statements
words = ['cat', 'dog', 'window']
for w in words:
    print(w, len(w))


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
