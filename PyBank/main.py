import os 
import csv

budgetdata1 = os.path.join("..","PyBank", "budget_data_1.csv")
budgetdata2 = os.path.join("..","PyBank", "budget_data_2.csv")

with open(budgetdata1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

with open(budgetdata2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(row)
number = []
#The total number of months included in the dataset
