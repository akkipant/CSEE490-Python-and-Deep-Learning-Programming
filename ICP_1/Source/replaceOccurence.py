Str = 'python python python hello world'

listStr = Str.split()
newStr = ''
print(listStr)
for x in listStr:
    if x == 'python':
        newStr += 'pythons'
    else:
        newStr += x
    newStr += ' '
print(newStr)
