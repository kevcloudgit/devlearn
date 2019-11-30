#import requests
#import urilib3
import requests
import csv
import pandas as pd
import urllib.request
# from urllib import requests   #got error ImportError: cannot import name 'requests', pip install urllib
csv_link = r'https://gist.githubusercontent.com/mikeckennedy/6622abf5a78feeed70de6737f0337f98/raw/89e886abe22effa00442bf57bbd2178cbb2a485a/stocks.csv'
#r = requests.get(csv_link)


# when download from internet 
def download_excel(url):
    fileOpen = urllib.request.urlopen(url)
    file_info = fileOpen.read()
    file_info_str = str(file_info)
    file_lines = file_info_str.split("\\n")
    newfile = open('mystock.csv',"w")

    for info in file_lines:
        newfile.write(info + "\n")
    newfile.close()
#download_excel(csv_link)


# Read and compare from local csv file 

apple = pd.read_csv('csv_files\AAPL.csv')      # read file from local folder, need to use "\"
print("APPLE STOCK","\n", apple)

team = pd.read_csv('csv_files\TEAM.csv')
print("ATLASSION STOCK", "\n", team)




'''
def obtain_data(info):
    response = pd.read_csv(info)
    cr = csv.reader(response)
    cr_str = str(cr)  # whatever been read will be saved as string
    lines = cr_str.split("\\n")
    save_loc = r'mystockinfo.csv'
    fstep = open(save_loc, "w")
    for line in lines:
        fstep.write(line + "\n")
        print(lines)
    fstep.close()


obtain_data(csv_link)
print("finish")


# error: raise HTTPError(req.full_url, code, msg, hdrs, fp)  urllib.error.HTTPError: HTTP Error 401: Unauthorized


'''
'''
url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)
'''


'''

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True
# >> False
print is_downloadable('https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1543462665&period2=1574998665&interval=1d&events=history&crumb=1FCAsktNLB/')
'''
# >> True



'''
Q1. Use what we have learned to automatically fetch the CSV files of S&P500 companies’ shares from yahoo finance/our csv_server.py into a single folder. (see. https://finance.yahoo.com/quote/AAPL/history?p=AAPL there is a download data link, can you write a program to auto-download from yahoo finance or any APIs that you can find online?)

Q1Advanced. Use multithread or processes to achieve the above task

Q2. Write two REST APIs. One to load all the CSV files and the other one load single CSV file. 

Q2Advanced. After being hit by the API call, load all the CSVs with pandas and use a separate process to get the top 5 growing shares and top 5 high volume shares. 
Could you make this task multithreading/multiprocessing? 
How fast can you get the results? 
Write the results into a file. 
Could you write it into a JSON format?
Could you return the result as a response of a REST API on your server(e.g. def get_top_ranked_stocks_by_growth_(stocks), def get_top_ranked_stocks_by_volume_(stocks))?
Make sure you have your own or team git repo for the homework! Welcome to show off your code and homework next time! Let us do a peer review :wink
'''