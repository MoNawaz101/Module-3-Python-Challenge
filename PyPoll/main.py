import os
import csv
from collections import defaultdict

#Set path to the Resources folder which contains the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

#Initial variables and lists
VoterID = []
County = []
Candidate = []
VoteCount = defaultdict(int)
TotalVotesCast = 0
NumVotesPerCand = []
CandidateNames = []
PercVotesCast = []
Index = 0
MaxVotes = 0

#Read the data in the CSV file into csvreader
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    for Vote in csvreader:
        #Create a default data dictionary (VoteCount) which contains the unique candidate name and the
        # number of votes cast for each candidate 
        VoteCount[Vote[2]] += 1

#Copy the values and the keys from the dictionary into lists so they are more easily used
NumVotesPerCand = list(VoteCount.values())
CandidateNames = list(VoteCount.keys())

NumCandidates = len(CandidateNames)

#Count the total votes whilst missing out the key (start num=1)
for num in range(1,NumCandidates):
    TotalVotesCast += NumVotesPerCand[num]

#A list with the % of votes cast per candidate
PercVotesCast = [round(100*NumVotesPerCand[votes]/TotalVotesCast,3) for votes in range(0,NumCandidates)]


#Identify the candidate with the most votes
MaxVotes = max(PercVotesCast) 
index = PercVotesCast.index(MaxVotes)
Winner = CandidateNames[index]


#Create strings to print to both the terminal and text file
Header1 = "Election Results"
Header2 = "-----------------------------------------------"
TotalVotes = "Total Votes: " + str(TotalVotesCast)
Candidate1 = CandidateNames[1] + ": " + str(PercVotesCast[1]) + "% (" + str(NumVotesPerCand[1]) + ")"
Candidate2 = CandidateNames[2] + ": " + str(PercVotesCast[2]) + "% (" + str(NumVotesPerCand[2]) + ")"
Candidate3 = CandidateNames[3] + ": " + str(PercVotesCast[3]) + "% (" + str(NumVotesPerCand[3]) + ")"
WinningCand = "Winner: " + Winner


#Print to terminal
print(f'\n{Header1} \n')
print(f'{Header2} \n')
print(f'{TotalVotes} \n')
print(f'{Header2} \n')
print(f'{Candidate1} \n')
print(f'{Candidate2} \n')
print(f'{Candidate3} \n')
print(f'{Header2} \n')
print(f'{WinningCand} \n')
print(f'{Header2} \n')


#print to the text file

#Set variable for output file
output_file = os.path.join("Analysis","PyPoll.txt")

#  Open the output file
with open(output_file, "w",newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header rows
    writer.writerow([Header1])
    writer.writerow([])
    writer.writerow([Header2])
    writer.writerow([])
    # Write in data rows
    writer.writerow([TotalVotes])
    writer.writerow([])
    writer.writerow([Header2])
    writer.writerow([])
    writer.writerow([Candidate1])
    writer.writerow([])
    writer.writerow([Candidate2])
    writer.writerow([])
    writer.writerow([Candidate3])
    writer.writerow([])
    writer.writerow([Header2])
    writer.writerow([])
    writer.writerow([WinningCand])
    writer.writerow([])
    writer.writerow([Header2])
    writer.writerow([])
   

