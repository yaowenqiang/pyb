from contextlib import contextmanager

class Open_File():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file

	def __exit__(self, exc_ty0e, exc_val, traceback):
		self.file.close()


with Open_File('sample.txt', 'w') as f:
	f.write('Testing')


@contextmanager
def open_file(file, mode):
	f = open(file, mode)
	yield f
	f.close()


print(f.closed)

with Open_File('sample.txt', 'w')  as f:
	f.write('Testing with function')
print(f.closed)
	
