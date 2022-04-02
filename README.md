# Election_Analysis

## Overview of Election-Audit 
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who recieved votes.
3. Calculate the voter turnout for each county.
4. Calculate the total number of votes each candidate recieved.
5. Calculate the percentage of votes each candidate won. 
6. Calculate the perentage of votes from each county out of the total count.
7. Determine the winner of the election based on popular vote.
8. Determine the county with the highest turn out.

## Resources
- Data Source : election_results.csv 
- Software: Python 3.6.1, Visual Studio, 1.38.1

## Election-Audit Results  
The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The county reults were: 
  - Jefferson received 10.5% of the vote and 38,855 number of votes.
  - Denver received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe recieved 6.7% of the vote and 24,801 number of votes.
- The winning county of the election was:
  - Denever, who received 82.8% of the vote and 306,055 number of votes.
- The candidate results were: 
  - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was: 
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This script can be used for any election by doing the following:
- Make sure the new data source file holds the same format of : Ballot ID, County, Candidate 
- Reference: Line 9: file_to_load = os.path.join("Resources", "election_results.csv")
Change "election_results.csv" to the new data source. 
