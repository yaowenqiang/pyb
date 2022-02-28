nums = list(range(0, 10))
my_list = [n for n in nums]

my_list2 = [n*n for n in nums]

my_list3 = map(lambda n: n*n, nums)

my_list4 = [n for n in nums if n%2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

my_list5 = filter(lambda n: n%2 == 0, nums)


my_list_6 = []

for letter in 'abcd':
	for num in range(4):
		my_list_6.append((letter, num))

print(my_list_6)

my_list_7 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list_7)


indexes = ['a', 'b','c']
values = [1,2,3]

print(list(zip(indexes, values)))

my_dict = {}

for index, value in zip(indexes, values):
	my_dict[index] = value

print(my_dict)


my_dict_2 = {index: value for index, value in zip(indexes, values) if index != 'a'}

print(my_dict_2)

nums_2 = [1,3,5,6,7,7,8,8,8,6,6,5]

my_set = set()
for i in nums_2:
	my_set.add(i)

my_set_2 = {n for n in nums_2}

print(my_set)

print(my_set_2)



# generator

my_g_nums = list(range(0, 10))

def gen_func(nums):
	for n in nums:
		yield n*n

my_gen = gen_func(my_g_nums)

my_gen_2 = (n*n for n in my_g_nums)

for i in my_gen:
	print(i)


for i in my_gen_2:
	print(i)
