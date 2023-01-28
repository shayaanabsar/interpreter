from lexer import Lexer
from parser import Parser
from sys import argv

lexer = Lexer()

if len(argv) != 2:
    print("Usage: python run.py input_file.mo")
    exit()

try:
    with open(argv[1], "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"File: {argv[1]} not found.")
    exit()

lexer.lex(text)

parser = Parser(lexer.tokens)

parser.parse()