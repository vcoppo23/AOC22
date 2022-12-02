with open("/Users/vcoppo23/Desktop/AOC22/inputs/input2.txt", "r") as file:
   guide = file.read()

values = guide.replace("A","1").replace("B","2").replace("C","3").replace("X","1").replace("Y","2").replace("Z","3")

guide = guide.splitlines()
values = values.splitlines()

#part 1
score = 0
for i in range(len(guide)):
    line = []
    guide[i] = guide[i].split()
    values[i] = values[i].split()

    line.append(guide[i][0])
    line.append(guide[i][1])
    
    if (line[0] == "A" and line[1] == "X") or (line[0] == "B" and line[1] == "Y") or (line[0] == "C" and line[1] == "Z"):
        score += 3 + int(values[i][1])
    elif (line[0] == "A" and line[1] == "Y") or (line[0] == "B" and line[1] == "Z") or (line[0] == "C" and line[1] == "X"):
        score += 6 + int(values[i][1])
    elif (line[0] == "A" and line[1] == "Z") or (line[0] == "B" and line[1] == "X") or (line[0] == "C" and line[1] == "Y"):
        score += 0 +  int(values[i][1])
    
print(score)
