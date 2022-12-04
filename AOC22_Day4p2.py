import time
with open("/Users/vcoppo23/Desktop/AOC22/inputs/input4.txt", "r") as file:
    input = file.read().splitlines()


start = time.time()
contains = 0


for lines in input:
    lines = lines.split(",")
    elf1 = lines[0].split("-")
    elf2 = lines[1].split("-")
    elf1 = set(range(int(elf1[0]), int(elf1[1])+1))
    elf2 = set(range(int(elf2[0]), int(elf2[1])+1))
    ## only change in this one is that it checks if there's an empty set (no overlap), instead of checking for full overlap
    if elf1.intersection(elf2) != set():
        contains += 1
    elif elf1.intersection(elf2) != set():
        contains += 1
        

print (contains)
print('total time: ',time.time()-start)

