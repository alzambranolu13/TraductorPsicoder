import sys
from antlr4 import *
from gen.PsicoderLexer import PsicoderLexer
from gen.PsicoderParser import PsicoderParser
from gen.PsicoderTraductorListener import PsicoderTraductorListener

def main(argv):
    input = FileStream("input.txt")
    lexer = PsicoderLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PsicoderParser(stream)
    tree = parser.s()
    output = open("output.py","w")

    Traductor = PsicoderTraductorListener(output)
    walker = ParseTreeWalker()
    walker.walk(Traductor, tree)

    output.close()

if __name__ == '__main__':
    main(sys.argv)