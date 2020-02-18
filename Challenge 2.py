import csv
import os

csvpath = os.path.join('C:/Users/rajka/Desktop/UofT/Assignments/Instructions/PyPoll/Resources/election_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    csvheader = next(csvreader)

    listcsv = list(csvreader)
    
    unique_candidates = []

    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    votes = []

    for row in listcsv:
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        if row[2] == unique_candidates[0]:
            khan_votes += 1
            votes.append(row[2])
        elif row[2] == unique_candidates[1]:
            correy_votes += 1
            votes.append(row[2])
        elif row[2] == unique_candidates[2]:
            li_votes += 1
            votes.append(row[2])
        else:
            otooley_votes += 1
            votes.append(row[2])

    if max(khan_votes,correy_votes,li_votes,otooley_votes) == votes.count('Khan'):
        winner = "Khan"
    elif max(khan_votes,correy_votes,li_votes,otooley_votes) == votes.count('Correy'):
        winner = "Correy"
    elif max(khan_votes,correy_votes,li_votes,otooley_votes) == votes.count('li'):
        winner = "Li"
    else:
        winner = "O'Tooley"

    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {len(listcsv)}")
    print("--------------------------------")
    print(f"{unique_candidates[0]}: {round((khan_votes/len(listcsv)*100),3)}00% ({khan_votes})")
    print(f"{unique_candidates[1]}: {round((correy_votes/len(listcsv)*100),3)}00% ({correy_votes})")
    print(f"{unique_candidates[2]}: {round((li_votes/len(listcsv)*100),3)}00% ({li_votes})")
    print(f"{unique_candidates[3]}: {round((otooley_votes/len(listcsv)*100),3)}00% ({otooley_votes})")
    print("--------------------------------")
    print(f"Winner: {winner}")
    print("--------------------------------")


output_file = os.path.join('C:/Users/rajka/Desktop/UofT/Assignments/Instructions/PyPoll/Output/Election Results.txt')

with open(output_file,'w') as report:
   report.write("Election Results\n")
   report.write("------------------------------\n")
   report.write(str(f"Total Votes: {len(listcsv)} \n"))
   report.write("------------------------------\n")
   report.write(str(f"{unique_candidates[0]}: {round((khan_votes/len(listcsv)*100),3)}00% ({khan_votes})\n"))
   report.write(str(f"{unique_candidates[1]}: {round((correy_votes/len(listcsv)*100),3)}00% ({correy_votes})\n"))
   report.write(str(f"{unique_candidates[2]}: {round((li_votes/len(listcsv)*100),3)}00% ({li_votes})\n"))
   report.write(str(f"{unique_candidates[3]}: {round((otooley_votes/len(listcsv)*100),3)}00% ({otooley_votes})\n"))
   report.write("------------------------------\n")
   report.write(str(f"Winner: {winner}\n"))
   report.write("------------------------------")