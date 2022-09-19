# Import Modules

import os
import csv

# Retrieve Data

filepath = os.path.join("C:\\Users\\Coding\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#Define and Create Lists

total_votes_cast = 0
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0
candidate = set()
winner = 0

# Open the CSV path where the file is located
with open(filepath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")

     #Reading the header row to skip to the next line
    csv_header = next(csvreader)
    
    #Loop through every row
    for row in csvreader:

#To get the total number of vote cast
        total_votes_cast += 1
        candidate.add(row[2])

#To get the number of vote per candidate
        if (row[2] == "Charles Casper Stockham"):
            Stockham_votes += 1
        elif (row[2] == "Diana DeGette"):
            DeGette_votes += 1
        else:
            Doane_votes += 1

#To get the percentage of votes for each candidate

Stockham_Percent = (Stockham_votes/total_votes_cast) 
DeGette_percent = (DeGette_votes/total_votes_cast) 
Doane_percent = (Doane_votes/total_votes_cast) 

#The winner of the election 
vote_total = [ Stockham_votes, DeGette_votes, Doane_votes ]

#Assign variables
winner_counts = max(vote_total)
winner_name = ""

#Use if statement to check winner
if winner_counts == Stockham_votes :
    winner_name = "Charles Casper Stockham"

elif winner_counts == DeGette_votes :
    winner_name = "Diana DeGette"   

elif winner_counts == Doane_votes :
    winner_name = "Raymon Anthony Doane"

else :
    winner_name = "No winner"



#Print the above statements

print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes_cast))
print("---------------------")
print("Charles Casper Stockham: " + "{:.3%}".format(Stockham_Percent) + " " + (str(Stockham_votes)))
print("Diana DeGette: " + "{:.3%}".format(DeGette_percent) + " " + (str(DeGette_votes)))
print("Raymond Anthony Doane: " + "{:.3%}".format(Doane_percent) + " " + (str(Doane_votes)))
print("---------------------")
print("Winner: " +  winner_name)
print("---------------------")
print("----")

# Printing analysis to the text file

output_path = os.path.join("C:\\Users\\Coding\\Documents\\GitHub\\python-challenge\\PyPoll\\Analysis\\Results.txt")

with open(output_path, 'w') as file:

    file.write("Election Results")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes_cast))
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Charles Casper Stockham: " + "{:.3%}".format(Stockham_Percent) + " " + (str(Stockham_votes)))
    file.write("\n")
    file.write("Diana DeGette: " + "{:.3%}".format(DeGette_percent) + " " + (str(DeGette_votes)))
    file.write("\n")
    file.write("Raymond Anthony Doane: " + "{:.3%}".format(Doane_percent) + " " + (str(Doane_votes)))
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Winner: " +  winner_name)
    file.write("\n")
    file.write("---------------------")