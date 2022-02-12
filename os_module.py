import os
from datetime import datetime

# print(dir(os))

# print(os.getcwd())

# os.chdir('/root/')
# print(os.getcwd())

# print(os.listdir())



# os.mkdir('demo/sub/')
# os.makedirs('demo/sub/')

# os.makedirs('')

# os.rmdir('demo')
# os.removedirs('demo/sub')

# os.rename('demo.txt', 'demo2.txt')

# print(os.stat('demo'))
md_time = os.stat('demo').st_mtime

print(datetime.fromtimestamp(md_time))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
# 	print('current Path:', dirpath)
# 	print('Directories:', dirnames)
# 	print('current Path:', filenames)




print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)


# with open(file_path, 'w') as f:
# 	f.write('')



print(os.path.basename('.'))
print(os.path.dirname('.'))
print(os.path.split('/tmp/text.txt'))


print(os.path.exists('/tmp/tmp.txt'))




print(os.path.isdir('/mtp/abc'))


print(os.path.splitext('/mtp/conf.d/abc.txt.exe'))


