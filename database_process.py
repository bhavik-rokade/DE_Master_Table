import pandas as pd
import time
date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)
import glob
newdf=[]
# def read_files():
all_files = glob.glob("DATABASE/processing/db_*.csv")
for i in all_files:
    print(i)
    read_df=pd.read_csv(i)
    newdf.append(read_df)
    # print(newdf)
    print(i,' This File read by user')
    df=pd.concat(newdf,axis=0,ignore_index=True)

    df.rename(columns = {'firstname':'name'}, inplace = True)

    df['phonenumber']=df["phonenumber"].str.replace("x","")
   
    cols = df.select_dtypes(object).columns
    df[cols] = df[cols].apply(lambda x: x.str.lower())
    
# def processed_files():
    df.to_csv("DATABASE/processed/"f"db_{date}.csv",index=False)
    df.to_csv("Master/"f"database_{date}.csv",index=False)

    print(df, "--------> This is cleaned data ")
