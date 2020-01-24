Str = input("Enter Number : ")
origNum = int(Str)
newNum = 0
for x in Str:
    newNum += pow(int(x), 3)

if origNum == newNum:
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')