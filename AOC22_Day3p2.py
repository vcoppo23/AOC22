with open("/Users/vcoppo23/Desktop/AOC22/inputs/input3.txt", "r") as file:
    input = file.read()
import time
start = time.time()
input = input.splitlines()
dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
score = 0

input = [input[i:i+3] for i in range(0, len(input), 3)]
for rucksack in input:
    rucksack1 = set(rucksack[0])
    rucksack2 = set(rucksack[1])
    rucksack3 = set(rucksack[2])
    score += dict.index(next(iter(set(rucksack1).intersection(rucksack2).intersection(rucksack3))))+1
print(score)
print('total time: ',time.time()-start)
print ("faster than gabe's")
