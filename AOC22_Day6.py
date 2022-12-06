import time
start = time.time()
with open("/Users/vcoppo23/Desktop/AOC22/inputs/input6.txt", "r") as file:
    stream = file.read()



for i in range(len(stream)):
    ##makes code a substrting of stream 4 characters long
    code = stream[i:i+4]
    ##makes code a set, which removes duplicates
    code = set(code)
    ## Checking if any duplicates were removed
    if len(code) == 4:
        ##if no duplicates were removed, then the code is the answer
        print (code,i+4)
        break

print('total time: ',time.time()-start)