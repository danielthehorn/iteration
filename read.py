#!/usr/bin/env python
import sys
import plotly
import plotly.graph_objs as go

data = open("jobs.csv", 'r')
lines = data.readlines()

user_id = []
income = []
age = []
department = []
college_years = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",") # [Bird, 88, Poland]
	user_id.append(info[0])
	income.append(info[1])
	age.append(info[2])
	department.append(info[3])
	college_years.append(info[4])

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

#print most_popular_color(car_colors)

def most_popular_color_dictionary(colors):
	color_dict = {}
	for color in colors:
		color_exist = color_dict.get(color, None)
		if not color_exist:
			color_dict[color] = 1
		else:
			color_dict[color] += 1
	current_largest = 0
	largest_one = ""
	for color_name, color_count in color_dict.items():
		if color_count > current_largest:
			largest_one = color_name
			current_largest = color_count
	return largest_one

#print most_popular_color_dictionary(car_colors)

# animals = ['giraffes', 'orangutans', 'monkeys']
# animal_counts = [20, 14, 23]

# data = [go.Bar(
# 			x = animals,
# 			y = animal_counts
# 	)]

# plotly.offline.plot(data, filename='basic-bar')

def colors_graph(colors):
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
	data = [go.Bar(
			x = color_list,
			y = color_counts,
			marker=dict(
				color=['rgba(240,230,140,0.8)', 'rgba(75,0,130,0.8)',
				'rgba(105,25,25,0.8)', 'rgba(238,130,238,0.8)',
				'rgba(218,165,32,0.8)', 'rgba(64,224,208,0.8)',
				'rgba(128,0,0,0.8)', 'rgba(225,192,203,0.8)',
				'rgba(145,95,109,0.8)', 'rgba(128,0,128,0.8)',
				'rgba(0,128,128,0.8)', 'rgba(127,255,212,0.8)',
				'rgba(255,255,0,0.8)', 'rgba(255,0,0,0.8)',
				'rgba(255,165,0,0.8)', 'rgba(0,128,0,0.8)',
				'rgba(0,0,255,0.8)', 'rgba(220,20,60,0.8)',
				'rgba(255,192,203,0.8)'])
		)]
	plotly.offline.plot(data, filename='car-colors')

#colors_graph(car_colors)

def years_graph(years):
	year_list = []
	year_counts = []
	for year in years:
		if not list_contains(year_list, year):
			year_list.append(year)
			year_counts.append(1)
		else:
			for i in range(0,len(year_list)):
				if year_list[i] == year:
					year_counts[i] += 1
	data = [go.Bar(
			x = year_list,
			y = year_counts
		)]
	plotly.offline.plot(data, filename='car-years')

#years_graph(car_years)

def scatter_plot(xvar, yvar):
	data = [go.Scatter(
		x = xvar,
		y = yvar,
		mode = 'markers'
	)]

	plotly.offline.plot(data, filename='scatterplot')

#scatter_plot(age, income)

def pie_chart(inputs):
	labels = []
	values = []
	for value in inputs:
		if not list_contains(labels, value):
			labels.append(value)
			values.append(1)
		else:
			for i in range(0,len(labels)):
				if labels[i] == value:
					values[i] += 1
	data = [go.Pie(labels=labels, values=values)]

	plotly.offline.plot(data, filename='piechart')

#pie_chart(department)

def line_plot(xvar, yvar):
	data = [go.Scatter(
		x = xvar,
		y = yvar
	)]

	plotly.offline.plot(data, filename='lineplot')

line_plot(user_id, income)