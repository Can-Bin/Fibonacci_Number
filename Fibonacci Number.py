def fibonacci(n) :
  if n > 1 :
    return fibonacci(n-1) + fibonacci(n-2)
  else :
    return n

fib_list = []

for i in range(11):
    fib_list.append(fibonacci(i))
print(fib_list)