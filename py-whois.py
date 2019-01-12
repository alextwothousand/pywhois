from bs4 import BeautifulSoup
import requests as re
import subprocess as sp

url = ''
while url == '':
    url = input('Please enter a URL to retrieve the WHOIS data of: ')

response = re.get(f"https://www.whois.com/whois/{url}")
soup = BeautifulSoup(response.content, "lxml")

try:
    souped = soup.select_one('.df-block-raw').text
except:
    print("An error has occured! (Most likely that website isn't registered.)")
    exit()

body = souped.split('Raw Whois Data', 1)

with open(f'whois/{url}.whois', 'w') as f:
    f.write(f'{body[1]}\n')
    f.write('================================================================\n')
    f.write("This service is provided to you by py-whois, written by Bork.\n")

sp.Popen(['notepad.exe', f'whois/{url}.whois'])
input(f'Complete. Data dumped to whois/{url}.whois! Press enter to exit.')

