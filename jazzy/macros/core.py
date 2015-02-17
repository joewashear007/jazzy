__all__ = ["LabelMacro"]

import re

class LabelMacro:
    def __init__(self):
        self.regex = re.compile("label\s.+")

    def testline(self, line):
        if self.regex.search(line) is not None:
            return true
        else:
            return false

    def processLine(self, line):
        return line
