# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv

#path to collect data
budgetCSV = os.path.join('Resources','budget_data.csv')

with open(budgetCSV, newline="") as newfile:
    csvreader = csv.reader(newfile, delimiter=",")

    for row in csvreader:
        print (row)
    
#with open(csvpath, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    #for row in csvreader:
        #if row[0] == video:
            #print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])


