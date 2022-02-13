with open('test.txt', 'r') as f:

	print(f.name)
	print(f.mode)

	f_content = f.read()
	print(f.tell())
	print(f_content)

	f.seek(0)

	print(f.readlines())

	print(f.readline(), end='')

	for lines in f:
		print(line)


	print(f.read(100))






print(f.closed)




def read_large_file(file_path):
	"""read large files line by line"""
	f = open(file_path,'r')
	bytes_to_read = 100

	f_contents = f.read(bytes_to_read)

	while len(f_contents) > 0:
		print(f_content, end='')
		f_contents = f.read(bytes_to_read)


def write_file(file_path):
	"""write to file"""
	with open(file_path,'w') as f:
		f.write('hello')
		f.write('hello')
		f.write('hello')
		f.seek(0)
		f.write('hello')




def copy_text_file(file_to_read, file_to_write):
		"""copy text file"""
		with open(file_to_read,'r') as rf:
			with open(file_to_write,'w') as wf:
				for line in rf:
					wf.write(line)


def copy_finary_file(file_to_read, file_to_write):
		"""copy binary file"""
		with open(file_to_read,'r') as rf:
			with open(file_to_write,'wb') as wf:
				for line in rf:
					wf.write(line)
