
import os
import psycopg2
from faker import Faker
import psycopg2.extras as extras
import glob
import pandas as pd

files = glob.glob(("Master/excel_*.csv"))
files.extend(glob.glob(("Master/csv_*.csv")))
files.extend(glob.glob(("Master/database_*.csv")))
files.extend(glob.glob(("Master/api_*.csv")))


li = []
for file in files:
    df=pd.read_csv(file,index_col=None, header=0)
    li.append(df)
df=pd.concat(li,axis=0,ignore_index=True)
print(df)


def insert_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))

    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()
  
  
conn = psycopg2.connect(
    database="ETL", user='admin1', password='admin@123', host='127.0.0.1', port='5432'
)
    
insert_values(conn, df, 'master_table')
print("sucesss .............")


import shutil
import os

origin = 'Master/'
target = 'Movedfiles/'

files1 = os.listdir(origin)

for f in files1:
   shutil.move(origin + f, target)
