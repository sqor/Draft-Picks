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

    return {
            "pages01": pagesWithBase01
        ,   "pages02": pagesWithBasae02
    }

def run(fileName="sites.json"):
    sites = readJsonFromFile(fileName)
    pages = generatePages(sites['pages'], sites["siteBase01"], sites["siteBase02"])

    return pages
