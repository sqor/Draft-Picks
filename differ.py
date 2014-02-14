# NOTE: very bad code.
import json
import sys
import os
import tempfile
import subprocess

import pdb

from time import sleep
# from lib.cmds import shell

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

    output = os.popen("./getPage.sh " + url + " " + imagePath)

    sleep(10)
    return output

def generatePages(pages, siteBase01, siteBase02):
    '''
    Takes the pages and adds a base to each page.
    '''
    pagesWithBase01 = []
    pagesWithBase02 = []
    # XXX super ugly, fix this
    for pagesEntry in pages[0]:
        page01End = pagesEntry
        pagesWithBase01.append(siteBase01 + page01End)

    for pagesEntry in pages[1]:
        page01End = pagesEntry
        pagesWithBase02.append(siteBase02 + page01End)

    return (pagesWithBase01, pagesWithBase02)

def fetchPages(reportDir, pages, prefix):
    index = 0
    for page in pages:
        fetchPage(index, page, reportDir, prefix)
        print index
        index+=1
    return index


def generateDiffImage(imagePath01, imagePath02, outputImageName):
    _arguments = imagePath01 + " " + imagePath02 + " " + outputImageName
    command = "./generateDiff.sh " + _arguments

    #pdb.set_trace()
    popoenResult = subprocess.Popen(
            command
            , shell=True
            , stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

    result = popoenResult.stderr.read()
    return result

#
def generateDiffImages(reportDir, prefix01, prefix02,  imagesCount):
    results = []
    for xx in range(0, imagesCount):
        image01Path = generatePageScreenshotPath(xx, reportDir, prefix01)
        image02Path = generatePageScreenshotPath(xx, reportDir, prefix02)
        outputPath = generatePageScreenshotPath(xx, reportDir, "diff_")
        print image01Path
        print image02Path
        result = generateDiffImage(image01Path, image02Path, outputPath )
        print "--- diff ------"
        print result

        results.append(result)
        # pdb.set_trace()

    print results
    return results

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
    resultsArray= generateDiffImages(reportDir, "pages01_",  "pages02_",  pagesCount)
    print "resultsArray"
    print resultsArray
    fileName = "report.json"
    with open(os.path.join(reportDir, fileName), 'w') as fh:
        jsonStr = json.dumps({"test":resultsArray})
        fh.write( jsonStr  )

# Finally we run our stuff
run()






