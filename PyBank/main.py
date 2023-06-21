# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

#import modules
import os
import csv

# path to collect data from resources folder
budget_data_csv=os.path.join('/Users/hchen/Desktop/python-challenge/PyBank/','Resources','budget_data.csv')

# Lists to store data
PnL=[]
months=[]
PnL_change=[]

# open and read csv
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

# read/skip the header row first
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

# read through each row, add PnL, months
    for row in csvreader:
        PnL.append(int(row[1]))
        months.append(row[0])

#read through PnL change
    for x in range(1,len(PnL)):
        PnL_change.append(int(PnL[x])-int(PnL[x-1]))

# calculate average PnL change
PnL_change_average=sum(PnL_change)/len(PnL_change)

#calculate total number of months
total_months=len(months)

# greatest increase/decrease in profit
greatest_increase=max(PnL_change)
greatest_decrease=min(PnL_change)

 # print the final results
print("Financial Analysis")
print("-------------------")
print("total months: " + str(total_months))
print("Total: " + "$" + str(sum(PnL)))
print("Average change: " + "$" + str(PnL_change_average))

print("Greatest Increase in Profits: " + str(months[PnL_change.index(greatest_increase)+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[PnL_change.index(greatest_decrease)+1]) + " " + "$" + str(greatest_decrease))

# Export a text file with the results
with open('PyBank.txt', 'w') as file:
        file.write('Financial Analysis\n')
        file.write('-------------------\n')
        file.write("total months: " + str(total_months)+"\n")
        file.write("Total: " + "$" + str(sum(PnL))+"\n")
        file.write("Average change: " + "$" + str(PnL_change_average)+"\n")
        file.write("Greatest Increase in Profits: " + str(months[PnL_change.index(greatest_increase)+1]) + " " + "$" + str(greatest_increase)+"\n")
        file.write("Greatest Decrease in Profits: " + str(months[PnL_change.index(greatest_decrease)+1]) + " " + "$" + str(greatest_decrease)+"\n")