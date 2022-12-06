
with open("/Users/vcoppo23/Desktop/AOC22/inputs/input6.txt", "r") as file:
    stream = file.read()



for i in range(len(stream)):
    code = stream[i:i+14]
    if len(code) < 14:
        break
    code = set(code)
    if len(code) == 14:
        print (code,i+14)
        break