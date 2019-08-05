# Extracts data from a html request
def extractData(htmlRequest, xpaths):
	cpu = htmlRequest.xpath(xpaths[0])
	cpu = [x.strip() for x in cpu]
	memory = htmlRequest.xpath(xpaths[1])
	memory = [x.strip() for x in memory]
	storage = htmlRequest.xpath(xpaths[2])
	storage = [x.strip() for x in storage]
	bandwidth = htmlRequest.xpath(xpaths[3])
	bandwidth = [x.strip() for x in bandwidth]
	price = htmlRequest.xpath(xpaths[4])
	price = [x.strip() for x in price]

	titles = ['CPU', 'Memory', 'Storage', 'Bandwidth', 'Price']
	data = [titles] + list(zip(cpu, memory, storage, bandwidth, price))
	return data