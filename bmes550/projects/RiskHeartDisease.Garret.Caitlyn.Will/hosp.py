# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:43:11 2022

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

def mkdirif(dir):
	if not os.path.isdir(dir): os.mkdir(dir, 0o777 )

def hosp():
    
    # Establish a dedicated data directory
    datadir = str(Path.home())+'/Data/';
    mkdirif(datadir);
        
    #Create new database in dedicated data folder and establish cursor
    conn = sqlite3.connect(datadir+'us_hospital_locations.sqlite');
    cur = conn.cursor();
    
    #Drop table if it already exists
    conn.execute("DROP TABLE IF EXISTS hospitals");
    
    #Create hospitals table in the database
    conn.execute("""CREATE TABLE   IF NOT EXISTS   hospitals (
    ID_PRIME INTEGER PRIMARY KEY,
    X FLOAT, 
    Y FLOAT,
    FID FLOAT,
    ID FLOAT,
    NAME VARCHAR(30), 
    ADDRESS VARCHAR(30),
    CITY VARCHAR(30),
    STATE VARCHAR(30),
    ZIP VARCHAR(30),
    ZIP4 VARCHAR(30),
    TELEPHONE VARCHAR(30),
    TYPE VARCHAR(30),
    STATUS VARCHAR(30),
    POPULATION VARCHAR(30),
    COUNTY VARCHAR(30),
    COUNTYFIPS VARCHAR(30),
    COUNTRY VARCHAR(30),
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    NAICS_CODE VARCHAR(30),
    NAICS_DESC VARCHAR(30),
    SOURCE VARCHAR(30),
    SOURCEDATE VARCHAR(30),
    VAL_METHOD VARCHAR(30),
    VAL_DATE VARCHAR(30),
    WEBSITE VARCHAR(100),
    STATE_ID VARCHAR(30),
    ALT_NAME VARCHAR(30),
    ST_FIPS VARCHAR(30),
    OWNER VARCHAR(30),
    TTL_STAFF VARCHAR(30),
    BEDS VARCHAR(30),
    TRAUMA VARCHAR(30),
    HELIPAD VARCHAR(30));
    """);
    
    # This is the filepath for the Kaggle hospitals data set. The url may expire,
    # in which case you will need to revisit this website: https://www.kaggle.com/datasets/andrewmvd/us-hospital-locations?resource=download 
    # After clicking on the download button, you should be able to pull the download link and update below
    filepath = 'https://storage.googleapis.com/kaggle-data-sets/756770/1307192/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T153528Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8de5659a0b0d66d8cf292dfaba02c6dd5ae4a35008617e7c2fb16b4834c0aa5608a9fde76641de7224c910e4d5f76c14f0edf0bb3c3c3b7b67a99df199becb1afccdc8cb361576b5704c6b3695970a8dcc78efad238c73251b034dfb80bda79efbdbd969cf990e91fe31e63763e624f8e6c64a3607487783883046bdbaf7f8bd82733a6306c4c849163f8df8d79b223a3a80ef576ace2d23706d41ffa2c88f6ce38b56fd66d2fcdb865a4b3307ceade9eb9f377afb8b6133ac2319b45b4267bbb278cafbb232349aaebcd89a0a3531b807872fa5ced54b1817c6c2e1bea6318f659fc380f157c890a4e36820a9968180aabd0eb069298bca70cf9bcdee38b508';
        
    # Create a temporary directory. Open the filepath.
    with TemporaryDirectory() as tempdir:
        tempfile_path = os.path.join(tempdir,"archive.zip")
        with urlopen(filepath, timeout=10) as fsrc, open(
                tempfile_path, "wb"
        ) as tempfile:
            # copy the opened file to the temp directory
            shutil.copyfileobj(fsrc, tempfile)
            # unzip the zip file to the temp directory
            shutil.unpack_archive(tempfile_path, tempdir)
            
            tempfile_path2 = os.path.join(tempdir, "us_hospital_locations.csv")
            #Read the csv file with all hospital locations into a DataFrame
            df = pd.read_csv(tempfile_path2);
    
    #Convert the DataFrame into a table and append to the hospitals table
    df.to_sql('hospitals', conn, if_exists='append', index=False);
    
    #Commit the changes to the database and close the database connection
    conn.commit();
    conn.close();
    
if __name__ == "__main__":
    #variable = sys.argv[1]
    hosp()