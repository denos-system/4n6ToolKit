#
#	Written By Darren Enos (4/26/2021)
#
#	Finally, check a list of IPs for abuse reports and write an IP lookup report, all at once!
#
#	*** Parts to change are noted like this ***



import requests
import json
import csv

#			*** UPDATE WITH YOUR LOCAL FILE NAME ***
infile = open("ips.txt","r")
jsons = []

for address in infile:
	# Defining the api-endpoint
	url = 'https://api.abuseipdb.com/api/v2/check'

	querystring = {
	    'ipAddress': address,
	    'maxAgeInDays': '90'
	}

	headers = {
	    'Accept': 'application/json',

#					*** UPDATE WITH YOUR OWN API KEY ***
	    'Key': '0315d4b0c2b5e16052a13f10fda0d7fab1f0bcf2706f2704a4ca957973bf2b000c6ac289fe1b8112'
	}

	response = requests.request(method='GET', url=url, headers=headers, params=querystring)

	# Formatted output
	decodedResponse = json.loads(response.text)
	jsons.append(decodedResponse["data"])



infile.close()


#			*** UPDATE WITH DESIRED OUTPUT NAME ***
data_file = open('data_file.csv', 'w')
  
# create the csv writer object
csv_writer = csv.writer(data_file)
  
# Counter variable used for writing 
# headers to the CSV file
count = 0
  
for item in jsons:
    if count == 0:
  	
        # Writing headers of CSV file
        header = item.keys()
        csv_writer.writerow(header)
        count += 1
  
    # Writing data of CSV file
    host_list = ['{0}'.format(element) for element in item["hostnames"]]
    item["hostnames"] = host_list

    csv_writer.writerow(item.values())
  
data_file.close()


