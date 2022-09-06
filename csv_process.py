import pandas as pd
import time
import glob

date = timestr = time.strftime("%Y%m%d-%H%M%S")
print(date)
newdf=[]
# def read_files():
all_files = glob.glob("CSV/csv_processing/user_*.csv")
for i in all_files:
    print(i)
    read_df=pd.read_csv(i)
    newdf.append(read_df)
    # print(newdf)
    print(i,' This File read by user')
    cleandata=pd.concat(newdf,axis=0,ignore_index=True)
    print(cleandata,"Concat uncleaned data  ............")


    cleandata['full_name'] = cleandata[['firstname', 'lastname']].apply(lambda x: ' '.join(x), axis=1)
    cleandata['firstname'] = cleandata['full_name']
    cleandata.drop(['full_name','lastname'],axis=1,inplace=True)
    cleandata.rename(columns = {'firstname':'name'}, inplace = True)

    cleandata['phonenumber']=cleandata["phonenumber"].str.replace("x","")
  
    cols = cleandata.select_dtypes(object).columns
    cleandata[cols] = cleandata[cols].apply(lambda x: x.str.lower())
    
# def processed_files():
    cleandata.to_csv("CSV/csv_processed/"f"user_{date}.csv")
    cleandata.to_csv("Master/"f"csv_{date}.csv",index=False)

    print(cleandata, "--------> This is cleaned data ")
