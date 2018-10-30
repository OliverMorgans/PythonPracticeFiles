#returns the sum of num1 and num 2

def add(num1, num2):
	return num1 + num2
	
def divide(num1, num2):
	return num1 / num2

def multiply(num1, num2):
	return num1 * num2

def minus (num1, num2):
	return num1 - num2
#*,-,/

def main():
	operation = input("what do you want to do? (+-*/): ")
	if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
		#invalid operation 
		print("You must enter a valid operation (+-*/)")
	else:
		num1 = int(input("Enter num1: "))
		num2 = int(input("Enter num2: "))
		if(operation == "+"):
			print(add(num1, num2))
		elif(operation == "-"):
			print(minus(num1, num2))
		elif(operation == "*"):
			print(multiply(num1, num2))
		elif(operation == "/"):
			print(divide(num1, num2))	

main()

	
