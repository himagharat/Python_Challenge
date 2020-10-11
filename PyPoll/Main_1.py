# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:00:17 2020

@author: ghara
"""
import os
import csv

#Join Path to csv file
py_poll_csv= os.path.join('py_poll.csv')
with open(py_poll_csv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

#Define Variables
#def get_results(data):
    total_votes = 0
    votes = {}
    candidate_count = 0
    unique_candidates = []
    percent = 0
    winning_count = 0
    winning_candidate = " "
    
    #Loop through Rows
    for row in csvreader:
        total_votes += 1 
        candidate_name = row[2]
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name)
            votes[candidate_name] = 0
        votes[candidate_name]= votes[candidate_name] + 1
            
            
            #Second Loop to Populate Candidate_count w/ each vote
    for candidate in votes:
        candidate_count = votes.get(candidate)
        percent = float(candidate_count) / float(total_votes*100)
            
            #Find Winner
        #winner = unique_candidates[candidate_count.index(max(candidate_count))]
        if candidate_count > winning_count:
            winning_count = candidate_count
            winning_candidate = candidate
            
            
                #Print Statements
            
            print("Election Results")
            print("---------------")
            print(f'Total Votes: {total_votes}')
            print("---------------------")
            print("----------------")
            print(f'Winner: {winning_candidate}')
            print("-------------------------")
            summary = f'{unique_candidates}: {percent:.3f}% ({candidate_count})'
            print(summary, end= "")
        
        #set exit path
py_poll= os.path.join("PyPollResults.txt")
        
        #output to txt file
with open(py_poll, "w") as txtfile:

    voting_summary = (
            f'--------------\n'
            f'Election Results\n'
            f'---------------\n'
            f'Total Votes: {total_votes}\n'
            f'---------------------\n'
            f'----------------\n'
            f'Winner: {winning_candidate}\n'
            f'-------------------------\n'
            )              
    txtfile.write(voting_summary)
        

                  
            

                
            
                

        

    