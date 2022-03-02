import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYz
1234567890

Ha HaHa

123.456.789

'''

print('\tTAB')
print(r'\tTAB')

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)


for match in matches:
	print(match)


print(text_to_search[1:4])


pattern2 = re.compile('\.')

matches2 = pattern2.finditer(text_to_search)
for matches in matches2:
	print(matches)