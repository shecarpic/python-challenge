#import module
import csv


#Path to collect the data from the resources folder
#csvpath = '/Users/alphamalenailcareservices/Desktop/Data Bootcamp/Python/Starter_Code_3/PyBank/Resources/budget_data.csv'
csvpath = 'Resources/budget_data.csv'
analysispath = 'analysis/pybank.txt'
#define the functions
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []
#read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header = next(csvreader)
  
#loop through each row in the dataset
    for row in csvreader:
        current_date = row[0]
        profit_loss = int(row[1])
      

        #Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        #Calculate the change in profit/loss and store in the changes
        if total_months > 1:
            current_change =profit_loss - previous_profit_loss
            changes.append(current_change)
            
#update previous date for next iteration
            dates.append(current_date)
#update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# calculate average change
    average_change = sum(changes)/len(changes)
#find  greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]

#print the results
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months:{total_months}")
    print(f"Total:${net_total}")
    print(f"Average Change: ${average_change: .2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open(analysispath,'w') as pybank_txt: 
    pybank_txt.write("Financial Analysis\n")
    pybank_txt.write("--------------------------\n")
    pybank_txt.write(f"Total Months:{total_months}\n")
    pybank_txt.write(f"Total:${net_total}\n")
    pybank_txt.write(f"Average Change: ${average_change: .2f}\n")
    pybank_txt.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    pybank_txt.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
       
        