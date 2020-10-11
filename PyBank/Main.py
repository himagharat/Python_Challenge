# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:55:14 2020

@author: ghara
"""
#Import Excel File
import os
import csv

#Join Path to Excel File
PyBank_csv = 'Py_Bank.csv'

#Open and Read Excel File
with open(PyBank_csv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile)
    
    #Skip Header
    print(f"Header: {csv_header}")
    
    #find net profit/loss
    P= []
    months= []
    
    #Read Rows After Header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])
   
    #Find Change in Revenue
    revenue_change= []

    for x in range (1, len(P)):
        revenue_change.append((int(P[x])-int(P[x-1])))

    # Calculate Average Revenue Change
    revenue_average=sum(revenue_change)/len(revenue_change)

    #calculate total number of months
    total_months = len(months)

    #Find Greatest Increase in Revenue
    greatest_increase= max(revenue_change)

    #Find Greatest Decrease in Revenue
    greatest_decrease= min(revenue_change)

    #Print Results
    print("Financial Analysis")
    
    print("----------------------------")
    
    print("Bank Data Analysis")

    print("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(P)))

    print("Average Change:" + "$" + str(revenue_average))

    print("Greatest Increase in Profits:" + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
                                                   
    print("Greatest Decrease in Profits:" + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
    
    #output to txt file
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()


