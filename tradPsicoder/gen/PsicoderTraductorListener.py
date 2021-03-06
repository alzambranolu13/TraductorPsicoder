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
        pass


    def enterFuncion_principal(self, ctx: PsicoderParser.Funcion_principalContext):
        self.output.write("def main():\n")
        self.ntabs = self.ntabs + 1


    def enterDeclaracion(self, ctx: PsicoderParser.DeclaracionContext):
        self.printTabs()
        initvar=""
        if len(ctx.ID()) == 1:
            self.output.write(ctx.ID()[0].getText())
            if ctx.asignacion():
                self.output.write("=")
                if ctx.asignacion()[0].expr() != None:
                    self.output.write(ctx.asignacion()[0].expr().getText().replace("verdadero","True").replace("falso","False"))
                else:
                    tipo = ctx.tipo().getText()
                    if tipo == "entero":
                        initvar = "0"
                    elif tipo == "caracter":
                        initvar = "\'\'"
                    elif tipo == "cadena":
                        initvar = "\"\""
                    elif tipo == "real":
                        initvar = "0.0"
                    elif tipo == "booleano":
                        initvar = "True"
                    else:
                        initvar = tipo+'()'
                    self.output.write(initvar)
        else:
            variables = ctx.ID()
            for var in variables:
                self.output.write(var.getText())
                if var != variables[-1]:
                    self.output.write(", ")

            self.output.write(" = ")

            for i in range(0,len(variables)):
                if ctx.asignacion()[i].expr() != None:
                    self.output.write(ctx.asignacion()[i].expr().getText().replace("verdadero","True").replace("falso","False"))
                    if i != len(variables)-1:
                        self.output.write(", ")
                else:
                    tipo = ctx.tipo().getText()
                    if tipo == "entero":
                        initvar = "0"
                    elif tipo == "caracter":
                        initvar = "\'\'"
                    elif tipo == "cadena":
                        initvar = "\"\""
                    elif tipo == "real":
                        initvar = "0.0"
                    elif tipo == "booleano":
                        initvar = "verdadero"
                    else:
                        initvar = "None"
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
        cadena = ctx.expresion_logica().getText().replace("&&"," and ").replace("||"," or ").replace("verdadero","True").replace("falso","False")
        self.output.write(cadena)
        self.output.write(":\n")
        self.ntabs = self.ntabs + 1
        if (ctx.comandos().getText() == ''):
            self.printTabs()
            self.output.write("pass \n")


    def exitSi(self, ctx:PsicoderParser.SiContext):
        #self.ntabs = self.ntabs - 1
        pass

    def enterSi_no(self, ctx:PsicoderParser.Si_noContext):
        if ctx.getText() != "":
            self.ntabs = self.ntabs - 1
            self.printTabs()
            self.output.write("else")
            self.output.write(":\n")
            self.ntabs = self.ntabs + 1
            if (ctx.comandos().getText() == ''):
                self.printTabs()
                self.output.write("pass \n")
    
    def exitSi_no(self, ctx:PsicoderParser.Si_noContext):
        self.ntabs = self.ntabs - 1
    
    def enterAsignacion_id(self,ctx:PsicoderParser.AsignacionContext):
        self.printTabs()
        cadena = ctx.getText().replace(";","").replace("verdadero","True").replace("falso","False")
        self.output.write(cadena+"\n")

    
    def enterPara(self, ctx: PsicoderParser.ParaContext):
        self.printTabs()
        if (ctx.asignacion_entero() != None):
            declaracion= ctx.asignacion_entero().getText().replace("entero","")
        if (ctx.asignacion_id_para() != None):
            declaracion= ctx.asignacion_id_para().getText()
        self.output.write(declaracion + "\n")
        self.printTabs()
        self.output.write("while "+ ctx.expresion_logica().getText().replace("&&"," and ").replace("||"," or ").replace("verdadero","True").replace("falso","False") + ': \n')
        self.ntabs = self.ntabs + 1

    def exitPara(self, ctx:PsicoderParser.ParaContext):
        self.printTabs()
        if (ctx.asignacion_entero() != None):
            variable = ctx.asignacion_entero().ID().getText()
        if (ctx.asignacion_id_para() != None):
            variable = ctx.asignacion_id_para().ID().getText()

        if ctx.ID() != None:
            aumento= ctx.ID().getText()
        if ctx.INT() != None:
            aumento = ctx.INT().getText()

        self.output.write(variable + "+=" + aumento + "\n")

        self.ntabs = self.ntabs - 1

    def enterMientras(self, ctx:PsicoderParser.MientrasContext):
        self.printTabs()
        self.output.write("while " + ctx.expresion_logica().getText().replace("verdadero","True").replace("falso","False") + ': \n')
        self.ntabs = self.ntabs + 1

    def exitMientras(self, ctx:PsicoderParser.MientrasContext):
        self.ntabs = self.ntabs - 1

    def enterHacer_mientras(self, ctx:PsicoderParser.Hacer_mientrasContext):
        self.printTabs()
        self.output.write("while True:\n")
        self.ntabs = self.ntabs + 1

    def exitHacer_mientras(self, ctx:PsicoderParser.Hacer_mientrasContext):
        self.printTabs()
        condicion = ctx.expresion_logica().getText().replace("verdadero","True").replace("falso","False")
        self.output.write ( "if "+ condicion + ": \n \t" )
        self.printTabs()
        self.output.write("break \n")
        self.ntabs = self.ntabs - 1

    def enterLlamar_funcion(self, ctx:PsicoderParser.Llamar_funcionContext):
        self.printTabs()
        self.output.write(ctx.getText()+ "\n")

    variable = ''
    primero = ""
    def enterSeleccionar(self, ctx: PsicoderParser.SeleccionarContext):
        self.printTabs()
        global variable
        variable = ctx.ID().getText()
        self.output.write ( "if "+ variable + ": \n")
        self.ntabs = self.ntabs + 1
        global primero
        if ctx.casos().caso() != None:
            primero = ctx.casos().caso().expr().getText()

    
    def exitSeleccionar(self,ctx: PsicoderParser.SeleccionarContext):
        self.ntabs = self.ntabs - 1

    def enterCaso(self, ctx:PsicoderParser.CasosContext):
        self.printTabs()
        global variable
        global primero
        if ctx.expr().getText() == primero:
            self.output.write("if " + variable + "==" + ctx.expr().getText() + ": \n")
        else:
            self.output.write("elif " + variable + "==" + ctx.expr().getText() + ": \n")
        self.ntabs = self.ntabs + 1


    def exitCaso(self, ctx:PsicoderParser.CasosContext):
        self.ntabs = self.ntabs - 1


    def enterDefecto(self, ctx:PsicoderParser.DefectoContext):
        self.printTabs()
        self.output.write("else:\n")
        self.ntabs = self.ntabs + 1
        if (ctx.comandos().getText() == '' or ctx.comandos().getText() == 'romper;'):
            self.printTabs()
            self.output.write("pass\n")

    def exitDefecto(self, ctx:PsicoderParser.DefectoContext):
        self.ntabs = self.ntabs - 1

    def enterFuncion(self, ctx:PsicoderParser.FuncionContext):
        self.printTabs()
        self.output.write ('def '+ ctx.ID().getText() + '(')
        parametros = ctx.parametros().ID()
        for par in parametros:
            if par != parametros[-1]:
                self.output.write(par.getText() + ',')
            else:
                self.output.write(par.getText())
        self.output.write(') : \n ')
        self.ntabs = self.ntabs + 1

    def exitFuncion(self, ctx:PsicoderParser.FuncionContext):
        self.ntabs = self.ntabs - 1
        self.output.write('\n')

    def enterRetornar(self, ctx:PsicoderParser.RetornarContext):
        self.printTabs()
        self.output.write( ctx.getText().replace("retornar", "return ").replace(";","") + '\n')

    def enterEstructura(self, ctx:PsicoderParser.EstructuraContext):
        self.output.write('class '+ ctx.ID().getText() + ": \n")
        self.ntabs = self.ntabs + 1

    def exitEstructura(self, ctx:PsicoderParser.EstructuraContext):
        self.ntabs = self.ntabs - 1
        self.output.write('\n')


    def exitFuncion_principal(self, ctx: PsicoderParser.Funcion_principalContext):
        self.ntabs = 0
        self.output.write("\nif __name__ == '__main__':\n\tmain() \n\n")


    def exitS(self, ctx:PsicoderParser.SContext):

        self.output.write("\n##Termine :)\n ")