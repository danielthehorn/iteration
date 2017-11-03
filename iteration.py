import math
# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	# standard for loop with range
	for i in range(0, len(list)):
	 	list[i] += 1

	return list


def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exclude a calculation from list members
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in range(0, len(numbers)):
		if n > current_max:
			current_max = n

	return current_max

def alternating_sum(numbers):
	current_total = numbers[0]
	for n in range(1, len(numbers)):
		if n % 2 == 0:
			current_total -= numbers[n]
		else:
			current_total += numbers[n]
	return current_total

def sum_outside(numbers, minimum, maximum):
	current_total = 0
	for n in range(0, len(numbers)):
		if n >= minimum - 1 and n < maximum - 1:
			t = True
		else:
			current_total += numbers[n]
	return current_total

def count_close_remainders(numbers, divisor):
	count = 0
	for n in range(0, len(numbers)):
		rem = numbers[n] % divisor
		if rem == divisor - 1 or rem == 0 or rem == 1:
			count += 1
	return count

def double_down(numbers, target):
	output = []
	previous_number = numbers[0]
	for n in range(0, len(numbers)):
		diff = numbers[n] - target
		if diff >= -3 and diff <= 3:
			output.append(numbers[n] * 2)
		elif previous_number > numbers[n]:
			output.append(numbers[n] * 2)
		else:
			output.append(numbers[n])
		previous_number = numbers[n]
	return output

def average(scores):
	total = float(sum(scores))
	amount = float(len(scores))
	av = total / amount
	return av

def average_drop_lowest_two(scores):
	if scores[0] > scores[1]:
		lowest = scores[1]
		next_lowest = scores[0]
	else:
		lowest = scores[0]
		next_lowest = scores[1]
	for n in scores:
		if scores[n] < lowest:
			next_lowest = lowest
			lowest = scores[n]
		elif scores[n] < next_lowest:
			next_lowest = scores[n]
	total = float(sum(scores) - lowest - next_lowest)
	amount = float(len(scores) - 2)
	av = total / amount
	return av

def standard_deviation(numbers):
	av = average(numbers)
	total_diff = float(0)
	for n in range(0, len(numbers)):
		diff = float(numbers[n]) - av
		squared_diff = diff * diff
		total_diff += squared_diff
	variance = total_diff / len(numbers)
	stdev = math.sqrt(variance)
	return stdev

def mountain_count(numbers):
	count = 0
	for n in range(1, len(numbers-1)):
		prev_num = numbers[n - 1]
		next_num = numbers[n + 1]
		if prev_num < numbers[n] and next_num < numbers[n]:
			count += 1
	return count
