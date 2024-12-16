
def add(a,b):
     return a+b
 
def subtract(a,b):
     return a-b

def multiply(a,b):
     return a*b


def divide(a, b):
     try:
         return a/b
     except ZeroDivisionError:
         raise ValueError("Error: Division by zero is not allowed")
     

# def calculator(operation,num1,num2):
#     try:
#         if operation == 'add':
#             print(num1+num2)
#         elif operation =='subtract':
#             print(num1-num2)
#         elif operation == 'multiply':
#             print(num1*num2)
#     except RuntimeError as error :
#         print(error)
#     # finally:
#     #     print("Program ended")

# calculator('',2,3)
# try:
#     divideTerm =divide(4,5)
#     print(divideTerm)
# except:
#     print("Error: Division function is not defined")
# finally:
#     input("enter any number")
#     print('end program')

def calculator():
    print('select an operation')
    print('1. addition')
    print('2 . Subtrection')
    print('3. Multiplicaion')
    print('4. Division')
    print('5 . Exit')
    while True:
        try:
             choice = input("Enter choice\n")
             if choice not in ['1', '2', '3', '4']:
                    raise ValueError("Invalid choice,please select valid operation")
             num1 = float(input("Enter first number\n"))
             num2 = float(input("Enter second number\n"))
             
             if choice == '1':
                 print(f"{num1} + {num2} = {add(num1, num2)}")
             elif choice == '2':
                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
             elif choice == '3':
                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
             elif choice == '4':
                    if num2 == 0:
                        raise ValueError("Cannot divide by zero")
                    print(num1/num2)
             elif choice == '5':
                 print("Exiting the program")
                 break
             else:
                raise ValueError("Invalid operation")
        except ValueError as error:
            print(error)
        except:
            print("Error: Invalid input")
        finally:
            calc =input("Operation has ended do you wish to continue(yes/no)")
            if calc == 'yes':
                continue
            else:
                print('Exiting the program')
                break
calculator()