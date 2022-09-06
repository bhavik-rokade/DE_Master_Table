import json
import pandas as pd
import time
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)
import glob
newdf=[]
# def read_files():
all_files = glob.glob("API/api_processing/api**.json")
for i in all_files:
    f=open(i)
    print(f)
    data1=json.load(f)
    # print(data1)
    print(type(data1))
    df = pd.DataFrame(data1, columns =["prefix", "name","phonenumber", "emailid","city","state","zipcode", "country","status"], dtype = float) 
    df['phonenumber']=df["phonenumber"].str.replace("x","")
    df['zipcode'] = df['zipcode'].astype(int)
    df['status'] = df['status'].astype(int)
    cols1 = df.select_dtypes(object).columns
    df[cols1] = df[cols1].apply(lambda x: x.str.lower())
    print(df)
    
def processed_files():
    df.to_csv("API/api_processed/"f"api_{date}.json",index=False)
    df.to_csv("Master/"f"api_{date}.csv",index=False)

if __name__=='__main__':
    processed_files()