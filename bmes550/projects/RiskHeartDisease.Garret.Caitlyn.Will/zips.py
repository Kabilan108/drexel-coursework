# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:32:50 2022

@author: CocosW
"""
import sqlite3
import pandas as pd
from pathlib import Path; 
import sys, os; 
from tempfile import TemporaryDirectory
from urllib.request import urlopen
import shutil
import requests

def zips():
    
    #url = 'https://www.unitedstateszipcodes.org/'
    #weburl = urlopen(url, timeout=10);
    #webdata = weburl.read();
    #print(webdata)
    
    #Create new database and establish cursor
    datadir = str(Path.home())+'/Data/';
    conn = sqlite3.connect(datadir+'us_hospital_locations.sqlite');
    cur = conn.cursor();
    
    #Drop table if it already exists
    conn.execute("DROP TABLE IF EXISTS zips");
    
    #Create zips table in the database
    conn.execute("""CREATE TABLE   IF NOT EXISTS   zips (
    ID_PRIME INTEGER PRIMARY KEY,
    zip VARCHAR(30), 
    type VARCHAR(30),
    decommissioned VARCHAR(30),
    primary_city VARCHAR(30),
    acceptable_cities VARCHAR(30), 
    unacceptable_cities VARCHAR(30),
    state VARCHAR(30),
    county VARCHAR(30),
    timezone VARCHAR(30),
    area_codes VARCHAR(30),
    world_region VARCHAR(30),
    country VARCHAR(30),
    latitude FLOAT,
    longitude FLOAT,
    irs_estimated_population FLOAT);
    """);
    
    #Read the csv file with all zip codes and according lat/long into a DataFrame
    df = pd.read_csv("zip_code_database.csv");
    
    #Convert the DataFrame into a table and append to the zips table
    df.to_sql('zips', conn, if_exists='append', index=False);
    
    #Commit the changes to the database and close the database connection
    conn.commit();
    conn.close();
    
if __name__ == "__main__":
    #variable = sys.argv[1]
    zips()