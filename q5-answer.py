def check_divisibility(num, divisor):
	if divisor == 0:
        	raise ValueError("Division by zero is not allowed")
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10,2))
#True

print(check_divisibility(7,3))
#False