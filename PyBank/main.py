import csv

budgetdata1 = "budget_data_1.csv"

total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change_list = []
greatest_increase = 0
greatest_decrease = 0

with open(budgetdata1) as csvfile:
    csvreader = csv.DictReader(csvfile)


    for row in csvreader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list.append(revenue_change)

        if revenue_change > greatest_increase:
            greatest_increase = revenue_change
        if revenue_change < greatest_increase:
            greatest_decrease = revenue_change


    
average_rev = sum(revenue_change_list)/len(revenue_change_list)


#print(total_months) 41
# print(total_revenue) 18971412
# print(average_rev) 21559.365853658535
# print(greatest_increase) 1837235
# print(greatest_decrease) -1756602
# number = []

#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)

