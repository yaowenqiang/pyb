import json

people_string = '''
	{
		"people":[
			{
				"name": "John",
				"phone": "615",
				"emails": ["john@gmail.com", "john@hotmail.com"],
				"has_license": false
			},
			{
				"name": "Jane",
				"phone": "560",
				"emails": null,
				"has_license": true
			}

		] 
	}
'''

data = json.loads(people_string)
# print(data)

for person in data['people']:
	# print(person)
	del person['emails']

new_string = json.dumps(data, indent=4, sort_keys=True)
print(new_string)


# with open('data.json') as f:
# 	data = json.load(f)

# with open('data2.json','w') as f:
# 	json.dump(data, f, indent=4)


# https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json