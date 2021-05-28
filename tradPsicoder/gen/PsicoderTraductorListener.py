import sys
from antlr4 import *
from gen.PsicoderLexer import PsicoderLexer
from gen.PsicoderParser import PsicoderParser
from gen.PsicoderListener import PsicoderListener

class PsicoderTraductorListener(PsicoderListener) :
    def __init__(self, output):
        self.output = output
        self.output.write("wtf")
    def enterS(self, ctx:PsicoderParser.SContext) :
        self.output.write("Empece :)")
    def exitS(self, ctx:PsicoderParser.SContext) :
        self.output.write("Termine :( ")