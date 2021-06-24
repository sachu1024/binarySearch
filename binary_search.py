def binarySearch(sorted_list, number,high,low):
	if high >= low:
		middle = low + (high - low) // 2

		if numbers[middle] == number_to_find:
			return middle
		elif numbers[middle] < number_to_find:
			return findValue(numbers, number_to_find, middle + 1, high)
		else:
			return findValue(numbers, number_to_find, low, middle - 1)
	
	else:
		return -1


sorted_list = [7, 9, 14, 22, 34]
number_to_find = 22

final = findValue(sorted_list, number_to_find, 0, len(sorted_list) - 1)

if final == -1:
	print("Nil")
else:
	print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")