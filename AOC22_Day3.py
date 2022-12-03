with open("/Users/vcoppo23/Desktop/AOC22/inputs/input3.txt", "r") as file:
   input = file.read()
input = input.splitlines()
dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
score = 0
for rucksack in input:
    rucksize = int(len(rucksack))
    compart1 = rucksack[0:rucksize//2]
    compart2 = rucksack[rucksize//2:rucksize]
    compart1 = set(compart1)
    compart2 = set(compart2)
    
    score += dict.index(next(iter(set(compart1).intersection(compart2))))+1
print(score)

