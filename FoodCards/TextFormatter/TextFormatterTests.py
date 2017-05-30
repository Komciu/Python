import unittest
from TextFormatter.TextFormatter import TextFormatter


class LineFormatterTests(unittest.TestCase):
    def test_create4Spaces(self):
        lf = TextFormatter()
        self.assertEqual("    ", lf.createText())

    def test_create2Letter2Spaces(self):
        lf = TextFormatter()
        self.assertEqual("ab  ", lf.createText("ab"))

    def test_create2Letter6Spaces(self):
        lf = TextFormatter(8)
        self.assertEqual("ab      ", lf.createText("ab"))

    def test_create3lettersFrom5LetterWord(self):
        lf = TextFormatter()
        self.assertEqual("abc ", lf.createText("abcde"))

    def test_createLineWithColumnNames(self):
        lf = TextFormatter(8)
        resultLine = "                size    kcal    fat     fatS    fatUsM  fatUsB  prot    fiber   \n"
        self.assertEqual(resultLine, lf.createColumnNames(["size", "kcal", "fat", "fatS", "fatUsM", "fatUsB", "prot", "fiber"]))

    def test_createColumnWithValues(self):
        lf = TextFormatter(8)
        resultLine = "Kurczak         100     200     0       0       0       0       0       0       \n"
        self.assertEqual(resultLine, lf.createColumnValues(["Kurczak", 100, 200, 0, 0, 0, 0, 0, 0]))