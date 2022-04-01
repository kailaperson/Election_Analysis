# Election_Analysis

## Project Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source : election_results.csv 
- Software: Python 3.6.1, Visual Studio, 1.38.1

## Summary 
The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham 
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was: 
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview 
The election commission has requested the following additional data to complete the audit.

1. Calculate the voter turnout for each county.
2. Calculate the perentage of votes from each county out of the total count.
3. Determine the county with the highest turn out.

## Challenge Audit Results ##Use images or examples of your code as support where necessary.
The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The counties were: 
  - Jefferson
  - Denver
  - Arapahoe
- The county reults were: 
  - Jefferson received 10.5% of the vote and 38,855 number of votes.
  - Denver received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe recieved 6.7% of the vote and 24,801 number of votes.
- The winning county of the election was: 
  - Denever, who received 82.8% of the vote and 306,055 number of votes.

## Challenge Summary
This script can be used for any election by doing the following:
- Make sure the new data source file holds the same format of : Ballot ID, County, Candidate 
- Line 9: file_to_load = os.path.join("Resources", "election_results.csv")
Change "Resources" to the appropiate folder and change "election_results.csv" to the new data source. 
