import pandas as pd
import csv  #This is python's built in csv module
from datetime import date   #this is a built in module in python


#we will first initiate a class 
class CSV:
    CSV_FILE = "finance_data.csv" # This is a class variable because it is associated with the class and it can only be accessed within this class
    COLUMNS = ["Date","Amount (in dollars)","Category","Description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "Date":date,
            "Amount (in dollars)": amount,
            "Category": category,
            "Description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvFile:    # We opened the file in append mode which is denoted by "a"
            # the above line is known as a context manager and it is opening this csv file as csvFile so all the context about this csv file will be stored int he csvFile 
            writer = csv.DictWriter(csvFile, fieldnames=cls.COLUMNS)    #We are creating a csv writer . This will take in a dictionary and write it into a csv file.

            writer.writerow(new_entry)
            print("Entry added successfully")

CSV.initialize_csv()
CSV.add_entry("10-05-2025", "200", "MSC Financial Engineering", "Python" )
