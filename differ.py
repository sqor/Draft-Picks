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

def generatePageScreenshotPath(index, reportDir, prefix):
    return  reportDir + "/" + prefix + str(index) + ".png"

def fetchPage(index, url, reportDir, prefix):
    imagePath = generatePageScreenshotPath(index, reportDir , prefix)
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

def fetchPages(reportDir, pages, prefix):
    index = 0
    for page in pages:
        fetchPage(index, page, reportDir, prefix)
        print index
        index+=1
    return index


def generateDiffImage(imagePath01, imagePath02, outputImageName):
    _arguments = imagePath01 + " " + imagePath01 + " " + outputImageName
    return shell.exec_cmd("./generateDiff.sh " + _arguments)

    #
def generateDiffImages(reportDir, prefix01, prefix02,  imagesCount):
    results = []
    for xx in range(0, imagesCount):
        image01Path = generatePageScreenshotPath(xx, reportDir, prefix01)
        image02Path = generatePageScreenshotPath(xx, reportDir, prefix02)
        outputPath = generatePageScreenshotPath(xx, reportDir, "diff_")
        result = generateDiffImage(image01Path, image02Path, outputPath )
        print "--- diff ------"
        print result


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
    fetchPages(reportDir, pages01, "pages01_")
    print "done Fetching ..."
    fetchPages(reportDir, pages02, "pages02_")
    pagesCount = len(pages02)

    print "**********************************"
    print pagesCount
    print "*********************************"

    # Now we actually compare
    generateDiffImages(reportDir, "pages01_",  "pages02_",  pagesCount)


# Finally we run our stuff
run()












