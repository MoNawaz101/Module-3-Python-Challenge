import os
import csv

#Set path to the Resources folder which contains the CSV file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Initial variables and lists
Months = []
ProfitorLoss = []
TotalProfit = 0
ChangeinProfitorLoss = []
TotalChangeinProfitorLoss = 0
AverageChangeinProfitorLoss = 0.0
NumRows = 0

#Read the data in the CSV file into csvreader
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Copy the CSV data into two lists, one for the months and the other for the 
    #associated profit or loss in that month.
    for Month in csvreader:
        Months.append(Month[0])
        ProfitorLoss.append(Month[1])
   
#Find how many months worth of data there are.
NumMonths = len(Months)

#Add up all the profit or losses per month to give a total
#Ignore the header so start the loop at 1 which is the 2nd item
for Month in range(1,NumMonths):
    TotalProfit = TotalProfit + int(ProfitorLoss[Month])
    #The first month does not have a previous month of profit or loss data
    #so a change can't be calculated. So ignore the first month.
    if Month >= 2:
        #subtract the previous months profit/loss from the present month to give the change
        ChangeinProfitorLoss.append(int(ProfitorLoss[Month])-int(ProfitorLoss[Month-1]))
    else:
        ChangeinProfitorLoss.append(0)          #put a 0 in the 1st cell as the first month does not have a change in profit figure
            
#Find out how many rows of change in profit or loss data there are and then sum ignoring first row.
NumRows = len(ChangeinProfitorLoss)
for Row in range(1,NumRows):
    TotalChangeinProfitorLoss += ChangeinProfitorLoss[Row]

#Take the sum of the change in profit or loss data and divide by the number of rows to give the 
#average change in profit or loss. Ignore first row as it has been set to 0.
AverageChangeinProfitorLoss = round(TotalChangeinProfitorLoss/( NumRows-1 ),2)  

#Find the maximum and minimum change in profit or loss in the monthly data and for which month 
MaxIncProfits = max(ChangeinProfitorLoss) 
index = ChangeinProfitorLoss.index(MaxIncProfits)
MonthMaxIncProfits = Months[index+1]                #Add 2 because the first line is the header file plus the first month did not have any change data
 
MaxDecProfits = min(ChangeinProfitorLoss)
index = ChangeinProfitorLoss.index(MaxDecProfits)
MonthMaxDecProfits = Months[index+1]                #Add 2 because the first line is the header file plus the first month did not have any change data
 
    
#Set up the strings which can be used to print to both the text file and the terminal
Header1 = "Financial Analysis "
Header2 = "----------------------------------------------------------------"
TotalMonths = "Total Months : "  + str(NumMonths-1)
TotalProfits = "Total: $" + str(TotalProfit)
AverageChange = "Average Change: $" + str(AverageChangeinProfitorLoss)  
GreatestIncProfits = "Greatest Increase in Profits: " + MonthMaxIncProfits + " ($" + str(MaxIncProfits) + ")"
GreatestDecProfits = "Greatest Decrease in Profits: " + MonthMaxDecProfits + " ($" + str(MaxDecProfits) + ")"



#Print to the terminal
print(f'\n{Header1}\n')
print(f'{Header2}\n')
print(f'{TotalMonths}\n')
print(f'{TotalProfits}\n')     
print(f'{AverageChange}\n')    
print(f'{GreatestIncProfits}\n')
print(f'{GreatestDecProfits}\n')


#print to the text file

#Set variable for output file
output_file = os.path.join("Analysis","pybank.txt")

#  Open the output file
with open(output_file, "w",newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header rows
    writer.writerow([Header1])
    writer.writerow([])
    writer.writerow([Header2])
    writer.writerow([])
    # Write in data rows
    writer.writerow([TotalMonths])
    writer.writerow([])
    writer.writerow([TotalProfits])
    writer.writerow([])
    writer.writerow([AverageChange])
    writer.writerow([])
    writer.writerow([GreatestIncProfits])
    writer.writerow([])
    writer.writerow([GreatestDecProfits])
    
     

