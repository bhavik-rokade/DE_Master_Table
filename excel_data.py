import xlsxwriter
from faker import Faker

faker = Faker()

def data_generate():
    workbook = xlsxwriter.Workbook("excel_processing/user_data.xlsx")
    sheet_data = workbook.add_worksheet('user_sheet1')
    sheet_data.write("A1","Prefix")
    sheet_data.write("B1","Name")
    sheet_data.write("C1",'Phone Number')
    sheet_data.write("D1","Email ID")
    sheet_data.write("E1","Zip Code") 
    sheet_data.write("F1","City") 
    sheet_data.write("G1","State") 
    sheet_data.write("H1","Country") 

    rowindex=2

             
    for i in range(10):
        prefix=faker.prefix()
        name=faker.name()
        phone_number=faker.phone_number()
        email=faker.email()
        zipcode=faker.zipcode()
        city=faker.city()
        state=faker.state()
        country=faker.country()

        print(name,email)
        sheet_data.write("A"+str(rowindex),prefix)
        sheet_data.write("B"+str(rowindex),name)
        sheet_data.write("C"+str(rowindex),phone_number)
        sheet_data.write("D"+str(rowindex),email)
        sheet_data.write("E"+str(rowindex),zipcode)
        sheet_data.write("F"+str(rowindex),city)
        sheet_data.write("G"+str(rowindex),state)
        sheet_data.write("H"+str(rowindex),country) 

        rowindex +=1

    workbook.close()
if __name__ == '__main__':
    data_generate()
    print("excel generation completed!")
