# Py Me Up, Charlie (PyBank)

# Import Modules/Dependencies
import os
import csv

# Initialize the variables
total_months = 0
net_total_amount = 0
monthy_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set path to csv file
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('Analysis', 'output.txt')
# Open and Read csv file
with open(budgetdata_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    row = next(csvreader)

    # Calculate the total number number of months, net total amount of "Profit/Losses" and set relevant variables
    previous_row = int(row[1])
    total_months += 1
    net_total_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    # Reach each row of data
    for row in csvreader:

        total_months += 1
        net_total_amount += int(row[1])

        # Calculate change in "Profits/Losses" on a month-to-month basis
        revenue_change = int(row[1]) - previous_row
        monthy_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        # Calculate the greatest increase in Profits
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in Profits (i.e. greatest instance of losses)
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    # Calculate the average change and the date
    average_change = sum(monthy_change)/ len(monthy_change)

    highest = max(monthy_change)
    lowest = min(monthy_change)

# Print Analysis
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Export results to text file

# Specify the file to write to
output_file = os.path.join('Analysis', 'output.txt')

# Open the file using "write" mode. Specify the variable to hold the contents.
with open(output_file, 'w',) as txtfile:

# Write to text file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
