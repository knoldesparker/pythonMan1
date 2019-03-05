from urllib.request import urlopen
from urllib.error import HTTPError
import subprocess

"""
try:
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    resault = res.read().decode('utf-8')
    
except HTTPError as hTTPeR:
    print(hTTPeR)
"""

try:
    file = open('localAPI.txt','r+')
    output = file.read()
    print(output)
except FileNotFoundError as fNFeR:
    print(fNFeR)

