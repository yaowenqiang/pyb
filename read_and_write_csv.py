import csv

with open('list.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	# print(csv_reader)

	# next(csv_reader)

	with open('new_name.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t')

		for line in csv_reader:
			csv_writer.writerow(line)


with open('new_name.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	for line in csv_reader:
		print(line)

with open('new_name.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter='\t')
	# for line in csv_reader:
	# 	print(line)
	field_names = ['first_name', 'last_name', 'email']
	with open('new_name2.csv', 'w') as new_file:
		csv_writer = csv.DictWriter(new_file, fieldnames = field_names ,delimiter='\t')
		csv_writer.writeheader()

		# for line in csv_reader:
		# 	csv_writer.writerow(line)
		for line in csv_reader:
			csv_writer.writerow(line)
