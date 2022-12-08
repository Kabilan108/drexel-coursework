# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:00:02 2022

@author: CocosW
"""
#Need to install the geopy module 
#pip install geopy
from pathlib import Path; 
from hosp import *
from zips import *
import sqlite3
import pandas as pd
import geopy.distance
import sys

def close_hosp(zipcode):
    #zipcode = '63125'
    
    #Create the hospitals reference table within us_hospital_locations database
    #This program also creates the data directory
    hosp();
    
    #Create the zipcode to latitude and longitude reference table within us_hospital_locations database
    zips();
    
    #Establish a connection and cursor to the database   
    datadir = str(Path.home())+'/Data/';
    conn = sqlite3.connect(datadir + 'us_hospital_locations.sqlite');
    cur = conn.cursor();
    
    #Pull all zipcodes from the database and convert to a DataFrame
    cur.execute("SELECT zip FROM zips;");
    rows_allzips=cur.fetchall();
    dfz = pd.DataFrame(rows_allzips);
    dfz.columns = [x[0] for x in cur.description];
        
    #Set the DataFrames to print all rows and columns
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    
    if zipcode in dfz['zip'].values:
        
        #Fetch the latitude and longitude for the user's zipcode that they entered into the streamlit gui
        cur.execute(f"SELECT latitude, longitude FROM zips z \
        WHERE z.zip = '{zipcode}';");
        rows_zips=cur.fetchall();
        coords_user = (rows_zips[0][0], rows_zips[0][1])
        
        #Convert the hospitals table to a pandas DataFrame
        cur.execute("SELECT * FROM hospitals;");
        rows_hospitals=cur.fetchall();
        df = pd.DataFrame(rows_hospitals);
        df.columns = [x[0] for x in cur.description];
        
        #Add a new column to the hospitals DataFrame, which is the coordinate tuple
        df['COORDS'] = df.apply(lambda df: (df['LATITUDE'],df['LONGITUDE']), axis=1);
        
        #Add a new column to the hospitals DataFrame, which is the distance between the user's location and each hospital
        df['DISTANCE_MILES'] = df.apply(lambda df: geopy.distance.geodesic(df['COORDS'],coords_user).miles, axis=1);
                
        #Sort the hospitals DataFrame from shortest to longest DISTANCE_MILES and print key data for the three closest hospitals
        output = df.sort_values('DISTANCE_MILES').loc[:,['NAME','ADDRESS','CITY','STATE','ZIP','TELEPHONE','WEBSITE','DISTANCE_MILES']].iloc[0:3,:];
    
    else: 
        output = "Error: zip code not valid.";
     
    #Close the database connection
    conn.close()    
     
    return(output)

if __name__ == "__main__":
    zipcode = sys.argv[1]
    close_hosp(zipcode)
    