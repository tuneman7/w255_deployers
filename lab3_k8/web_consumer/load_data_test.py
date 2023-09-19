from libraries.data_objects import data_objects as do
from libraries.altair_renderings import AltairRenderings
from libraries.utility import Utility 
import socket 
from libraries.mortgage_amort import Affordability as ma
from libraries.analysis_object import analysis_object as Analysis

def test_amort():
    my_amort = ma()
    my_amort.how_much_can_i_afford(monthly_allocation=1750, interest_rate = 0.065, 
    repayment_freq = 12, down_payment_pct = 0.07, input_years = 30,
    input_loan = 50000,print_output=True)

def load_analysis_object():
    my_ao = Analysis("clark_nv")



def main():
    load_analysis_object()


main()




