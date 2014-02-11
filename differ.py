import json


class Differ():
    def readFileAsString(self, fileName):
        # Open our file
        fileHandle = open(fileName, "r")
        jsonString = fileHandle.read()
        return jsonString


