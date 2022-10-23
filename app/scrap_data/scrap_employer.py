#open https://transparency-in-coverage.uhc.com/ and print all href links

import urllib.request as urllib2
from bs4 import BeautifulSoup
import json
import csv
import re

url = urllib2.urlopen("https://transparency-in-coverage.uhc.com/api/v1/uhc/blobs/").read()
# print(url)
soup = BeautifulSoup(url, "html.parser")

# print(soup.prettify())
transform_json = json.loads(soup.prettify())

dump_data = json.dumps(transform_json, indent=4, sort_keys=True)

#print "downloadUrl" in dump_data
dump_data = dump_data.split("downloadUrl")

for i in range(1, len(dump_data)):
    if "employees" in dump_data[i] or "EMPLOYEES" in dump_data[i] or "Employees" in dump_data[i]:
        if dump_data[i].split('"')[2].endswith("index.json"):
            print(dump_data[i].split('"')[2])
            #TODO click and download all the files
            #write all to a new csv file
            with open('links.csv', 'a') as f:
                f.write(dump_data[i].split('"')[2] + ",")
                f.close()
#read links.csv and download all the files
with open('links.csv', 'r') as f:
    for line in f:
        for link in line.split(","):
            if link != "":
                print(link)
                urllib2.urlretrieve(link, link.split("/")[-1])