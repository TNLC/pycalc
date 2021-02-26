import math
import readline
from utils import lexer, parser

ZIFFERN = '-0123456789.'

def eingabe_reparieren(eingabe):
    ergebnis = eingabe
    index = 0
    while index < len(ergebnis):
        if index != 0 and ergebnis[index] == '(':
            if ergebnis[index-1] in ZIFFERN:
                ergebnis = ergebnis[:index] + '*' + ergebnis[index:]
        elif index != len(ergebnis) - 1 and ergebnis[index] == ')':
            if ergebnis[index+1] in ZIFFERN + '(':
                ergebnis = ergebnis[:index+1] + '*' + ergebnis[index+1:]
        index = index + 1
    return ergebnis

if __name__ == '__main__':
    while(True):
        eingabe = input('>>> ')

        print(parser.parse(lexer.lex(eingabe)))

        if eingabe == 'exit' or eingabe == 'stop':
            break


