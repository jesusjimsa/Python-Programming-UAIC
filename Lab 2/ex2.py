# Write a function that receives a list of
# numbers and returns a list of the prime
# numbers found in it.

def is_prime(a):
    return all(a % i for i in xrange(2, a))	# Check if a number is prime

def primeList(numbers):
	primes = list()

	for a in numbers:
		if is_prime(a):
			primes.append(a)
	
	primes.sort()

	return primes

print primeList([3, 76, 1234, 83, 98765, 24 ,987, 45, 77, 9376, 435, 61, 123, 8949])