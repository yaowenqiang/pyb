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

