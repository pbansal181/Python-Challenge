import os
import csv

#Reading the election data from csv file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#set path for output file
text_file = os.path.join("Analysis", "Election_summary.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader)
    
    #finding total number of candidate's names
    total_candidates = [row[2] for row in csvreader]

#Finding total number of votes cast
total_votes = len(total_candidates)

#create a new list with all candidates and number of votes associated with each
candidate_details = [[candidate, total_candidates.count(candidate)] for candidate in set(total_candidates)]

#sort the list in descending order to find the 1st entry as winner and create new sorted list
# using sorted() so that original list doesn't change and returns the sorted list.
candidate_details = sorted(candidate_details, key=lambda candidate:candidate[1], reverse= True)

#printing the results
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for candidate in candidate_details:
    percentage = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percentage:.3f}% ({candidate[1]})')
print("---------------------------------")
print(f"Winner: {candidate_details[0][0]}")
print("---------------------------------")

#Copying the results in output file
with open(text_file, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------\n")
    for candidate in candidate_details:
        percentage = (candidate[1] / total_votes) * 100
        file.write(f"{candidate[0]}: {percentage:.3f}% ({candidate[1]})\n")
    file.write("---------------------------------\n")
    file.write(f"Winner: {candidate_details[0][0]}\n")
    file.write("---------------------------------")

         