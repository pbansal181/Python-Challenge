import os, csv

#set path for input file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#set path for output file
text_file = os.path.join('Analysis', 'Financial_summary.txt')

#create empty list variables
total_month = []
total_profit = []
profit_change = []

with open(csvpath) as csvfile:
 csvreader = csv.reader(csvfile, delimiter = ',')
 header = next(csvreader)
#iterate through all rows
 for row in csvreader:
    total_month.append(row[0])
    total_profit.append(int(row[1]))

#iterate through the profits to find changes in profit/loss
 for i in range(len(total_profit) - 1):
    profit_change.append(total_profit[i+1] - total_profit[i])

#Calculation of max and min profit change
    max_increase = max(profit_change)
    max_decrease = min(profit_change)

#Final value of max incraese and decrease monthly
    max_inc_month = profit_change.index(max(profit_change)) + 1
    max_dec_month = profit_change.index(min(profit_change)) + 1

#Printing the output statements
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {len(total_month)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase in Profits: {total_month[max_inc_month]} (${(str(max_increase))})")
    print(f"Greatest Decrease in Profits: {total_month[max_dec_month]} (${(str(max_decrease))})")

#Writing all the output to the file we created
    with open(text_file, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {len(total_month)}\n")
        file.write(f"Total: ${sum(total_profit)}\n")
        file.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n")
        file.write(f"Greatest Increase in Profits: {total_month[max_inc_month]} (${(str(max_increase))})\n")
        file.write(f"Greatest Decrease in Profits: {total_month[max_dec_month]} (${(str(max_decrease))})\n")




