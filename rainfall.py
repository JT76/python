# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:28:59 2019

@author: ucapjti
"""

import csv
import json
import matplotlib.pyplot as plt
import math

rainfall_data = {}
csv_file = "python_language_1_data.csv"
json_file = "python_language_1_json.json"

def rainfall_csv_to_json(csv_file, json_file):
    with open(csv_file, "r") as input_file:
        datareader=csv.reader(input_file)
        columns = next(datareader)
        year = 0
        for row in datareader:
            if row[0] != year:
                year=row[0]
                rainfall_data[year]=[]
            rainfall_data[year].append(float(row[2]))
        input_file.close
        with open(json_file, "w") as output_file:
            json.dump(rainfall_data, output_file, sort_keys=True, indent=4, 
                      separators=(',',': '))
        output_file.close

def rain_plot(json_file, year, colour):
    with open(json_file, "r") as input_file:
        rainfall_data = json.load(input_file)
        year_data = rainfall_data[str(year)]
    input_file.close
    plt.plot(year_data, color=colour)

def list_average(mylist):
    return sum(mylist)/len(mylist)

def rain_plot_avg(json_file, year_begin, year_end, colour):
    with open(json_file, "r") as input_file:
        rainfall_data = json.load(input_file)
    input_file.close
    x = []
    y = []
    for i in range(year_begin, year_end +1):
        x.append(i)
        y.append(list_average(rainfall_data[str(i)]))
    plt.plot(x, y, color=colour)    
    
def save_plot(json_file, year, colour):
    rain_plot(json_file, year, colour)
    plt.savefig(str(year) + "_rainfall.png")
    plt.clf()

def save_plot_avg(json_file, year_begin, year_end, colour):
    rain_plot_avg(json_file, year_begin, year_end, colour)
    plt.savefig(str(year_begin) + "_to_" + str(year_end) +
                "_rainfall.png")
    plt.clf()

rainfall_csv_to_json(csv_file, json_file)    
save_plot(json_file, 1998, 'green')
save_plot_avg(json_file, 1988, 2000, 'green')

def rain_gauge_corrector(rainfall_value):
    return (rainfall_value* 1.2)**math.sqrt(2) 

def correct_year_loop(json_file, year):
    with open(json_file, "r") as input_file:
        rainfall_data = json.load(input_file)
        new_data = []
        for value in rainfall_data[str(year)]:
            new_data.append(rain_gauge_corrector(value))
    input_file.close
    return new_data

def correct_year_comp(json_file, year):
    with open(json_file, "r") as input_file:
        rainfall_data = json.load(input_file)
        new_data = [rain_gauge_corrector(value) for value 
                    in rainfall_data[str(year)]]
    input_file.close
    return new_data

print(correct_year_loop(json_file, 1998))
print(correct_year_comp(json_file, 1998))


        