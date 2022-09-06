import pandas as pd
import time
import glob
newdf=[]
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)



newdf=[]
# def read_files():
all_files = glob.glob("EXCEL/excel_processing/user_*.xlsx")
for i in all_files:
    print(i)
    read_df=pd.read_excel(i)
    newdf.append(read_df)
    # print(newdf)
    print(i,' This File read by user')
    df=pd.concat(newdf,axis=0,ignore_index=True)
    print("concatenated uncleaned data  ............" ,df)

    df.rename(columns = {'name':'name'}, inplace = True)

    df['phonenumber']=df["phonenumber"].str.replace("x","")
    
    cols1 = df.select_dtypes(object).columns
    df[cols1] = df[cols1].apply(lambda x: x.str.lower())
    
# def processed_files():
    df.to_excel("EXCEL/excel_processed/"f"user_{date}.xlsx")
    df.to_csv("Master/"f"excel_{date}.csv",index=False)

    print(df, "--------> This is cleaned data ")