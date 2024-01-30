import pandas as pd
import numpy as np
import glob
import os
import xml.etree.ElementTree as ET 
from datetime import datetime 
import requests
from bs4 import BeautifulSoup
import sqlite3

log_file = "code_log.txt"

def extract(url , names):
    
    data_frame =pd.DataFrame( columns = names)


    response = requests.get(url).text
    soup = BeautifulSoup(response , "html.parser")
    table = soup.find_all("table" , {"class":"wikitable sortable mw-collapsible"})
    rows = table[0].find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        if len(cols)!=0:
            dict_ = {
                
                "Name" : cols[2].text.strip(),
                "MC_USD_Billion" : cols[2].text.strip()
            }
            
            
            df = pd.DataFrame(dict_ , index = [0])

            data_frame = pd.concat([data_frame , df] , ignore_index=True)
    return(data_frame)

def transform(df , exchange_file):
    '''
    MC_GBP_Billion, GBP
    MC_EUR_Billion, EUR
    MC_INR_Billion, INR
    '''
    df_rate = pd.read_csv(exchange_file, index_col=[0])

    MC_USD_Billion_list = df["MC_USD_Billion"].tolist()
    MC_USD_Billion_list = [float(x) for x in MC_USD_Billion_list]
    df["MC_GBP_Billion"] = np.array(MC_USD_Billion_list)*df_rate.loc['GBP',:]["Rate"]
    df["MC_EUR_Billion"] = np.array(MC_USD_Billion_list)*df_rate.loc['EUR',:]["Rate"]
    df["MC_INR_Billion"] = np.array(MC_USD_Billion_list)*df_rate.loc['INR',:]["Rate"]
    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
  
    df.to_sql(table_name, sql_connection , if_exists = "replace" , index = False)
    


def run_query(query_statement, sql_connection):
    data = pd.read_sql(query_statement  ,sql_connection)
    
    return(data)
   
    

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 
    
    
        