courses = ['history', 'math', 'physic', 'compsci']
courses_2 = ['art', 'education']
courses_3 = [3,4,6,5,4,3,3,6,7]

print(len(courses))
print(courses)
print(courses[0])
print(courses[-1])
print(courses[-0])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('art')
print(courses)

courses.insert(0,'art')
# courses.insert(0,courses_2)
# courses.append(courses_2)

courses.extend(courses_2)
print(courses)

popped = courses.remove('art')

courses.pop()
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses_3.sort(reverse = True)
print(courses_3)


print(courses)
new_course = sorted(courses, reverse = True)
print(courses)
print(new_course)





print(max(courses_3))
print(min(courses_3))
print(sum(courses_3))
print(courses.index('compsci'))
print('art' in courses)




for i in courses:
	print(i)


for index, course in enumerate(courses, start=1):
	print(index, course)


course_str = ', '.join(courses)

print(course_str)


new_list = course_str.split(', ')

print(new_list)
