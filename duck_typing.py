class Duck:
	def quack(self):
		print('Quack, quack')

	def fly(self):
		print('Flap, Flap')


class Person:
	def quack(self):
		print("I'm Quacking like a Duck!")

	def fly(self):
		print("I'm flapping my arms!")


def quack_and_fly(thing):
	# if isinstance(thing, Duck):
	# 	thing.quack();
	# 	thing.fly()
	# else:
	# 	print('This has to b a Duck!')

	# print()

	if hasattr(thing, 'quack'):
		if callable(thing.quack):
			thing.quack()

	if hasattr(thing, 'fly'):
		if callable(thing.fly):
			thing.fly()



d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)




person = {
	'name': 'jack',
	'age': 20,
	'job':'programmer'
}



if 'name' in person and 'age' in person and 'job' in person:
	print("I'm {name}, I'm {age}, years old and I am a {job}'".format(**person))
else:
	person('Missing some keys')


try:
	print("I'm {name}, I'm {age}, years old and I am a {job}'".format(**person))
except KeyError as e:
	print('missing {} key'.formate)



my_list = [1,2,3,4,5]

if len(my_list) > 5:
	print(my_list[5])
else:
	print('That index does not exist')


try:
	print(my_list[5])
except IndexError as e:
	print(e)




