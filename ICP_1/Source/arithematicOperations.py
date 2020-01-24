# Get value of variables
x = int(input('Enter Operand 1 : '))
y = int(input('Enter Operand 2 : '))

# Get type of operator
operator = input('Enter Operator : ')

# Get  the answer
if operator == '+':
    answer = x + y
    print('Sum :', answer)
elif operator == '-':
    answer = x - y
    print('Difference :', answer)
elif operator == '*':
    answer = x * y
    print('Product :', answer)
elif operator == '/':
    answer = x / y
    print('Division :', answer)
elif operator == '**':
    answer = x ** y
    print('Exponent :', answer)
elif operator == '%':
    answer = x % y
    print('Modulus :', answer)
else:
    print('Try Again')

