#import dependencies
import os
import csv

#declaring variables
TotalMonths = 0
TotalRevenue = 0
PreviousRevenue = 0
HighIncProfit = 0
HighDecProfit = 99999999999

#Open List to store revenue change
RevenueChange = []

#Map the file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Read contents of csv file
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')
    next(csvdata, None)

    for row in csvdata:
        #count total months in csv file
        TotalMonths = TotalMonths + 1

        #count total revenue in csv file
        TotalRevenue = TotalRevenue + (int(row[1]))
        #print(type(row[1])) <--check the data type and issues with str

        #create a variable that will count the revenue change
        monthlyRevenueChange = int(row[1]) - PreviousRevenue
        PreviousRevenue = int(row[1])

        #add changes in new list
        RevenueChange.append(monthlyRevenueChange)

        #calculate the average change in revenue
        avgRevenueChange = round(sum(RevenueChange)/TotalMonths)
        #print(avgRevenueChange)

        #find the greatest increase in revenue
        if (monthlyRevenueChange > HighIncProfit):
            highestIncMonth = row[0]
            HighIncProfit = monthlyRevenueChange 

        #find the greatest decrease in revenue
        if (monthlyRevenueChange < HighDecProfit):
            lowestDecMonth = row[0]
            HighDecProfit = monthlyRevenueChange

#create varible and assign results
Results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {TotalMonths} \n"
f"Total: ${TotalRevenue} \n"
f"Average Change: ${avgRevenueChange} \n"
f"Greatest Increase in Profits: {highestIncMonth} (${HighIncProfit}) \n"
f"Greatest Decrease in Profits: {lowestDecMonth} (${HighDecProfit}) \n")
print(Results)

#write a text file in order to export results to text file
outputtxt = os.path.join('Resources/PyBankAnalysis.txt')

with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)