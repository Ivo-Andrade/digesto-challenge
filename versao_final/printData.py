import json
import csv

# Prints data on console
def createConsolePrint(data):
	for index, value in enumerate(data):
		line = '|'.join(str(x).ljust(12) for x in value)
		print(line)
		if index == 0:
			print('-' * len(line))

# Saves data on a JSON file (as an array of arrays)
def createJSONFile(data, filename):
	with open(filename, 'w') as outfile:
		json.dump(data, outfile)
	print("Arquivo salvo em formato JSON em", filename)

# Saves data on a CSV file
def createCSVFile(data, filename):
	with open(filename, mode='w') as outfile:
	    csv_writer = csv.writer(outfile, delimiter=',', lineterminator = '\n')
	    for row in data:
	    	csv_writer.writerow(i for i in row)
	print("Arquivo salvo em formato CSV em", filename)