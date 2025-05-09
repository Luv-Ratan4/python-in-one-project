import pandas as pd
import csv  #This is the csv module
from datetime import date   #this is a built in module in python


#we will first initiate a class 
class CSV:
    CSV_FILE = "finance_data.csv" # This is a class variable because it is associated with the class and it can only be accessed within this class
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Date","Amount","Category","Description"])
            df.to_csv(cls.CSV_FILE, index=False)

CSV.initialize_csv()
