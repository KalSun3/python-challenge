# import
import os
import csv

#Input & Output Paths
PyBank = os.path.join('Resources', 'budget_data.csv')
OutPath = os.path.join('analysis', 'output_txt')
#Variables

TotalMonths = 0
PrevRevenue = 0
MonthChange = []
RevChangeList = []
GreatIncrease = ["", 0]
GreatDecrease = ["", 9999999999999999]
TotalRev = 0 

with open(PyBank) as csvfile:
    PyBankReader = csv.DictReader(csvfile)

    for row in PyBankReader:
        #Track Totals
        TotalMonths = TotalMonths + 1
        TotalRev = TotalRev + int(row["Profit/Losses"])

        #Calculate Rev Change
        RevChange = int(row["Profit/Losses"]) - PrevRevenue
        PrevRevenue = int(row['Profit/Losses'])
        RevChangeList.append(RevChange)
        MonthChange = MonthChange + [row['Date']]

        #Greatest Increase
        if (RevChange > GreatIncrease[1]):
            GreatIncrease[0] = row['Date']
            GreatIncrease[1] = RevChange

        #Calculate Decrease
        if (RevChange < GreatDecrease[1]):
            GreatDecrease[0] = row['Date']
            GreatDecrease[1] = RevChange
#Calculate Average
RevAvg = sum(RevChangeList) / len(RevChangeList)

output = (
    f'\n Financial Analysis \n'
    f'--------------------------\n'
    f'Total Months: {TotalMonths}\n'
    f'Total Revenue: {TotalRev}\n'
    f'Average Revenue Change: $ {RevAvg}\n'
    f'Greatest Increase in Revenue: {GreatIncrease[0]} (${GreatIncrease[1]})\n'
    f'Greatest Decrease in Revenue: {GreatDecrease[0]} (${GreatDecrease[1]})\n'
)

#printoutput
print(output)
with open (OutPath, "w") as txt_file:
    txt_file.write(output)