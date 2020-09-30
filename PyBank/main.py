#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#%%
#import modules
import os
import csv

#find file
raw_budget_data = os.path.join("Resources/raw_budget_data.csv")

#with open(raw_budget_data, 'r') as csvfile:
    
    #budgetreader = csv.reader(csvfile, delimiter = ',')

    #print(budgetreader)

    #csv_header = next(budgetreader)
    #print(f"CSV Header: {csv_header}")

    #read each row of data after the header
    #for row in budgetreader:
        #print(row)

#set lists to hold the data
total_months=[]

#The total number of months included in the dataset
total_months = 0

with open(raw_budget_data) as csvfile:
    budgetreader = csv.reader(csvfile)

    if csv.Sniffer().has_header:
        next(budgetreader)
    for row in budgetreader:
        #total number of months
        total_months += 1

print ("Financial Analysis")
print ("----------------------")
print ("Total Months: " + str(total_months))
#print (total_months)


#The net total amount of "Profit/Losses" over the entire period
profit =[]

with open(raw_budget_data) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter= ",")

    if csv.Sniffer().has_header:
        next(budgetreader)
    
    for row in budgetreader:
        
        #net total of profits/losses
        amount = row[1]
        profit.append(amount)
        float_profit = [float(integral) for integral in profit]
        net_total = sum(float_profit)

print ("Net Total: " + str(net_total)) 
#print (net_total)

#The average of the changes in "Profit/Losses" over the entire period
change =[]

with open(raw_budget_data) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter= ",")
    
    for row in budgetreader:
        change.append(row[1])
        
        ##for amount in range (0, len(change)):
            ##print (change[amount])
        
        #assign first and last elements to variables
        #start_profit, end_profit = [change[i] for i in (1, 86)] 
        start_profit = (change[2])
        print (start_profit)
        
        #average change is (end profit-start profit)/total number of months
        ##average_change = (end_profit - start_profit)/total_months

#class example
#Creating lists to store data
##months = []
##with open(pybank_csv, 'r') as budgetreader:
    ##pybankcsv = csv.reader(budgetreader, delimiter = 'r')
    ##next(pybankcsv)
#Loop through file to add to the month and profit lists
    ##for row in pybankcsv:
        ##months.append(row[0])


##print ("Average Change: " + str(average_change)) 

#index of 671099.00 in change
index = change.index('671099.00')
print(index)

index = change.index('867884.00')
print(index)

print (change[-1])
print (change[86])
print (change[1])





#The greatest increase in profits (date and amount) over the entire period

    ##print (row[0])

#The greatest decrease in losses (date and amount) over the entire period

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

##Text_File = open("Text_File.txt","w")
#You write to the file using
##Text_file.write("")
#and close using
##Text_file.close()


# Zip lists together
##Analysis_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
##output_file = os.path.join("web_final.csv")

#  Open the output file
##with open(output_file, "w") as datafile:
    ##writer = csv.writer(datafile)

    # Write the header row
    ##writer.writerow(["Title", "Course Price", "Subscribers"])

    # Write in zipped rows
    ##writer.writerows(cleaned_csv)

#text example:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
# %%
