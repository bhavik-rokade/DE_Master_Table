import os
import psycopg2
from faker import Faker
import csv 
import time
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)


faker=Faker()
class PsqlConnection:
	def __init__(self):
		self.conn = psycopg2.connect(
			host="localhost",
			database="ETL",
			user='admin1',
			password='admin@123'
			# user= os.environ.get("DB_USERNAME"),
			# password =os.environ.get("DB_PASSWORD")
		)
		self.cursor=self.conn.cursor()

	def generate_data(self):
		for i in range(10):
			prefix=faker.prefix().upper()
			name=faker.name()
			phone_number=faker.phone_number()
			email=faker.email()
			city=faker.city()
			state=faker.state()
			zipcode=faker.zipcode()
			country=faker.country()
			status=faker.random_choices(elements=('TRUE', 'True', 'FALSE', 'false'),length=1)


			print(prefix,name,phone_number,email,city,state,zipcode,country,status)
			data=(prefix,name,phone_number,email,city,state,zipcode,country,status)
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS database_data 
				(Prefix VARCHAR(200), Name VARCHAR(200), Phone_Number VARCHAR(200), Email_Id VARCHAR(200), City VARCHAR(200),State VARCHAR(200),Zip_Code VARCHAR(200),Country VARCHAR(200),Status VARCHAR(200)) """)
			# print(111111111111)
			self.cursor.execute("INSERT INTO database_data(Prefix, Name, Phone_Number, Email_Id, City,State,Zip_Code, Country,Status) values (%s, %s, %s, %s, %s, %s,%s,%s,%s) ",data)
		
	
	def fetch_data(self,headers): 
		select_Query = "select * from database_data"
		self.cursor.execute(select_Query)
		records = self.cursor.fetchall()
		# print(records)
		with open("DATABASE/processing/"f"db_{date}"+".csv", 'wt') as csvFile:
			writer = csv.writer(csvFile)
			# writer.writeheader()
			writer.writerow(headers)
			for i in records:
				writer.writerow(i)	
			self.conn.commit()
		self.conn.close()



if __name__=="__main__":
	headers = ["prefix", "name","phonenumber", "emailid","city","state","zipcode", "country","status"]

	ps=PsqlConnection()
	ps.generate_data()
	ps.fetch_data(headers)

	

