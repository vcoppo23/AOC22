import time
start = time.time()
with open("/Users/vcoppo23/Desktop/AOC22/inputs/input6.txt", "r") as file:
    stream = file.read()



for i in range(len(stream)):
    code = stream[i:i+4]
    if len(code) < 4:
        break
    code = set(code)
    if len(code) == 4:
        print (code,i+4)
        break

print('total time: ',time.time()-start)