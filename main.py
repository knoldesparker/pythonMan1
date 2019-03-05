from urllib.request import urlopen
from urllib.error import HTTPError
import subprocess
import os

#Getting API file from Github
"""
try:
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    resault = res.read().decode('utf-8')
except HTTPError as hTTPeR:
    print(hTTPeR)
"""

urlList = []
#Method for searching the file
def search(filename, filter):
    try:
        with open(filename) as f:
            for line in f:
                if filter in line:
                    line = line[:]
                    yield line[18:-3].strip()
    except FileNotFoundError as fNFE:
        print(fNFE)
    except Exception as err:
        print(err)

try:
    for result in search('localAPI.txt', 'clone_url'):
        urlList.append(result)
except Exception:
    print(Exception)

try:
    if "repos" not in os.listdir('.'):
        os.mkdir("repos")
        os.chdir("repos")
    else:
        os.chdir("repos")
except Exception as err:
    print(err)

for element in urlList:
    subprocess.run(['git','clone',element])







