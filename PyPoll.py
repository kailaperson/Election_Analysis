import csv 
import os 

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to save to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Intialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

#Declare an empty dictionary
candidate_votes = {} 

#Winning Candidate and Winning Count Tracker
winning_candidate = " "
winning_count = 0 
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row 
    headers = next(file_reader)

    #Print each row in the CSV file 
    for row in file_reader:
        total_votes +=1 

        #print candidate name from each row
        candidate_name = row[2] 

        #IF candiate does not match any existing candidate
        if candidate_name not in candidate_options:

            #add candiate name to the candidate list
            candidate_options.append(candidate_name) 

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file
with open(file_to_save, "w") as txt_file: 
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes
    for candidate_name in candidate_votes: 
        # Retrive vote count of candidate 
        votes = candidate_votes[candidate_name]

        #Calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
        print(candidate_results)
        txt_file.write(candidate_results) 

        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name 

# Print the winning candidates results to the terminal
winning_candidate_summary = (
     f"----------------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-----------------------------------\n")
# print(winning_candidate_summary) 