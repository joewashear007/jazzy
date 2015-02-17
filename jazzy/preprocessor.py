from macros import *

class Preprocessor:
    def __init__(self):
        self._macros = [core.LabelJazMacro()]
        self._labels = {}
        self._lines = []

    def parseLine(self, line):
        #scan each line to match it agaisnt any macro
        #returns on first match
        for m in self._macros:
            # does the pre processor match
            if m.testLine(line):
                newLines = m.processLine(line)
                # this won;t work, need to operator as a stack
                self._lines = newLines + self._lines

    def parseFile(self, filelines):
        self._lines = filelines;
        for line in  self._lines:
            self.parseLine(line)
