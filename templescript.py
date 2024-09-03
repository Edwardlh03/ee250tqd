import sys
import math

def is_prime(n):
	"""check for primality"""
	if n<=1:
		return False
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <=n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i +=6
	return True
def main():
	if len(sys.argv) != 3:
		print("Usage: python3 templescript.py <number1> <number2>")
		sys.exit(1)

	try:
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
	except ValueError:
		print("PLease provide valid integers")
		sys.exit(1)

	sum = num1 + num2
	product = num1 * num2
	prime1 = is_prime(num1)
	prime2 = is_prime(num2)

	print(f"sum: {sum}")
	print(f"product: {product}")
	print(f"{num1} is {'prime' if prime1 else 'not a prime'} number.")
	print(f"{num2} is {'prime' if prime2 else 'not a prime'} number.")
if __name__ == "__main__":
	main()
