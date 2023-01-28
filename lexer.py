from re import finditer, compile
from copy import copy
from tokens import *

KEYWORDS = ["True", "False", "if", "else", "switch", "case", "default", "while", "stdin", "stdout", "func", "return"]

class Lexer:
    def __init__(self):
        self.tokens = []

    def lex(self, code):
        self.tokens = []
        self.error = None

        lexemes = {
            "COMMENT": r"\/\/.+",

            "NEWLINE": r"\n",

            "NUMBER": r"\d+\.\d+|\d+",
            "TRUE": r"\bTrue\b",
            "FALSE": r"\bFalse\b",
            "STRING": r'\"[^"]*\"',


            "ADD": r"\+",
            "MINUS": r"-",
            "MULTIPLY": r"\*",
            "DIVIDE": r"(?<!/)/(?!/)",
            "MOD": r"%",

            "LPAREN": r"\(",
            "RPAREN": r"\)",
            "LCURLYPAREN": r"{",
            "RCURLYPAREN": r"}",
            "LSQUAREPAREN": r"\[",
            "RSQUAREPAREN": r"\]",
            "ID": r"[A-Za-z]+",
            "ASSIGN": r"(?<![=><!])=(?![=><!])",

            "GREATER": r">(?!=)",
            "LESS": r"<(?!=)",
            "EQUAL": r"==",
            "NOT_EQUAL": r"!=",
            "GREATER_EQUAL": r">=",
            "LESS_EQUAL": r"<=",

            "IF": r"\bif\b",
            "ELSE": r"\belse\b",

            "SWITCH": r"\bswitch\b",
            "CASE": r"\bcase\b",
            "DEFAULT": r"\bdefault\b",

            "WHILE": r"\bwhile\b",

            "STDIN": r"\bstdin\b",
            "STDOUT": r"\bstdout\b",

            "AND": r"&&",
            "OR": r"\|\|",
            "NOT": r"!(?!=)",

            "FUNCTION": r"\bfunc\b",
            "RETURN": r"\breturn\b",

            "STRUCT": r"struct",
        }


        self.tokens = []

        for lexeme in lexemes:
            matches = finditer(compile(lexemes[lexeme]), code)
            for match in matches:
                if lexeme == "ID":
                    if match.group() in KEYWORDS:
                        continue
                self.tokens.append(Token(lexeme, match.span(), match.group()))
        self.tokens.sort(key=lambda x: x.span)

        start, end = -1, -1
        for token in copy(self.tokens):
            if token.type in ("STRING", "COMMENT"):
                start, end = token.span
                continue
            tokenStart, tokenEnd = token.span
            if tokenStart >= start and tokenEnd <= end:
                self.tokens.remove(token)

        return self.tokens