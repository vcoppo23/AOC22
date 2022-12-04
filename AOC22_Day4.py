import time
with open("/Users/vcoppo23/Desktop/AOC22/inputs/input4.txt", "r") as file:
    input = file.read().splitlines()


start = time.time()
contains = 0


for lines in input:
    lines = lines.split(",")
    elf1 = lines[0].split("-")
    elf2 = lines[1].split("-")
    #Creates two ranges of numbers for each elf as sets, 
    elf1 = set(range(int(elf1[0]), int(elf1[1])+1))
    elf2 = set(range(int(elf2[0]), int(elf2[1])+1))
    #Checks if the intersection of the two sets contains one of the other sets in whole
    if elf1.intersection(elf2) == elf1:
        contains += 1
    elif elf1.intersection(elf2) == elf2:
        contains += 1
        

print (contains)
print('total time: ',time.time()-start)
