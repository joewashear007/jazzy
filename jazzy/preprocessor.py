from macros import *
import re

class Preprocessor:
    def __init__(self):
        # self._macros = [core.LabelMacro()]
        self._labels = {}
        self._lines = []
        self.regex = re.compile("label\s(?P<name>.+)")

        #if we added in macros, then can be be inserted here
    # def parseLine(self):
    #     #scan each line to match it against any macro
    #     #returns on first match
    #     line = self._linesToProcess.pop();
    #     macthed = False
    #     for m in self._macros:
    #         # does the pre processor match
    #         if m.testLine(line):
    #             macthed = True
    #             newLines = m.processLine(line)
    #             newLines.reverse()
    #             #Adds the current file to the top of the stack
    #             self._linesToProcess =  self._linesToProcess + newLines;
    #     if not macthed:
    #         self.lines.append(line)


    def parseFile(self, filename):
		#Use reverse to be able to use list as stack
        file = open(filename, 'r')
        lineNumber = 1
        for line in file:
            # print("#Reading: "+line)
            labelName =  self.TestForLabel(line)
            # print("LabelName: ", labelName)
            if labelName is not None:
                # print("#Has Label!");
                self._labels[labelName] = lineNumber

            lineNumber = lineNumber + 1;
            self._lines.append(line)
        return self._lines

    def GetLabels(self):
        return self._labels

    def TestForLabel(self, line):
        matches = self.regex.search(line)
        # print("Has match: ", (matches is not None))
        if matches is not None:
            # label name
            return matches.group("name")
        else:
            return None
