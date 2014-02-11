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


def generatePages(pages, siteBase01, siteBase02):
    pagesWithBase01 = []
    pagesWithBasae02 = []
    # pdb.set_trace()
    for pagesEntry in pages:
        page01End = pagesEntry["url1"]
        page02End = pagesEntry["url2"]

        pagesWithBase01.append(siteBase01 + page01End)
        pagesWithBasae02.append(siteBase02 + page02End)

    return (pagesWithBase01, pagesWithBasae02)

def run(fileName="sites.json"):
    # We get our pages into a nicer form
    sites = readJsonFromFile(fileName)
    (pages01, pages02) = generatePages(sites['pages'], sites["siteBase01"], sites["siteBase02"])
    print pages01
    print "pages 02"
    print pages02
