# coding=utf-8

from io import StringIO
from unittest import TestCase

from citeproc.source.bibtex.bibparse import BibTeXParser


class TestBibTeXParser(TestCase):
    def setUp(self):
        file = StringIO()
        self.parser = BibTeXParser(file)

    # def test__parse(self):
    #     self.fail()
    #
    # def test__parse_entry(self):
    #     self.fail()
    #
    # def test__parse_key(self):
    #     self.fail()
    #
    # def test__parse_name(self):
    #     self.fail()
    #
    # def test__parse_value(self):
    #     self.fail()
    #
    # def test__parse_string(self):
    #     self.fail()
    #
    # def test__parse_variable(self):
    #     self.fail()
    #
    # def test__parse_integer(self):
    #     self.fail()
    #
    # def test__eat_whitespace(self):
    #     self.fail()
    #
    # def test__jump_to_next_line(self):
    #     self.fail()
    #
    # def test__parse_preamble(self):
    #     self.fail()

    # from "A TEX Primer for Scientists" (sections 5.2 and 5.3)
    # by Stanley A. Sawyer, Steven G. Krantz
    MACROS = [("Æsop's fables", r"\AE sop's fables"),
              ('Æ is a Latin ligature', r"\AE\ is a Latin ligature"),
              ('A TeX expert is a TeXnician.',
                    r"A \TeX\ expert is a \TeX nician."),
              ('This book is ©ed.', r"This book is \copyright ed."),
              ('Umeå, Sweden', r"Ume\aa, Sweden"),
              ('Your serial number is Å1102.',
                    r"Your serial number is \AA1102."),
              ('Your serial number is Å1102.',
                    r"Your serial number is \AA  1102."),
              ('$22.50 plus $ 4.07 tax.', r"\$22.50 plus \$ 4.07 tax."),
              ('Crève Cœur, Missouri', r"Cr\`eve C\oe ur, Missouri"),
              ('Pëtr, meet Françoise', r"P\"etr, meet Fran\c coise")]

    ACCENT_MACROS = [('très élevé', r"tr\`es \'elev\'e"),
                     ('übel Föhn', r'\"ubel F\"ohn'),
                     ('Andō Tokutarō', r"And\=o Tokutar\=o"),
                     ('García Lorca', r"Garc\'\i a Lorca"),
                     ('naïve', r'na\"\i ve')]

    # nested macros
    NESTED_MACROS = [('Escobar, María José', r"Escobar, Mar{\'\i}a Jos{\'e}"),
                     ('Escobar, María-José', r"Escobar, Mar\'{\i}a-Jos\'{e}")]

    def test__expand_macros(self):
        for reference, name in self.MACROS:
            self.assertEqual(reference, self.parser._expand_macros(name))
        for reference, name in self.ACCENT_MACROS:
            self.assertEqual(reference, self.parser._expand_macros(name))
        for reference, name in self.NESTED_MACROS:
            self.assertEqual(reference, self.parser._expand_macros(name))

    # def test__split_name(self):
    #     self.fail()