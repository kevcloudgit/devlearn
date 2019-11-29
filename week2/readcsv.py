import requests

#from urllib import requests   #got error ImportError: cannot import name 'requests', pip install urllib

csv_link = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1543462665&period2=1574998665&interval=1d&events=history&crumb=1FCAsktNLB/'

def obtain_data(csv_link):
    response = requests.urlopen(csv_link)
    csv = response.read()
    csv_string = str(csv)  # whatever been read will be saved as string 
    lines = csv_string.split("\\n")
    save_loc = r'mystockinfo.csv'
    fstep = open(save_loc,"w")
    for line in lines:
        fstp.write(line + "\n")
    fstep.close()

obtain_data(csv_link)

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
# >> True

'''

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



Make sure you have your own or team git repo for the homework! Welcome to show off your code and homework next time! Let us do a peer review :wink:
'''