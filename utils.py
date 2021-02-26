import math
from rply import LexerGenerator, ParserGenerator


def build_lexer():
    # LEXERGENERATOR INSTANZIEREN
    lexer_generator = LexerGenerator()
    # WHITESPACES IGNORIEREN
    lexer_generator.ignore(r'\s+')
    # ZAHLEN ERKENNEN
    # -? => ENTWEDER MINUS ODER NICHT
    # \.? => ENTWEDER EIN PUNKT ODER NICHT
    # [0-9]* BELIEBIG OFT 0-9 (MINDESTENS 0 MAL)
    # [0-9]+ BELIEBIG OFT 0-9 (MINDESTENS 1 MAL)
    # 'NUM' => NUMBER
    lexer_generator.add('NUM', r'-?[0-9]*\.?[0-9]+')
    
    # OPERATOREN
    lexer_generator.add('ADD', r'\+')   # 'ADD' => ADD
    lexer_generator.add('SUB', r'-')    # 'SUB' => SUBTRACT
    lexer_generator.add('MUL', r'\*')   # 'MUL' => MULTIPLY
    lexer_generator.add('DIV', r'/')    # 'DIV' => DIVIDE
    lexer_generator.add('MOD', r'%')    # 'MOD' => MODULO
    lexer_generator.add('EXP', r'^|\*\*')    # 'EXP' => EXPONENTIATE

    lexer_generator.add('BR_O', r'\(')  # 'BR_O' => BRACKET OPEN
    lexer_generator.add('BR_C', r'\(')  # 'BR_O' => BRACKET CLOSE
    lexer_generator.add('ABS_P', r'\|') # 'ABS_P' => ABSOLUTE PART

    # LEXER ERSTELLEN UND ZURÜCKGEBEN
    return lexer_generator.build()

def build_parser():
    # TOKENS FÜR PARSER FESTLEGEN
    parser_generator = ParserGenerator([
        'NUM',
        'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'EXP',
        'ABS_P',
        'BR_O', 'BR_C'
    ])

    # REGELN FÜR PARSER FESTLEGEN

    @parser_generator.production('main : expr')
    def main(x): return x[0]

    @parser_generator.production('expr : factor')
    def term_zahl(x): return x[0]
    @parser_generator.production('expr : expr SUB factor')
    def term_zahl(x): return x[0] - x[2]
    @parser_generator.production('expr : expr ADD factor')
    def term_zahl(x): return x[0] + x[2]


    # STANDARD RECHENOPERATIONEN 
    @parser_generator.production('factor : term')
    def term_zahl(x): return x[0]
    @parser_generator.production('factor : factor EXP term')
    def term_zahl(x): return x[0] ** x[2]
    @parser_generator.production('factor : factor DIV term')
    def term_zahl(x): return x[0] / x[2]
    @parser_generator.production('factor : factor MOD term')
    def term_zahl(x): return x[0] % x[2]
    @parser_generator.production('factor : factor MUL term')
    def term_zahl(x): return x[0] * x[2]

    @parser_generator.production('term : NUM')
    def term_zahl(x): return float(x[0].getstr())
    # KLAMMERN
    @parser_generator.production('term : BR_O expr BR_C')
    def term_zahl(x): return x[1]
    # BETRAG
    @parser_generator.production('term : ABS_P expr ABS_P')
    def term_zahl(x): return x[0] if x[0] >= 0 else x[0] * -1


    return parser_generator.build()



lexer = build_lexer()
parser = build_parser()
