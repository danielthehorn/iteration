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