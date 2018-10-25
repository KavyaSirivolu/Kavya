lst =range(1,100,2)
z=lst[0:31]
print reduce(lambda x,y : x + y, filter ( lambda x : x % 2!=0, z))
	
		