import json
import sys
import os
import tempfile

def readJsonFromFile(fileName):
    '''
        Reads file into json python object
    '''
    fileHandle = open(fileName, "r")
    jsonString = fileHandle.read()
    return json.loads(jsonString)

def setupDirectory()
    # Create a directory for our data
    reportDir = tempfile.mkdtemp(prefix="report_", dir=".")
    #Fetch our little pages

def fetchPage(index, url, reportDir)
    os.popen("./getPage.sh " + url + " " + reportDir "/" + index)
