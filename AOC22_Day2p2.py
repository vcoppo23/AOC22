with open("/Users/vcoppo23/Desktop/AOC22/inputs/input2.txt", "r") as file:
   guide = file.read()
guide = guide.splitlines()
#part 2 
score = 0
for v in range (len(guide)):
    line = []
    guide[v] = guide[v].split()
    line.append(guide[v][0])
    line.append(guide[v][1])
    if line[1] == "X": ## go for loss
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 1
        elif line[0] == "C":
            score += 2
    elif line[1] == "Y": ## go for draw
        if line[0] == "A":
            score += 4
        elif line[0] == "B":
            score += 5
        elif line[0] == "C":
            score += 6
    elif line[1] == "Z":  ## go for win
        if line[0] == "A":
            score += 8
        elif line[0] == "B":
            score += 9
        elif line[0] == "C":
            score += 7
print (score)