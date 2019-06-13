import csv

inputfile='Resources/election_data2.csv'
outputfile='Resources/ElectionResults.txt'

#Empty list for csv file
Elections=[]

#Empty dictionary to record only candidate names
DictElections={}

#Empty dictionaty to summarize the total number votes per candidate name
DictSummary={}

#Open election_data file
with open(inputfile, newline='') as csvfile:
    ReadPolls=csv.reader(csvfile, delimiter=',')

    next(ReadPolls) # Skip header row

    text_file=open(outputfile,"w")

    text_file.write("Election Results")  # Output to text file
    print("Election Results")  # Output to console
    text_file.write("\n-------------------------") # Output to text file
    print("-------------------------") # Output to console

    # Convert ReadPolls string to list 
    for line in ReadPolls:
        Elections.append(line)

    text_file.write("\nTotal Votes: "+str(len(Elections))) # Output to text file
    print("Total Votes: "+str(len(Elections))) # Output to console
    text_file.write("\n-------------------------") # Output to text file
    print("-------------------------") # Output to console

    # Convert Elections list into dictionary for counting and grouping candidate names
    for line2 in Elections:
       # print(line2[0])
        name_key=line2[2]
        if name_key not in DictElections:
           # insert name_key into dictionary and initialize to 0
            DictElections[name_key]=0
        # count the name key inside dictionary
        DictElections[name_key]+=1
    
    # Compute the percentages of each name key of DictElections and insert into DictSummary
    total_Elections=len(Elections)
    for name in DictElections:
        DictSummary[name]=round((DictElections[name]/total_Elections)*100)
        
        text_file.write("\n"+str(name)+": "+str(DictSummary[name])+"% "+"("+str(DictElections[name])+")")   # Output to text file
        print(str(name)+": "+str(DictSummary[name])+"% "+"("+str(DictElections[name])+")")  # Output to console
        
    # Initialize the highest value to comapre
    highest=0
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    for name in DictSummary:
        if highest < DictSummary[name]:
            highest=DictSummary[name]
            winner=name
            
    text_file.write("\n-------------------------")  # Output to text file
    print("-------------------------")  # Output to console
    text_file.write("\nWinner: "+winner) # Output to text file
    print("Winner: "+winner)    # Output to console
    text_file.write("\n-------------------------")  # Output to text file
    print("-------------------------")  # Output to console
    
# Close text file
text_file.close()