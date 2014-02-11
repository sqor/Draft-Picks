import json
import sys
import os
import tempfile

import pdb

def readJsonFromFile(fileName):
    '''
        Reads file into json python object
    '''
    fileHandle = open(fileName, "r")
    jsonString = fileHandle.read()
    return json.loads(jsonString)

def setupDirectory():
    # Create a directory for our data
    reportDir = tempfile.mkdtemp(prefix="report_", dir=".")
    #Fetch our little pages

def fetchPage(index, url, reportDir):
    os.popen("./getPage.sh " + url + " " + reportDir + "/" + index)


def generatePages(pages, siteBase):
    pagesWithBase = []
    pdb.set_trace()
    for page in pages:
        pagesWithBase.append(siteBase + page)
    return pagesWithBase

def run(fileName="sites.json"):
    sites = readJsonFromFile(fileName)
    pages01 = generatePages(sites['pages'], sites["siteBase01"])
    pages02 = generatePages(sites['pages'], sites["siteBase02"])
    print pages01

