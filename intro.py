message = """
hello
world
"""

print(len(message))
print(message.count('h'))
print(message.find('world'))

new_message = message.replace('world', 'universe')
print(new_message)

greeting = 'hello'

name = 'jack'
msg = greeting + ', ' + name

msg2 = '{}, {}, welcome!'.format(greeting, name)
# print(msg)
print(msg2)
msg3 = f'{greeting}, {name.upper()}, welcome!'
print(msg3)
print(dir(msg3))
print(help(str))
print(help(str.lower))
