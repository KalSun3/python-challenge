#import
import os
import csv

#path
PyPoll = os.path.join('Resources', 'election_data.csv')
Output = os.path.join("analysis","output.txt")


#variables
TotalVotes = 0
CandidateOptions = []
CandidateVotes = {}
WinningCandidate = ""
WinningCount = 0

with open(PyPoll) as csvfile:
    PyPollReader = csv.DictReader(csvfile)
    PyPollHeader = next(PyPollReader)


    for row in PyPollReader:
            #Get total vote count
            TotalVotes += 1
            # Get candidate name from row
            CandidateName = row["Candidate"]

            if CandidateName not in CandidateOptions:
                  CandidateOptions.append(CandidateName)
                  CandidateVotes[CandidateName] = 0
            CandidateVotes[CandidateName] = CandidateVotes[CandidateName] + 1
with open(Output, "w") as txt_file:
    ElectionResults = (
         f'\n\nElection Results\n'
         f'-----------------------\n'
         f'Total Votes: {TotalVotes}\n'
         f'------------------------\n'
         )
    print(ElectionResults)  
    txt_file.write(ElectionResults)
   

    for Candidate in CandidateVotes:
        Votes = CandidateVotes.get(Candidate)
        VotePercentage = float(Votes) / float(TotalVotes) * 100
        if (Votes > WinningCount):
            WinningCount = Votes
            WinningCandidate = Candidate
        #print(PyPollHeader)
        VoterOutput = (f'{Candidate}: {VotePercentage:.3f}% ({Votes})\n')
        print(VoterOutput)
        txt_file.write(VoterOutput)
    WinningResults = (
         f'------------------\n'
         f'Winner: {WinningCandidate}\n'
         f'----------------------\n'
    )
    print(WinningResults)
    txt_file.write(WinningResults)


