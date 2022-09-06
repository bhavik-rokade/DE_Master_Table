import xlsxwriter
from faker import Faker
import time
faker = Faker()
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)
def data_generate():
    workbook = xlsxwriter.Workbook("EXCEL/excel_processing/"f"user_data_{date}"+".xlsx")
    sheet_data = workbook.add_worksheet('user_sheet1')
    
    sheet_data.write("A1","prefix")
    sheet_data.write("B1","name")
    sheet_data.write("C1",'phonenumber')
    sheet_data.write("D1","emailid")
    sheet_data.write("E1","city") 
    sheet_data.write("F1","state") 
    sheet_data.write("G1","zipcode") 
    sheet_data.write("H1","country") 
    sheet_data.write("I1","status") 

    rowindex=2

             
    for i in range(10):
        prefix=faker.prefix()
        name=faker.name()
        phonenumber=faker.phone_number()
        email=faker.email()
        city=faker.city().upper()
        state=faker.state()
        zipcode=faker.zipcode()
        country=faker.country()
        status= faker.pybool()


        print(name,email,status)
        sheet_data.write("A"+str(rowindex),prefix)
        sheet_data.write("B"+str(rowindex),name)
        sheet_data.write("C"+str(rowindex),phonenumber)
        sheet_data.write("D"+str(rowindex),email)
        sheet_data.write("E"+str(rowindex),city)
        sheet_data.write("F"+str(rowindex),state)
        sheet_data.write("G"+str(rowindex),zipcode)
        sheet_data.write("H"+str(rowindex),country)
        sheet_data.write("I"+str(rowindex),(status)) 
 

        rowindex +=1

    workbook.close()
if __name__ == '__main__':
    data_generate()
    print("excel generation completed!")
