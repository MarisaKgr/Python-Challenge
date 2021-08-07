import os
import csv

#create path
csvpath = os.path.join('Resources','election_data.csv')

voters = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0
Khan_percent = 0.0
Correy_percent = 0.0
Li_percent = 0.0
OTooley_percent = 0.0
winner = 0
total = []
rounded_values=[]


#use path to open file, newline to move to next line
with open(csvpath,newline='') as csvfile:

    #need reader to delimiter by ,
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        #find total of voters based on voter ID column
        voters = voters + 1

        #Add totals for each candidate
        if (row[2]=="Khan"):
            Khan = Khan + 1
        elif (row[2]=="Correy"):
            Correy = Correy + 1
        elif (row[2]=="Li"):
            Li = Li +1
        elif (row[2]=="O'Tooley"):
            OTooley = OTooley +1

      
        #calculate percentages
        Khan_percent = (Khan/voters)*100
        Correy_percent = (Correy/voters)*100
        Li_percent = (Li/voters)*100
        OTooley_percent = (OTooley/voters)*100
        



        #create list and use max to find highest value for candidates
        total = (Khan,Correy,Li,OTooley)
        winner = max(total)
        
        #set max to each candidate to generate name for the candidate equal to max
        if winner == Khan:
            winner_name = "Khan"
        elif winner == Correy:
            winner_name = "Correy"
        elif winner == Li:
            winner_name = "Li"
        elif winner == OTooley:
            winner_name = "OTooley"

    #print analysis, used format with '.3f' to get third decimal place as string and not integer
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(voters))
    print("-----------------------------")
    print("Khan: " + (str(format(Khan_percent,'.3f')) + "%") + (" (" + str(Khan) + ")"))
    print("Correy: " + (str(format(Correy_percent,'.3f')) + "%") + (" (" + str(Correy) + ")"))
    print("Li: " + (str(format(Li_percent,'.3f')) + "%") + (" (" + str(Li) + ")"))
    print("OTooley: " + (str(format(OTooley_percent,'.3f')) + "%") + (" (" + str(OTooley) + ")"))
    print("-----------------------------")
    print("Winner: " + str(winner_name))
    print("-----------------------------")
 
#export results as text file
election_output = os.path.join('Resources','PyPoll_election_results.txt')
with open (election_output,'w',newline='') as text:
    myList = [("Election Results"),("-----------------------------"),("Total Votes: " + str(voters)),("-----------------------------"),("Khan: " + (str(format(Khan_percent,'.3f')) + "%") + (" (" + str(Khan) + ")")),("Correy: " + (str(format(Correy_percent,'.3f')) + "%") + (" (" + str(Correy) + ")")),("Li: " + (str(format(Li_percent,'.3f')) + "%") + (" (" + str(Li) + ")")),("OTooley: " + (str(format(OTooley_percent,'.3f')) + "%") + (" (" + str(OTooley) + ")")),("-----------------------------"),("Winner: " + str(winner_name)),("-----------------------------")]
    for i in myList:
        text.write(i+'\n')
    text.close()
        




