from urllib.request import urlopen
from urllib.error import HTTPError
import subprocess
import os
import sys
from glob import iglob
import glob
import re

#Getting API file from Github
"""
try:
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    resault = res.read().decode('utf-8')
except HTTPError as hTTPeR:
    print(hTTPeR)
"""

urlList = []
readMeList = []
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

#Appends the elements to the urllist
try:
    for result in search('localAPI.txt', 'clone_url'):
        urlList.append(result)
except Exception:
    print(Exception)

try:
    if "repos" not in os.listdir('.'):
        os.mkdir("repos")
        os.chdir("repos")
        print("Creating dir")
    else:
        os.chdir("repos")
        print("dir exist, swapping dir")
except Exception as err:
    print(err)
except FileNotFoundError as fNFE:
    print(fNFE)

"""
for elm in urlList:
    if not os.path.exists(elm[49:-4]):
            print("cloning from git")
            subprocess.run(['git','clone', elm])
    else:
            print("pulling from git")
            subprocess.run(['git', 'pull'])
"""

"""
for filename in glob.iglob('**/README.md', recursive=True):
    print(filename)
"""
rr = []
file_list = [f for f in iglob('**/README.md', recursive=True) if os.path.isfile(f)]
for f in file_list:
    with open(f,'rt') as fl:
        lines = fl.read()
        rr.append(lines)
    print(rr)

"""
for fp in file_list:
        with open(fp, 'r') as f:
            # Read the first line
            rReading = f.read()
            # Append the first line into the list
            rr.append(first_line)
        print(rr)
"""








