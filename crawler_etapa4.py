import requests
from lxml import html
import sys
import json
import csv

#     ETAPA 4: 2 páginas-alvo
# A quarta etapa exige que você extraia as informações também da página-alvo 2, tendo as mesmas funcionalidades da etapa anterior.

print("ETAPA 4: 2 páginas-alvo")

# launch proprierty variables
console_print = False
save_json = False
save_csv = False

# sys.argv treatment
for args in sys.argv[1:]:
	if args == '--print':
		console_print = True
	elif args == '--save_json':
		save_json = True
	elif args == '--save_csv':
		save_csv = True
	else:
		print("Argumento incorreto:", args, ". Arhgumentos disponíveis: --print, --save_json.")
		exit()

# print('Making request to vultr.com...')
r = requests.get("https://www.vultr.com/pricing/")
# print('Request complete!')

# print('Parsing request via lxml...')
htmlR = html.fromstring(r.content)
# print('Request parsed!')

# print('Acquiring table data...')
cpu = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[3]/span/strong/text()')

memory = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[4]/strong/text()')

storage1 = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[2]/span/strong/text()')
storage2 = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[2]/span/text()')
storage2 = [x.strip() for x in storage2]
storage2 = [i for i in storage2 if i]
storage = list(' '.join(x) for x in zip(storage1, storage2))

bandwidth = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[5]/span/strong/text()')

price1 = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[6]/span[1]/strong/text()')
price2 = htmlR.xpath('//*[@id="compute"]/div[1]/div[2]/div/div[1]/div[6]/span[1]/text()')
price2 = [x.strip() for x in price2]
price2 = [i for i in price2 if i] 
price = list(''.join(x) for x in zip(price1, price2))

titles = ['CPU', 'Memory', 'Storage', 'Bandwidth', 'Price']
data_vultr = [titles] + list(zip(cpu, memory, storage, bandwidth, price))
# print('Data acquired!')



# print('Making request to digitalocean.com...')
r = requests.get("https://www.digitalocean.com/pricing/")
# print('Request complete!')

# print('Parsing request via lxml...')
htmlR = html.fromstring(r.content)
# print('Request parsed!')

# print('Acquiring table data...')
cpu = htmlR.xpath('//*[@id="standard-droplets-pricing-table"]/div/div/table/tbody/tr/td[2]/text()')
cpu = [x.strip() for x in cpu]

memory = htmlR.xpath('//*[@id="standard-droplets-pricing-table"]/div/div/table/tbody/tr/td[1]/strong/text()')
memory = [x.strip() for x in memory]

storage = htmlR.xpath('//*[@id="standard-droplets-pricing-table"]/div/div/table/tbody/tr/td[3]/text()')
storage = [x.strip() for x in storage]

bandwidth = htmlR.xpath('//*[@id="standard-droplets-pricing-table"]/div/div/table/tbody/tr/td[4]/text()')
bandwidth = [x.strip() for x in bandwidth]

price = htmlR.xpath('//*[@id="standard-droplets-pricing-table"]/div/div/table/tbody/tr/td[5]/strong/text()')
price = [x.strip() for x in price]

titles = ['CPU', 'Memory', 'Storage', 'Bandwidth', 'Price']
data_digitalocean = [titles] + list(zip(cpu, memory, storage, bandwidth, price))
# print('Data acquired!')



# print('Displaying data...')
if console_print:
	print("Cloud Computing Services at Vultr.com")
	for index, value in enumerate(data_vultr):
		line = '|'.join(str(x).ljust(12) for x in value)
		print(line)
		if index == 0:
			print('-' * len(line))
	print("Cloud Computing Services at DigitalOcean.com")
	for index, value in enumerate(data_digitalocean):
		line = '|'.join(str(x).ljust(12) for x in value)
		print(line)
		if index == 0:
			print('-' * len(line))

if save_json:
	with open('vultr_json.txt', 'w') as outfile:
		json.dump(data_vultr, outfile)
	print("Arquivo salvo em formato JSON em vultr_json.txt")

	with open('digitalocean_json.txt', 'w') as outfile:
		json.dump(data_digitalocean, outfile)
	print("Arquivo salvo em formato JSON em digitalocean_json.txt")

if save_csv:
	with open('vultr.csv', mode='w') as outfile:
	    csv_writer = csv.writer(outfile, delimiter=',', lineterminator = '\n')
	    for row in data_vultr:
	    	csv_writer.writerow(i for i in row)
	print("Arquivo salvo em formato CSV em vultr.csv")

	with open('digitalocean.csv', mode='w') as outfile:
	    csv_writer = csv.writer(outfile, delimiter=',', lineterminator = '\n')
	    for row in data_digitalocean:
	    	csv_writer.writerow(i for i in row)
	print("Arquivo salvo em formato CSV em digitalocean.csv")