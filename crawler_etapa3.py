import requests
from lxml import html
import sys
import json

import csv

#     ETAPA 3: 1 página-alvo, imprime na tela, salva em json, salva em csv
# A terceira etapa exige que o seu crawler funcione para a mesma página-alvo da etapa anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de salvar os dados em um arquivo em formato csv.

print("ETAPA 3: 1 página-alvo, imprime na tela, salva em json, salva em csv")

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
		print("Argumento incorreto:", args, ". Arhgumentos disponíveis: --print, --save_json, --save_csv.")
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
data = [titles] + list(zip(cpu, memory, storage, bandwidth, price))
# print('Data acquired!')

# print('Displaying data...')
if console_print:
	for index, value in enumerate(data):
		line = '|'.join(str(x).ljust(12) for x in value)
		print(line)
		if index == 0:
			print('-' * len(line))

if save_json:
	with open('data_json.txt', 'w') as outfile:
		json.dump(data, outfile)
	print("Arquivo salvo em formato JSON em data_json.txt")

if save_csv:
	with open('data.csv', mode='w') as outfile:
	    csv_writer = csv.writer(outfile, delimiter=',', lineterminator = '\n')
	    for row in data:
	    	csv_writer.writerow(i for i in row)
	print("Arquivo salvo em formato CSV em data.csv")