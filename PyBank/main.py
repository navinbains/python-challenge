# Import Modules

import os
import csv

# Retrieve Data 

filepath = os.path.join("C:\\Users\\Coding\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv")


# Define and Create Lists

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


# Open and read csv

with open(filepath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    print(f"Header: {csv_header}")
    # This prints -->> Header: Date, Profit/Losses
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count  months
        count_months += 1

        # Profit/Losses
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

           
            months.append(row[0])

        
            profit_loss_changes.append(profit_loss_change)

          
            previous_month_profit_loss = current_month_profit_loss

    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)


    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export text file with results
analysis_text_file = os.path.join("C:\\Users\\Coding\\Documents\\GitHub\\python-challenge\\PyBank\\Analysis\\analysis.txt")
with open(analysis_text_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")
