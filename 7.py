from random import shuffle

def find_median(numbers):
	n = len(numbers)
	if n == 0:
		return None
	if n == 1:
		return numbers[0]

	# Shuffle the list to ensure a random ordering
	shuffle(numbers)

	# Find the median by selecting the middle element
	return numbers[n // 2]

# Example usage
print(find_median([1, 2, 3, 4, 5])) # Output: 3
print(find_median([1, 2, 3, 4, 5, 6])) # Output: 3 or 4 (randomly chosen)
print(find_median([])) # Output: None
print(find_median([7])) # Output: 7
