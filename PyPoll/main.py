import csv

inputfile='Resources/election_data.csv'
outputfile='Resources/ElectionResults.txt'

#Empty list for csv file
Elections=[]

#Empty dictionary to record only candidate names
DictElections={}

#Empty dictionaty to summarize the total number votes per candidate name
DictSummary={}

#Open election_data file
with open(inputfile, newline='') as csvfile:
    ReadPolls=csv.reader(csvfile,delimiter=',')

    # Skip header row
    next(ReadPolls)

    text_file=open(outputfile,"w")

    # Output to text file
    text_file.write("Election Results")

    # Output to console
    print("Election Results")

    # Output to text file
    text_file.write("\n-------------------------")

    # Output to console
    print("-------------------------") 

    # Convert ReadPolls string to list 
    for line in ReadPolls:
        Elections.append(line)

    # Output to text file
    text_file.write("\nTotal Votes: "+str(len(Elections)))

    # Output to console
    print("Total Votes: "+str(len(Elections)))

    # Output to text file
    text_file.write("\n-------------------------")

    # Output to console
    print("-------------------------")

    # Convert Elections list into dictionary for counting and grouping candidate names
    for line in Elections:
        name_key=line[10]
        if name_key not in DictElections:
           # insert name_key into dictionary and initialize to 0
            DictElections[name_key]=0
        # count the name key inside dictionary
        DictElections[name_key]+=1
    
    # Compute the percentages of each name key of DictElections and insert into DictSummary
    total_Elections=len(Elections)
    for name in DictElections:
        DictSummary[name]=round((DictElections[name]/total_Elections)*100)
        # Output to text file
        text_file.write("\n"+str(name)+": "+str(DictSummary[name])+"% "+"("+str(DictElections[name])+")")
        # Output to console
        print(str(name)+": "+str(DictSummary[name])+"% "+"("+str(DictElections[name])+")")
        
    # Initialize the highest value to comapre
    highest=0
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    for name in DictSummary:
        if highest < DictSummary[name]:
            highest=DictSummary[name]
            winner=name
            
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    # Output to text file
    text_file.write("\nWinner: "+winner)
    # Output to console
    print("Winner: "+winner)
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    
# Close text file
text_file.close()