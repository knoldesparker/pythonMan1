from urllib.request import urlopen
from urllib.error import HTTPError
import subprocess
import os
import sys
from glob import iglob
import glob
import re
import fileinput

#Getting API file from Github
"""
try:
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    resault = res.read().decode('utf-8')
    file = open('localAPI2.txt', 'r+')
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
        for result in search('localAPI2.txt', 'clone_url'):
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
# Remove """ for automatic git updates, disable due to speed
##Clones form the git repos
for elm in urlList:
    if not os.path.exists(elm[49:-4]):
            print("cloning from git")
            subprocess.run(['git','clone', elm])
    else:
            print("pulling from git")
            subprocess.run(['git', 'pull'])


#Reads from the md files in the repos, slicing the lines from ## RR to ## SP. Also takes acount for errors
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
#Writes the lines in rr array to the required_reading.md file
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

#Opens the file and removes the ## Required reading headline
def removeHashTag():
    global line
    f = open("required_reading.md", "r")
    lines = f.readlines()
    f.close()
    f = open("required_reading.md", "w")
    for line in lines:
        if line != "## Required reading" + "\n":
            f.write(line)
    f.close()
removeHashTag()

#Sorts the file
#Opens the file
with open('required_reading.md', "r") as f:
    sorted_file = sorted(f)

#save to a file
with open('required_reading.md', "w") as f:
    f.writelines(sorted_file)


for line in fileinput.FileInput("required_reading.md", inplace=1):
    if line.rstrip():
        print(line)


#Method to push to git
def pushToGit():
    # add,comit,push to git
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'commit requred reading'])
    subprocess.run(['git', 'pull'])
    subprocess.run(['git', 'push'])


pushToGit()


