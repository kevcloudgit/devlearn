import csv
from urllib3.request import urlopen

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib3.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print(row)