#basic file handling synatx
f = open("funny.txt","r")

for line in f:
    print(line)
f.close()

# with open("funny.txt","r") as f:

with open("funny.txt","r") as f:
    for line in f:
        print(line)
    
# using readlines
with open("funny.txt","r") as f:
    lines = f.readlines()
    print(lines)
    
#write file
with open("love1.txt","w") as f:
    f.write("This is a funny file 1") 
    
#write file & append
with open("love1.txt","a") as f:
    f.write("This is a funny file 2") 
    
#write file & append & next line
with open("love1.txt","a") as f:
    f.write("\nThis is a funny file 3") 
    
#write line
with open("love2.txt","w") as f:
    f.writelines(["This is a funny file 1\n","This is a funny file 2\n","This is a funny file 3\n"])
    

#read player list from file & create list to find players min & max score
player_score = {}
with open("scores.csv", "r") as f:
    for line in f:
        player , score = line.split(",")
        score = int(score)
        
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player] = [score]
            
print(player_score)

for player , score_list in player_score.items():
    print(f"{player} -> Min Score : {min(score_list)} & Max Score : {max(score_list)}")
    
#give me similer example to practice
#read player list from file & create list to find players min & max score
