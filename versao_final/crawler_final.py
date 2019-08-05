import sys
import csv
from extractData import extractData
from requestData import requestPageData
from printData import createConsolePrint, createJSONFile, createCSVFile

#############################################
### FUNCTIONS
#############################################

# Retrives website xpath and variable data
def initWebsiteObjects(filename):
	websites = []
	try:
		with open(filename) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			next(csv_reader)
			for row in csv_reader:
				websites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
	except IOError:
		print(filename, " não pode ser encontrado para inicializar o programa!")
	if not websites:
		print("Não existem dados em ", filename)
	return websites

# Closes app if cmd line argument is unsupported
def argumentoIncorreto(args):
	print("Argumento incorreto:", args, ". Argumentos disponíveis: --print, --save_json, --save_csv, --websiteDBFilename, --websiteList.")
	exit()

# Prints data
def printData(data, handle, name):
	if data != []:
		print("\nCloud Computing Services at", name, ":")
		if print_default or (['--print', True] in printArgs):
			createConsolePrint(data)
		if print_default or (['--save_json', True] in printArgs):
			filename = handle + '_json.txt'
			createJSONFile(data, filename)
		if print_default or (['--save_csv', True] in printArgs):
			filename = handle + '.csv'
			createCSVFile(data, filename)
	else:
		print("Dados não puderam ser extraidos!")

#############################################
### CLASSES
#############################################

class Website:
	def __init__(self, name, handle, url, xpathCpu, xpathMemory, xpathStorage, xpathBandwidth, xpathPrice):
		self.name = name
		self.handle = handle
		self.url = url
		self.xpaths = [xpathCpu, xpathMemory, xpathStorage, xpathBandwidth, xpathPrice]

#############################################
### GLOBAL
#############################################

# 	website xpaths database filename variables
changeFilename = False
websitesFilename = '../websitelist.csv'

#	website xpaths database variables
websites_default = True
websites_handles = []

# 	print variables
print_default = True
printArgs = []
printArgs.append(['--print', False])
printArgs.append(['--save_json', False])
printArgs.append(['--save_csv', False])


# sys.argv treatment
for indexArgs, args in enumerate(sys.argv[1:]):
	if not args.startswith('--'):
		if changeFilename:
			websitesFilename = args
			changeFilename = False
			continue
		if not websites_default:
			websites_handles.append(args)
		else:
			argumentoIncorreto(args)
	elif [args, False] in printArgs:
		index = printArgs.index([args, False])
		printArgs[index] = [args, True]
		print_default = False
	elif args == '--websiteList':
		websites_default = False
	elif args == '--websiteDBFilename':
		changeFilename = True
	else:
		argumentoIncorreto(args)

# initializing website xpath database
websitesDB = initWebsiteObjects(websitesFilename)
website_list = []

if websites_default:
	for site in websitesDB:
		website_list.append(site)
else:
	for handle in websites_handles:
		for site in websitesDB:
			if handle == site.handle:
				website_list.append(site)
				break

for site in website_list:

	# print('Making request to vultr.com...')
	htmlRequest = requestPageData(site.url)
	# print('Request complete!')
	# print('Acquiring table data...')
	# data_digitalocean = extractDataDigitalOcean(htmlRequest, xpaths)
	data = extractData(htmlRequest, site.xpaths)
	# print('Data acquired!')

	# print('Displaying data...')
	printData(data, site.handle, site.name)