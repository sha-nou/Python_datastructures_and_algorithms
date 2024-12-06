# Multiplication Table  :Case 1 Using For loop
# get user input
num = int (input('enter number'))

i = 0
for i in range(0,13):
    result = i*num
    i += 1
    print(f"{i} x{num} ={result}")

#Case:2 Using While loop

# x = int(input('choose any number to see its multiplication table'))
# a=0
# while  a <= 12:
#     b= x*a
#     print(b)
#     a = a+1
    
