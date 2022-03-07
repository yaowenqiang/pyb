import memory_profiler as memory_profile
import random
import time

names = ['John','Corey','Adam','Steve','Rick','thomas']
majors = ['Math','Engineering','CompSci','Arts','Business']

print('Memory (before): {}Mb'.format(memory_profile.memory_usage()))

def people_list(num_people):
	result = []
	for i in range(num_people):
		person = {
			'id':i,
			'name':random.choice(names),
			'majors': random.choice(majors)
		}
		result.append(person)
	return result

def people_generator(num_people):
	for i in xrange(num_people):
			person = {
			'id':i,
			'name':random.choice(names),
			'majors': random.choice(majors)
		}

	yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()


print('Memory (Afger): {}Mb'.format(memory_profile.memory_usage()))

print('toke {} seconds'.format(t2-t1))
