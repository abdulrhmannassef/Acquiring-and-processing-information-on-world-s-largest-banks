import pandas as pd
import numpy as np
import glob
import os
import xml.etree.ElementTree as ET 
from datetime import datetime 
import requests
from bs4 import BeautifulSoup
import sqlite3
from bank_project_utils import extract , transform , load_to_csv , load_to_db , log_progress , run_query


url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
names = ["Name" , "MC_USD_Billion"]
exchange_file = "exchange_rate.csv"
target = "Largest_banks_data.csv"
log_file = "code_log.txt"

log_progress("Preliminaries complete. Initiating ETL process")



extracted_data = extract(url , names)
log_progress("Data extraction complete. Initiating Transformation process")



transformed_data = transform(extracted_data , exchange_file)
log_progress("Data transformation complete. Initiating Loading process")



load_to_csv(transformed_data,target)
log_progress("Data saved to CSV file")


sql_connection = sqlite3.connect("Banks.db")
Table_name = "Largest_banks"
log_progress("SQL Connection initiated")


load_to_db(transformed_data ,sql_connection, Table_name)
log_progress("Data loaded to Database as a table, Executing queries")


query_statement = f"select * from {Table_name}"
run_query(query_statement, sql_connection)
log_progress("Process Complete")


sql_connection.close()
log_progress("Server Connection closed")





