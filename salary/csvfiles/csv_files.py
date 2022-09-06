import csv
from faker import Faker
from faker.providers import BaseProvider
import random
import time

faker = Faker()
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)

def data_generate(headers):
    with open("salary/csvfiles/"f"user_salary_{date}"+".csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(10):
            writer.writerow({
                    "prefix" : faker.prefix(),
                    "firstname": faker.first_name(),
                    "lastname": faker.last_name(),
                    "phonenumber" : faker.phone_number(),
                    "emailid": faker.email(),
                    "city" : faker.city(),
                    "state" : faker.state(),
                    "zipcode" : faker.zipcode(),
                    "country" : faker.country(),
                    "status": faker.pybool()
                    
                    })
    
if __name__ == '__main__':
    headers = ["prefix", "firstname","lastname","phonenumber", "emailid","city","state","zipcode", "country","status"]
    for i in range(10):
        data_generate(headers)
        print(i)
        time.sleep(10)
        print("CSV generation completed")