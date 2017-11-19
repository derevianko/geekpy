import argparse
# import logging
import requests

# # add filemode="w" to overwrite
# logging.basicConfig(filename="sample.log",filemode=”w”, level=logging.INFO)
#
# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")
#
# url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
# response = requests.get(url)
# response(response.json())

parser = argparse.ArgumentParser()
parser.add_argument('url', help='input parse url', type=str)

args = parser.parse_args()
url = args.url

# url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
response = requests.get(url)
response = response.json()
for num, x_id in enumerate(response, 0):
    print(str(num) + ':' + str(x_id))



print (args.url)
