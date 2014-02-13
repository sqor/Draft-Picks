import json
import sys
import os
import tempfile

import pdb

from lib.cmds import shell

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
    return reportDir

def generatePageScreenshotPath(index, reportDir):
    return reportDir + "/" + str(index) + ".png"

def fetchPage(index, url, reportDir):
    imagePath = generatePageScreenshotPath(index, reportDir )
    print "--------------------_"
    print imagePath
    print url
    print "--------------------_"

    output = shell.exec_cmd("./getPage.sh " + url + " " + imagePath)


def generatePages(pages, siteBase01, siteBase02):
    '''
    Takes the pages and adds a base to each page.
    '''
    pagesWithBase01 = []
    pagesWithBasae02 = []
    for pagesEntry in pages:
        page01End = pagesEntry["url1"]
        page02End = pagesEntry["url2"]

        pagesWithBase01.append(siteBase01 + page01End)
        pagesWithBasae02.append(siteBase02 + page02End)

    return (pagesWithBase01, pagesWithBasae02)

def fetchPages(reportDir, pages):
    index = 0
    for page in pages:
        fetchPage(index, page, reportDir)
        print index
        index+=1

def run(fileName="sites.json"):
    '''
    Runs the program
    '''
    print "Start"
    # We get our pages into a nicer form
    sites = readJsonFromFile(fileName)
    (pages01, pages02) = generatePages(
                sites['pages']
            ,   sites["siteBase01"], sites["siteBase02"])
    print pages01
    print "pages 02"
    print pages02

    reportDir = setupDirectory()
    print reportDir
    fetchPages(reportDir, pages01)
    print "done Fetching ..."
    # fetchPages(reportDir, pages02)

# Finally we run our stuff
run()












