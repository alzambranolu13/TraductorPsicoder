import sys
from antlr4 import *
from gen.PsicoderLexer import PsicoderLexer
from gen.PsicoderParser import PsicoderParser
from gen.PsicoderListener import PsicoderListener

class PsicoderTraductorListener(PsicoderListener):
    def __init__(self, output):
        self.output = output
        self.ntabs = 0
        self.output.write("##New python script\n")

    def printTabs(self):
        for n in range(0,self.ntabs):
            self.output.write("\t")

    def enterS(self, ctx:PsicoderParser.SContext):
        self.output.write("##Empece :)\n")

    def enterFuncion_principal(self, ctx: PsicoderParser.Funcion_principalContext):
        self.output.write("def main():\n")
        self.ntabs = self.ntabs + 1


    def enterDeclaracion(self, ctx: PsicoderParser.DeclaracionContext):
        self.printTabs()
        if len(ctx.ID()) == 1:
            self.output.write(ctx.ID()[0].getText())
            if ctx.asignacion():
                self.output.write("=")
                self.output.write(ctx.asignacion()[0].expr().getText())
        else:
            variables = ctx.ID()
            for var in variables:
                self.output.write(var.getText())
                if var != variables[-1]:
                    self.output.write(", ")

            self.output.write(" = ")

            for i in range(0,len(variables)):
                if ctx.asignacion()[i].expr() != None:
                    self.output.write(ctx.asignacion()[i].expr().getText())
                    if i != len(variables)-1:
                        self.output.write(", ")
                else:
                    tipo = ctx.tipo().getText()
                    if tipo == "entero":
                        initvar = "0"
                    if tipo == "caracter":
                        initvar = "\'\'"
                    if tipo == "cadena":
                        initvar = "\"\""
                    if tipo == "real":
                        initvar = "0.0"
                    if tipo == "booleano":
                        initvar = "verdadero"
                    self.output.write(initvar)
                    if i != len(variables)-1:
                        self.output.write(", ")
        self.output.write("\n")

    def enterLeer(self,ctx: PsicoderParser.LeerContext):
        self.printTabs()
        self.output.write(ctx.id_pos_estruct().getText())
        self.output.write(" = input()\n")

    def enterImprimir(self, ctx: PsicoderParser.ImprimirContext):
        self.printTabs()
        self.output.write("print(")
        cadena = ctx.getText()[9:-1]
        self.output.write(cadena + "\n")
        

    def enterSi(self, ctx: PsicoderParser.SiContext):
        self.printTabs()
        self.output.write("if ")
        cadena = ctx.expresion_logica().getText().replace("&&"," and ").replace("||"," or ")
        self.output.write(cadena)
        self.output.write(":\n")
        self.ntabs = self.ntabs + 1

    def exitSi(self, ctx:PsicoderParser.SiContext):
        self.ntabs = self.ntabs - 1
    
    def enterSi_no(self, ctx:PsicoderParser.Si_noContext):
        pass

    def exitFuncion_principal(self, ctx: PsicoderParser.Funcion_principalContext):
        self.ntabs = 0
        self.output.write("if __name__ == '__main__':\n\tmain()")


    def exitS(self, ctx:PsicoderParser.SContext):
        self.output.write("\n##Termine :(\n")