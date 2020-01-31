N = int(input("Enter Number of students : "))
lbsWeight = list()
kgWeight = list()
for x in range(N):
    lbsWeight.append(int(input("Enter Weight for student " + str(x+1) + " : ")))       # Take input

for x in lbsWeight:
    kgWeight.append(x * 0.454)      # Calculate weights
print(kgWeight)