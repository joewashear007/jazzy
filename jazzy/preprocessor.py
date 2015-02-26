import re

class Preprocessor:
    def __init__(self):
        self._labels = {}
        self._lines = []
        self.regex = re.compile("label\s(?P<name>.+)")

    def parseFile(self, file):
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
