import AmortaPy as ap
import os
import sys
import json
from datetime import datetime
from os import system, name
from time import sleep
import time
import copy
import threading
import imp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pandasql as psql
import scipy.stats as st
import seaborn as sns
from utility import Utility
import glob
import string
import shutil

g_input_interest_rate = 0.025
g_input_loan = 500000
g_input_years = 30
g_repayment_freq = 12 # monthly
g_down_payment_pct = 0.2

g_loan_amt = g_input_loan - (g_input_loan * g_down_payment_pct)

g_period_int_rate = g_input_interest_rate/g_repayment_freq
g_periods = g_input_years*g_repayment_freq


# Simple brute force mortgage allocation change. 
def how_much_can_i_afford(monthly_allocation, interest_rate = g_input_interest_rate, 
repayment_freq = g_repayment_freq, down_payment_pct = g_down_payment_pct, input_years = g_input_years,
input_loan = g_input_loan):

    loan_amt = input_loan - (input_loan * down_payment_pct)
    period_int_rate = interest_rate/repayment_freq
    periods = input_years * repayment_freq

    df = ap.generate_amortization_table(period_int_rate, loan_amt, periods)
    period_payment = df["period_payment"][0]
    
    while period_payment > monthly_allocation:
        #print("monthly_allocation = ", monthly_allocation)
        #print("period_payment = ", period_payment)
        input_loan = input_loan - 1000
        #print("loan changes",input_loan)
        down_payment_amount = (input_loan * down_payment_pct)
        loan_amt = input_loan - down_payment_amount
        df = ap.generate_amortization_table(period_int_rate, loan_amt, periods)
        period_payment = df["period_payment"][0]
        #print(period_payment)


    while period_payment < monthly_allocation:
        #print("monthly_allocation = ", monthly_allocation)
        #print("period_payment = ", period_payment)
        input_loan = input_loan + 1000
        #print("loan changes",input_loan)
        down_payment_amount = (input_loan * down_payment_pct)
        loan_amt = input_loan - down_payment_amount
        df = ap.generate_amortization_table(period_int_rate, loan_amt, periods)
        period_payment = df["period_payment"][0]
        #print(period_payment)

    return monthly_allocation, input_loan, down_payment_amount, down_payment_pct, interest_rate , df 


monthly_allocation, property_price, down_payment_amount, down_payment_pct, interest_rate , df = how_much_can_i_afford(monthly_allocation=2000,interest_rate=0.065,down_payment_pct=0.2)

print("*" * 60)

print("With a monthly allocation of: {} .".format(monthly_allocation))
print("At an interest rate of {} .".format(interest_rate))
print("and a down payment of {} %, or $ {} ".format(down_payment_pct*100, down_payment_amount))
print("You can afford a property priced $ {} .".format(property_price))

print("*" * 60)
