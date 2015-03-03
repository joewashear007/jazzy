import re

class Preprocessor:
    def __init__(self):
        self._labels = {}
        self._lines = []
        self.regex = re.compile("label\s(?P<name>.+)")

    def parseFile(self, file):
        lineNumber = 0
        for line in file:
            # if line.strip() is '':
            #     continue
            labelName =  self.TestForLabel(line)
            if labelName is not None:
                # print("#Has Label!");
                self._labels[labelName.strip()] = lineNumber

            lineNumber = lineNumber + 1;
            self._lines.append(line.strip())
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
