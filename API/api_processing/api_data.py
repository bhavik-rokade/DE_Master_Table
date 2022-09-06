from flask import Flask, jsonify, request
from faker import Faker
import json
import time
app = Flask(__name__)
faker=Faker()
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)
@app.route('/')
def generate_data():
	my_array = []
	for i in range(10):
		# print("ttttttttttttttttttttttttt",i)
		prefix=faker.prefix().upper()
		name=faker.name()
		phone_number=faker.phone_number()
		email=faker.email()
		city=faker.city()
		state=faker.state()
		zipcode=faker.zipcode()
		country=faker.country()
		status=faker.pybool()
		# status=faker.random_choices(elements=['TRUE', 'True', 'FALSE', 'false'],length=1)
		data=(prefix,name,phone_number,email,city,state,zipcode,country,status)
		my_array.append(data)
		
		# print(data)
		# you are printing data here so it will print on every iteration
		# but data is reassign to any one value in each iteration

		with open("API/api_processing/"f"api_{date}.json", 'w') as jsonfile:
			json.dump(my_array, jsonfile, indent=2)
			# print("JSON generation completed")

	return jsonify({'data': my_array})

# import pandas as pd

# print('I am innnnnnnnnnnn')
# df = pd.read_json("API/api_processing/api_{date}.json")
# print(df.head())

if __name__ == '__main__':
	app.run(debug=True)





# import requests
# import json
# from faker import Faker
# faker=Faker()

# url = 'http://127.0.0.1:8000/users/'

# ## API Call to retrieve User
# result = requests.get(url)
# print(result)
# ## API Results
# data = result.text
# print(data)
# with open('api_processing/user_data.json', 'w') as f:
#     json.dump(data, f, indent=2)
#     print("JSON generation completed")


## Write API Results to CSV
# with open('api_processing/api_data.csv', "wb") as csvFile:
#     writer = csv.writer(csvFile, delimiter=',')
#     # for line in data:
#     #     writer.writerow(line)