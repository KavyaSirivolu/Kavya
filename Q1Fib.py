fib = lambda n: n if n<=1 else fib(n-1)**3+fib(n-2)**3

for i in range(6):
	print(fib(i))