#!/usr/bin/env python
import sys

data = open("cars.csv", 'r')
lines = data.readlines()

car_makes = []
car_models = []
car_years = []
car_colors = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",") # [Bird, 88, Poland]
	car_makes.append(info[1])
	car_models.append(info[2])
	car_years.append(info[3])
	car_colors.append(info[4])

def list_all_cars_from_year(makes, models, years, target_string):
	output = []
	for i in range(0, len(years)):
		if years[i] == target_string:
			new_thing = makes[i] + ' ' + models[i]
			output.append(new_thing)

	return output

#print list_all_cars_from_year(car_makes, car_models, car_years, "2006")

def count_cars_by_maker_since_year(makes, years, target_make, after_year):
	count = 0
	for i in range(0, len(makes)):
		if makes[i] == target_make:
			current_year = int(years[i])
			if current_year > after_year:
				count += 1

	return count

#print count_cars_by_maker_since_year(car_makes, car_years, "Toyota", 2000)

def most_popular_color(colors):
	color_list = []
	color_counts = []
	for color in colors:
		if not list_contains(color_list, color):
			color_list.append(color)
			color_counts.append(1)
		else:
			for i in range(0,len(color_list)):
				if color_list[i] == color:
					color_counts[i] += 1
	current_largest = color_counts[0]
	largest_position = 0
	for i in range(1, len(color_counts)):
		if current_largest < color_counts[i]:
			current_largest = color_counts[i]
			largest_position = i
	return color_list[largest_position]

def list_contains(values, target):
	for value in values:
		if value == target:
			return True
	return False

print most_popular_color(car_colors)