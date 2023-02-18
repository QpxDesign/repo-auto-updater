import requests
import os
import json


def getLatestCommitID():
    url = "https://api.github.com/repos/qpxdesign/csclubwesbite/commits"
    response = requests.get(url)
    response = response.json()
    return response[0]["sha"]


def getCurrentlyUpCommitID():
    f = open("current_commit_id.txt", "r")


def writeCommitID():
    f = open("current_commit_id.txt", "w")
    f.write(getLatestCommitID())


def run():
    os.system("echo standing by")
    if (getLatestCommitID() != getCurrentlyUpCommitID()):
        writeCommitID()
        # os.system("bash ~/update-portfolio-repos/csclub.sh")


run()
