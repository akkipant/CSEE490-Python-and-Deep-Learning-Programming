rfile = open('sample.txt', 'r')     # Open file in read mode
data = rfile.read()     # Read data from file
countDic = dict()

for x in data.split():
    if x not in countDic:
        countDic[x] = 1
    else:
        countDic[x] += 1

wfile = open('output.txt', 'w')     # Open file in write mode
for x in countDic:
    wfile.write(x + ' : ' + str(countDic[x]) + '\n')        # Write data to file
