# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:54:06 2019

@author: nguye
"""

#import modules
import os
import csv

# Path for the CSV file 

file_csv = os.path.join("Resources","budget_data.csv")

# Initiate export file
exportfile = "finanalysis.txt"

# Empty lists to store data. 
profit = []
monthlychange = []
monthcount = []

# Initialize the variables 
totalmonthcount = 0
startprofit = 0
totalprofit = 0
totchangeprofit = 0


# Open the CSV using the set path 

with open(file_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csv_reader)

    #first row
    first_row = next(csv_reader)
    totalmonthcount = totalmonthcount + 1 
    totalprofit = totalprofit + int(first_row[1])
    startprofit = int(first_row[1])
    
    
    for row in csv_reader:
        # Count the number months in this dataset
        totalmonthcount = totalmonthcount + 1 
        # Add profit to list, calculate the total profit
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])
        
        # Calculate the avg change in profits m/m, calulate the avg change in profits
        finalprofit = int(row[1])
        monthlychangeprofits = finalprofit - startprofit
        
        # Add monthly changes in a list
        monthlychange.append(monthlychangeprofits)
        
        totchangeprofit = totchangeprofit + monthlychangeprofits
        startprofit = finalprofit

        # Calculate the avg change in profits
        avg_change_profit = round((totchangeprofit/(totalmonthcount-1)),2)
      
        # Collect the largest increase/decrease in profits
        monthcount.append(row[0])      
      
        # Look for the max/min change in profits with dates
        maxprofit = max(monthlychange)
        minprofit = min(monthlychange)

        maxprofitdate = monthcount[monthlychange.index(maxprofit)]
        minprofitdate = monthcount[monthlychange.index(minprofit)]
    
    #Print results
    print("Financial Analysis")
    print(
            f"--------------------\n"
            f"Total Months: {totalmonthcount}\n"
            f"Total Profits: ${totalprofit}\n"
            f"Average Change: $ {avg_change_profit}\n"
            f"Greatest Increase in Profits: {maxprofitdate} (${maxprofit})\n"
            f"Greatest Decrease in Profits: {minprofitdate} (${minprofit})\n"
            )
#Export results to new file
with open(exportfile, 'w') as file:
    file.write("Financial Analysis\n")
    file.write(f"---------------------------\n")
    file.write(f"Total Months: {totalmonthcount}\n")
    file.write(f"Total Profits: {totalprofit}\n")
    file.write(f"Average Change: ${avg_change_profit}\n")
    file.write(f"Greatest Increase in Profits: {maxprofitdate} (${maxprofit})\n")
    file.write(f"Greatest Decrease in Profits: {minprofitdate} (${minprofit})\n")