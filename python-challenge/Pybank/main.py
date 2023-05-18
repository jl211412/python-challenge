import os
import csv

csvpath = os.path.join('/Users/jackielarios/Desktop/python-challenge/Pybank/Resources/budget_data.csv')

with open(csvpath, 'r') as budgetfile:
    csvreader = csv.reader(budgetfile)
    # read & skip header
    header = next(csvreader)
    # read remaining data
    data = list(csvreader)

    # calculate months
    total_months = len(data)

    # insert variables
    total_profit_losses = 0
    previous_profit_loss = 0
    changes = []

    # calculate total profit/losses and changes
    for row in data:
        profit_loss = int(row[1])
        total_profit_losses += profit_loss

        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)

        previous_profit_loss = profit_loss

    # calculate avg
    average_change = sum(changes) / len(changes)

    # find greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    # find dates for the greatest increase and decrease
    increase_index = changes.index(greatest_increase)
    decrease_index = changes.index(greatest_decrease)
    greatest_increase_date = data[increase_index + 1][0]
    greatest_decrease_date = data[decrease_index + 1][0]

output_folder = '/Users/jackielarios/Desktop/python-challenge/Pybank/Analysis'
output_file = os.path.join(output_folder, 'Budget_Results.txt')

# open the output file in write mode
with open(output_file, 'w') as outfile:

    # print 
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit_losses}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
