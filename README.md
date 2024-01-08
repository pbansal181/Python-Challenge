# Python-Challenge
In this Challenge we need to create 2 python scripts for calculating Financial and Election summary for data given.
There are 2 Files to be created:
PyBank Details
In this data there are 2 columns named as "Date" and "Profit/Losses".
The task is calculating the below values:
•The total number of months included in the dataset(This can be calculated using a list and adding 1 everytime as we iterate through all rows when we find a new value and then getting the length of it)
•The net total amount of "Profit/Losses" over the entire period(This is calculated by adding the value of 2nd column to a list variable as we iterate through row and finally getting sum of it)
•The changes in "Profit/Losses" over the entire period, and then the average of those changes(Change can be find out going in loop and getting difference of 1st and next entry. Average can be find out as divison of summing and length of the changes)
•The greatest increase in profits (date and amount) over the entire period(Can be find out using max function)
•The greatest decrease in profits (date and amount) over the entire period(can be found out using min function)

PyPoll Details
This dataset is composed of three columns: "Voter ID", "County", and "Candidate"
The task is to calculate below values:
•The total number of votes cast(It can be calculated by getting length of the column)
•A complete list of candidates who received votes(creating a list with counting candidate from 3rd column) 	
•The percentage of votes each candidate won(Percentage can be calculated using formula [candidate’s vote/total votes] *100)
•The total number of votes each candidate won( putting a counter for each candidate and then counting occurence)
•The winner of the election based on popular vote(For this we need to sort the candidate’s list in descending order and then fetching the first entry)
