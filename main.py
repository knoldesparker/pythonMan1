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
    file = open('localAPI.txt', 'r+')
    file.write(resault)
except HTTPError as hTTPeR:
    print(hTTPeR)
"""

urlList = []
readMeList = []

#Method for searching the local API file
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


def readURLFromAPI():
    try:
        for result in search('localAPI.txt', 'clone_url'):
            urlList.append(result)
    except Exception:
        print(Exception)


#Appends the elements to the urllist
readURLFromAPI()


def make_change_directory():
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


make_change_directory()


for elm in urlList:
    if not os.path.exists(elm[49:-4]):
            print("cloning from git")
            subprocess.run(['git','clone', elm])
    else:
            print("pulling from git")
            subprocess.run(['git', 'pull'])

def readFromMdFile():
    global rr
    rr = []
    file_list = [f for f in iglob('**/README.md', recursive=True) if os.path.isfile(f)]
    for f in file_list:
        with open(f, 'rt') as fl:
            lines = fl.read()
            lines = lines[lines.find('## Required reading'):lines.find('## Supplementary reading')]
            lines = lines[lines.find('## Required reading'):lines.find('### Supplementary reading')]
            lines = lines[lines.find('## Required reading'):lines.find('## Required reading paragraph')]
            rr.append(lines)


readFromMdFile()

def writeToRRMD():
    os.chdir('..')
    if "required_reading.md" not in os.listdir("."):
        e = open("required_reading.md", "w+")
        for line in rr:
            e.write(line)
    else:
        e = open("required_reading.md", "w+")
        for line in rr:
            e.write(line)

writeToRRMD()








