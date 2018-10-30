def find35sum(x):
	All_num = []
	for i in range(1,x+1):
		if i % 3 == 0:
			All_num.append(i)
		elif i % 5 == 0:
			All_num.append(i)
	total = sum(All_num)
	print total