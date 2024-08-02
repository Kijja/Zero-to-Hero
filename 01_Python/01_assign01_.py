# Write a python code to count the number of words in the following song. Use conditional statement.
# Do not count words by hand and print. do not count by special chararecter such as space or '

print("Assignment+1_python")

a = 0
f = open("song.txt", "r")
lines = f.readlines()

for line in lines:

    ## List for special chararecter.
    l = ["\n", "?", "\"", ",", "'s", "'", "(", ")"]
    
    ## Remove special chararecter with For loop replace function.  
    for i in range(len(l)):        
        if l[i] == "'":
            line = line.replace(l[i], " ")
        else:
            line = line.replace(l[i], "")
            
    ## Count spec plus1 = count words by line          
    a += line.count(" ")
    a +=1 
    
## Print count words
print(a)  
