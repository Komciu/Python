class TextFormatter:
    def __init__(self, n = 4):
        self.baseCellWidth = n

    def createText(self, txt = "", n = -1):
        if(n == -1):
            n = self.baseCellWidth
        line = ""
        for c in txt:
            if(int(line.__len__()) < n - 1):
                line += c
            else:
                break
        line = self.fillWithZeros(line, n)
        return line

    def fillWithZeros(self, txt = '', n = -1):
        if(n == -1):
            n = self.baseCellWidth
        while(int(txt.__len__()) < n):
            txt += " "
        return txt

    def createColumnNames(self, names):
        line = self.fillWithZeros(n = 2*self.baseCellWidth)
        for name in names:
            line += self.createText(name)
        line += '\n'
        return line

    def createColumnValues(self, values):
        line = self.createText(values[0], 2*self.baseCellWidth)
        for value in values[1:]:
            line += self.createText(str(value))
        line += '\n'
        return line