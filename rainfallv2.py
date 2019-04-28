import csv
import json
import matplotlib.pyplot as plt

csv_file = 'python_language_1_data.csv'
json_file = 'python_language_1_jsondata.json'


def save_csv_to_json(csv_file, json_file):
    raindatadict = {}
    with open(csv_file, 'r') as input_file:
        raindata=csv.reader(input_file)
        next(raindata)
        for year, day, rainfall in raindata:
            try:
                raindatadict[year].append(float(rainfall))
            except:
                raindatadict[year] = [float(rainfall)]
    input_file.close
    with open(json_file, 'w') as output_file:
        json.dump(raindatadict, output_file, indent=4)
    output_file.close

save_csv_to_json(csv_file, json_file)

def plot_year(json_file, year, colour='green'):
    with open(json_file, 'r') as input_file:
        raindatadict = json.load(input_file)
    input_file.close
    plt.plot(raindatadict[str(year)], color=colour)
    plt.xlabel('days')
    plt.ylabel('rainfall (mm)')
    plt.title('Daily rainfall in ' + str(year))
    plt.savefig('rainfall_' + str(year) +'.png')
    #plt.show()
    plt.clf()

plot_year(json_file, 1998)

def list_mean(mylist):
    return float(sum(mylist))/len(mylist)

def plot_mean(json_file, year_begin, year_end, colour='green'):
    with open(json_file, 'r') as input_file:
        raindatadict = json.load(input_file)
    input_file.close
    year_list = []
    raindata_list = []
    for year in range(year_begin, year_end+1):
        year_list.append(str(year))
        raindata_list.append(list_mean(raindatadict[str(year)]))
    plt.plot(year_list, raindata_list, color=colour)
    plt.xlabel('year')
    plt.ylabel('Average daily rainfall (mm)')
    plt.title('Average daily rainfall from ' 
              + str(year_begin) + ' to ' + str(year_end))
    plt.savefig('rainfall_' + str(year_begin) + '_' + str(year_end) + '.png')
    plt.show()
    plt.clf()

plot_mean(json_file, 1988, 2000, colour='green')

def corrector(value):
    return value*(1.2**(1./2.))

def apply_correction_loop(json_file, year):
    with open(json_file, 'r') as input_file:
        raindatadict = json.load(input_file)
    input_file.close
    new_data = []
    for value in raindatadict[str(year)]:
        new_data.append(corrector(value))
    return new_data 

def apply_correction_comp(json_file, year):
    with open(json_file, 'r') as input_file:
        raindatadict = json.load(input_file)
    input_file.close
    new_data = [corrector(value) for value in rainfall_data[str(year)]
    return new_data



