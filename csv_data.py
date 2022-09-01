import csv
from faker import Faker
from faker.providers import BaseProvider
import random

faker = Faker()
# class provider(BaseProvider):
#     status = ['Active', 'Inactive','ACTIVE','INACTIVE']

# def status(self):
#         """Return a random client_product."""        

#         return random.choice(self.status)


def data_generate(headers):
    with open("csv_processing/user_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(10):
            writer.writerow({
                    "Prefix" : faker.prefix(),
                    "Name": faker.name(),
                    "Phone Number" : faker.phone_number(),
                    "Email Id": faker.email(),
                    "Zip Code" : faker.zipcode(),
                    "City" : faker.city(),
                    "State" : faker.state(),
                    "Country" : faker.country(),
                    # 'Status':faker.status()
                    })
    
if __name__ == '__main__':
    headers = ["Prefix", "Name","Phone Number", "Email Id","City","State","Zip Code", "Country","status"]
    data_generate(headers)
    print("CSV generation completed!")