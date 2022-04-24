# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular votes
# 6. create a filename variable to a direct or indirect path to the file

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
 print(election_data)
file_to_save = os.path.join("anal")
