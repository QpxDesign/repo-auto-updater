from requests_html import HTMLSession
import re
import os

session = HTMLSession()

r = session.get('https://github.com/QpxDesign/csclubwesbite')
aElements = r.html.find("a")
def getLatestCommitID():
    for a in aElements:
        if len(re.findall("/commit/",a.attrs['href'])) != 0:
            if len(a.text) == 7:
                return a.text 
    return ""
  
def getCurrentlyUpCommitID():
    f = open("current_commit_id.txt", "r")

def writeCommitID():
    f  = open("current_commit_id.txt", "w")
    f.write(getLatestCommitID())

def run():
    os.system("echo standing by")
    if (getLatestCommitID() != getCurrentlyUpCommitID()):
        writeCommitID();
        os.system("bash ~/update-portfolio-repos/csclub.sh")

run()