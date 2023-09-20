import os
import sys
import json
from datetime import datetime
from os import system, name
from time import sleep
import copy
import threading
import imp
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pandasql as psql
from  libraries.utility import Utility



class data_objects(Utility):
    
    MONTHLY_ALLOCATION_DF = None
    INTEREST_RATE_DF = None
    DOWN_PAYMENT_PCT_DF = None
    LOAN_TERM_DF = None
    STATE_FILE_DF = None
    COUNTY_FILE_DF = None
    MSA_FILE_DF = None
    CAL_CITY_TO_LONG_LAT_DF = None
    CAL_CITY_TO_POPULATION_DF = None
 

    def __init__(self,load_data_from_url=False):
        super().__init__()
        global MONTHLY_ALLOCATION_DF
        global INTEREST_RATE_DF
        global DOWN_PAYMENT_PCT_DF
        global LOAN_TERM_DF
        global STATE_FILE_DF
        global COUNTY_FILE_DF
        global MSA_FILE_DF
        global CAL_CITY_TO_LONG_LAT_DF
        global CAL_CITY_TO_POPULATION_DF
        global BG_POP_DF
        global AVG_HOME_AGE_DF
        global HH_INCOME_DF
        global AVG_BEDS_DF 
        global AVG_BATHS_DF
        global AVG_OCCUPANCY_DF

        if load_data_from_url == False:
            MONTHLY_ALLOCATION_DF, INTEREST_RATE_DF, DOWN_PAYMENT_PCT_DF, LOAN_TERM_DF = self.load_monthly_allocation_data()
            STATE_FILE_DF, COUNTY_FILE_DF, MSA_FILE_DF  = self.load_state_drop_down_data()
            CAL_CITY_TO_LONG_LAT_DF, CAL_CITY_TO_POPULATION_DF, BG_POP_DF, AVG_HOME_AGE_DF, \
                HH_INCOME_DF, AVG_BEDS_DF, AVG_BATHS_DF, AVG_OCCUPANCY_DF = self.load_cal_city_data()

    def avg_occupacy(self):
        global AVG_OCCUPANCY_DF
        my_sql = '''
        SELECT
            avg_occupancy
        FROM 
            AVG_OCCUPANCY_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))

    def avg_baths_tuple(self):
        global AVG_BATHS_DF

        my_sql = '''
        SELECT
            avg_baths
        FROM 
            AVG_BATHS_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))


    def avg_baths_tuple(self):
        global AVG_BATHS_DF

        my_sql = '''
        SELECT
            avg_beds
        FROM 
            AVG_BEDS_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))


    def avg_beds_tuple(self):
        global AVG_BEDS_DF

        my_sql = '''
        SELECT
            avg_beds
        FROM 
            AVG_BEDS_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))


    def h_age_tuple(self):
        global AVG_HOME_AGE_DF

        my_sql = '''
        SELECT
            avg_home_age
        FROM 
            AVG_HOME_AGE_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))

    def hh_income_tuple(self):
        global HH_INCOME_DF

        my_sql = '''
        SELECT
            annual_income
        FROM 
            HH_INCOME_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))


    def bg_pop_tuple(self):
        global BG_POP_DF

        my_sql = '''
        SELECT
            block_group_population as bg_pop
        FROM 
            BG_POP_DF
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,0],ma.iloc[:,0]))


    def ca_pop_df(self):
        global CAL_CITY_TO_POPULATION_DF
        return CAL_CITY_TO_POPULATION_DF
        

    def ca_pop_by_city(self,city):
        global CAL_CITY_TO_POPULATION_DF
        my_sql='''
        select
        pop_april_2010 as population
        from CAL_CITY_TO_POPULATION_DF
        where ltrim(rtrim(lower(City))) = \'''' + city.strip().lower() + '''\'
        '''
        return psql.sqldf(my_sql)

    def ca_city_lat_long_df(self):
        global CAL_CITY_TO_LONG_LAT_DF

        my_sql = '''
        SELECT
            name as city,
            Latitude, 
            Longitude 
        FROM 
            CAL_CITY_TO_LONG_LAT_DF
        ORDER BY city
        '''
        return psql.sqldf(my_sql)
        #return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))


    def ca_city_lat_long_tuple(self):
        global CAL_CITY_TO_LONG_LAT_DF

        my_sql = '''
        SELECT
            name as city,
            Latitude ||','|| Longitude as lat_long
        FROM 
            CAL_CITY_TO_LONG_LAT_DF
        ORDER BY city
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))
    




    def load_cal_city_data(self):

        data_directory          = "data"
        sub_dir                 = "cal_city_data"
        cal_cities_lat_long     = "cal_cities_lat_long.csv"
        cal_populations_city    = "cal_populations_city.csv"
        bg_population           = "bg_populations.csv"
        avg_home_age            = "avg_home_age.csv"
        hh_income               = "hh_income.csv"
        AVG_BEDS                = "avg_beds.csv"
        AVG_BATHS               = "avg_baths.csv"
        AVG_OCCUPANCY           = "avg_occupancy.csv"

        dir = os.path.join(self.get_this_dir(),data_directory,sub_dir)

        CAL_CITY_TO_LONG_LAT_DF = pd.read_csv(os.path.join(dir,cal_cities_lat_long))

        CAL_CITY_TO_POPULATION_DF = pd.read_csv(os.path.join(dir,cal_populations_city))

        BG_POP_DF  = pd.read_csv(os.path.join(dir,bg_population))

        AVG_HOME_AGE_DF = pd.read_csv(os.path.join(dir,avg_home_age))
                
        HH_INCOME_DF =  pd.read_csv(os.path.join(dir,hh_income))

        AVG_BEDS_DF = pd.read_csv(os.path.join(dir,AVG_BEDS))

        AVG_BATHS_DF = pd.read_csv(os.path.join(dir,AVG_BATHS))

        AVG_OCCUPANCY_DF = pd.read_csv(os.path.join(dir,AVG_OCCUPANCY))

        return CAL_CITY_TO_LONG_LAT_DF, CAL_CITY_TO_POPULATION_DF, BG_POP_DF, \
            AVG_HOME_AGE_DF, HH_INCOME_DF, AVG_BEDS_DF, AVG_BATHS_DF, AVG_OCCUPANCY_DF


    def print_internal_directory(self):

        for k,v in self.__dict__.items():
            print("{} is \"{}\"".format(k,v))

    def get_affordability_data(self):
        global MONTHLY_ALLOCATION_DF
        global INTEREST_RATE_DF
        global DOWN_PAYMENT_PCT_DF
        global LOAN_TERM_DF


        return DOWN_PAYMENT_PCT_DF , INTEREST_RATE_DF, MONTHLY_ALLOCATION_DF, LOAN_TERM_DF

    def monthly_allocation_tuple(self):
        global MONTHLY_ALLOCATION_DF

        ma = MONTHLY_ALLOCATION_DF
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def interest_rate_tuple(self):
        global INTEREST_RATE_DF

        ma = INTEREST_RATE_DF
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def down_payment_tuple(self):
        global DOWN_PAYMENT_PCT_DF

        ma = DOWN_PAYMENT_PCT_DF
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def loan_term_tuple(self):
        global LOAN_TERM_DF

        ma = LOAN_TERM_DF
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def state_names_tuple(self):
        global STATE_FILE_DF
        ma = STATE_FILE_DF
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def county_names_tuple(self,state):
        global COUNTY_FILE_DF

        my_sql = '''
        SELECT
            county_name,
            county_name_state
        FROM 
            COUNTY_FILE_DF
        WHERE 
            state =  \'''' + state.lower().lower() + '''\'
        and
            county_name_state != \'''' + 'agler_fl' + '''\'
        ORDER BY county_name
        '''
        ma = psql.sqldf(my_sql)
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    def msa_names_tuple(self,state):
        global MSA_FILE_DF

        my_sql = '''
        SELECT
            county_name,
            county_name_state
        FROM 
            MSA_FILE_DF
        WHERE 
            state =  \'''' + state.upper() + '''\'
        ORDER BY county_name
        '''
        ma = psql.sqldf(my_sql)
        #print(ma)
        return tuple(zip(ma.iloc[:,1],ma.iloc[:,0]))

    

    def load_monthly_allocation_data(self):

        data_directory      = "data"
        sub_dir             = "affordability_calculator"
        downpayment_amount  = "downpayment_amount.csv"
        interest_rates      = "interest_rates.csv"
        monthly_allocation  = "monthly_allocation.csv"
        loan_term           = "loan_term.csv"

        downpayment_amount = pd.read_csv(os.path.join(self.get_this_dir(),data_directory,sub_dir,downpayment_amount))

        interest_rates = pd.read_csv(os.path.join(self.get_this_dir(),data_directory,sub_dir,interest_rates))

        monthly_allocation = pd.read_csv(os.path.join(self.get_this_dir(),data_directory,sub_dir,monthly_allocation))

        loan_term = pd.read_csv(os.path.join(self.get_this_dir(),data_directory,sub_dir,loan_term))

        #print(downpayment_amount)

        return monthly_allocation, interest_rates, downpayment_amount, loan_term

    def load_state_drop_down_data(self):

        data_directory          = "data"
        sub_dir                 = "ml_predictions"
        sub_dir1                = "files_for_drop_downs"
        state_file              = "state_file.csv"
        unique_counties         = "unique_counties.csv"
        unique_counties_msa     = "unique_counties_msa.csv"

        dir = os.path.join(self.get_this_dir(),data_directory,sub_dir,sub_dir1)

        state_file = pd.read_csv(os.path.join(dir,state_file))

        unique_counties = pd.read_csv(os.path.join(dir,unique_counties))

        unique_counties_msa = pd.read_csv(os.path.join(dir,unique_counties_msa))

        return state_file, unique_counties, unique_counties_msa


