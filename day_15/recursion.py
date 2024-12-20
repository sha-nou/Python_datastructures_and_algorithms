# def countdown(n):
#     print(n)
#     if n == 0:
#         return
#     else:
#         countdown(n-1)

# countdown(6)


# def factorial(n):
#     print(n)
#     if n<=1:
#         return 
#     else:
#         n * factorial(n-1)

# factorial(6)

# def factorial(n):
#      return_value = 1
#      for i in range(2, n + 1):
#        return_value *= i
#      return return_value


# factorial(4)
from functools import reduce
def factorial(n):
  return reduce(lambda x, y: x * y, range(1, n + 1) or [1])


print(factorial(4))

def fibonacci():
  n=input('enter a number')
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_sequence = [0, 1]
    for i in range(2, n):
      fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(fibonacci(6))
