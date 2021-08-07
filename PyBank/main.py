import os
import csv


#create path 
csvpath = os.path.join('Resources','budget_data.csv')

Month = 0
Total = 0.0
average = 0
end_change = 0
start_change = 0
row_changes =[]
Dates=[]
greatest_increase = 0
greatest_decrease = 0




#use path to open file, newline to move to next line
with open(csvpath, newline='') as csvfile:

    
    #need reader to delimiter by ,
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
   
    for row in csvreader:
        #find total of date column 
        Month=Month+1   
        

        #find total of column profit/loss
        Total= Total +float(row[1])
        

        #find the change in each row subtracting the end from the start in each row
        end_change = int(row[1])
        row_change = end_change - start_change
        #next starting point is previous row ending point
        start_change = end_change
        row_changes.append(row_change)

        
        #average to the total of changes per row divided by number of rows(established in month count calculation)
        average = sum(row_changes)/len(row_changes)
       

        #find mximum value
        greatest_increase = max(row_changes)
       
        #find greatest decrease
        greatest_decrease = min(row_changes)
              
        #append date list to index date to min/max
        Dates.append(row[0])
        greatest_dec_month = Dates[row_changes.index(greatest_decrease)]
        greatest_inc_month = Dates[row_changes.index(greatest_increase)]
        
    #print analysis        
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(Month))
    print("Total: " + str(Total))
    print("Average Change: " + str(average))
    print("Greatest Increase in Profits: " + (str(greatest_inc_month) + " $") + str(greatest_increase))
    print("Greatest Decrease in Profits: " + (str(greatest_dec_month)+" $") + str(greatest_decrease))
  
 #export analysis in text format
test_output = os.path.join('Resources','pybank_analysis.txt')
with open (test_output,'w',newline='') as text:
    myList = [("Financial Analysis"),("-----------------------------------"),("Total Months: " + str(Month)),("Total: " + str(Total)),("Average Change: " + str(average)),("Greatest Increase in Profits: " + (str(greatest_inc_month) + " $") + str(greatest_increase)),("Greatest Decrease in Profits: " + (str(greatest_dec_month)+" $") + str(greatest_decrease))]
     
    for i in myList:
        text.write(i+'\n')
    text.close()