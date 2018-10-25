import operator
num = range(1,26)
x=num[1:22:2]
y=reduce(operator.mul, x)
print "the product of 1st 10 even numbers is",y