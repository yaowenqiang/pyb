import builtins

print(dir(builtins))

# def min():
# 	pass

x = 'global x'

def test(z):
	global x
	y = 'local y'
	x = 'local x'

	print(y)

	print(x)
	print(z)

test('local z')
# print(y)

m  = min([1,4,6,5,34])
print(m)


# eenclosing scope


def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		x = 'inner x'
		print(x)


	inner()
	print(x)


outer()
