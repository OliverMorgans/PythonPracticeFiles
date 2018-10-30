def EvenFibonacciSum(SumRange):
	Num_list = [1]
	x = 1
	y = 2
	total = 3
	while x < SumRange:
		x = y
		y = x + y
		if x % 2 == 0:
			num_list.append(x)
	
	return sum(Num_list)
		
print EvenFibonacciSum(4000000)