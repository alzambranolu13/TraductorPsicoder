import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from antlr4 import *
from gen.PsicoderLexer import PsicoderLexer
from gen.PsicoderParser import PsicoderParser
from gen.PsicoderTraductorListener import PsicoderTraductorListener




def main(argv):
    ##GUI
    window = tk.Tk()
    window.geometry("1280x720")
    window.configure(bg = 'beige')
    window.title('Traductor Psicoder-Python3')
    #Titles
    fuenteTitulo = ("Consolas","25")
    fuenteSubtitulo = ("Consolas","20")
    titulo = tk.Label(window,text = 'Traductor Psicoder',font =fuenteTitulo)
    subtitulo = tk.Label(window,text = 'por Diego Bayona y Alejandra Zambrano',font=fuenteSubtitulo)
    titulo.grid(column=0,row=0)
    subtitulo.grid(column=0 ,row=1)
    marcoCode = ttk.Frame(window,borderwidth=2,relief="ridge",padding=(10,10))
    marcoCodetrad = ttk.Frame(window,borderwidth=2,relief="ridge",padding=(10,10))
    marcoButtons = ttk.Frame(window,borderwidth=2,relief="ridge",padding=(5,5))
    #Psicoder text
    fuentecode = ("Consolas","15")
    tPsicoder = tk.Text(marcoCode,width=50,height=20,bg="#16172B",fg="#8A8AA7")
    tPsicoder.grid(column=0,row=0)
    tPsicoder.configure(font = fuentecode)
    def openFilePsicoder():
        #Clean TextField
        tPsicoder.delete("1.0",tk.END)
        #Open file
        filetypes = (("text files","*.txt"),("All files","*.*"))
        file = fd.askopenfile(filetypes=filetypes)
        tPsicoder.insert("1.0",file.read())
    bPsicoder = ttk.Button(marcoButtons,text="De archivo...",command=openFilePsicoder)
    bPsicoder.grid(column=0,row=1)


    


    #Texto traducido a python
    
    tPython = tk.Text(marcoCodetrad,width=50,height=20,bg="#16172B",fg="#8A8AA7")
    tPython.grid(column=0,row=0)
    tPython.configure(font = fuentecode)
    #traduccion
    def Traducir():
        #Clean TextField
        tPython.delete("1.0",tk.END)
        #Take text in input Psicoder
        code = tPsicoder.get("1.0",tk.END)
        lexer = PsicoderLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        parser = PsicoderParser(stream)
        tree = parser.s()
        codepython = open("output.py","w")
        Traductor = PsicoderTraductorListener(codepython)
        walker = ParseTreeWalker()
        walker.walk(Traductor, tree)
        codepython.close()
        with open("output.py", "r") as codepython:
            tPython.insert("1.0",codepython.read())
        

    btrad = ttk.Button(marcoButtons,text="Traducir :D",command=Traducir)
    btrad.grid(column=1,row=1)

    #exit button
    bsalir= ttk.Button(marcoButtons,text="Salir",command=window.destroy)
    bsalir.grid(column=0,row=2)

    
    marcoCode.grid(column=0,row=2)
    marcoCodetrad.grid(column=2,row=2)
    marcoButtons.grid(column=1,row=2)

    #run GUI
    window.mainloop()




    ##Logic
    input = FileStream("input.txt")
    print(type(input))
    lexer = PsicoderLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PsicoderParser(stream)
    tree = parser.s()
    output = open("output.py","w")
    print(type(output))
    Traductor = PsicoderTraductorListener(output)
    walker = ParseTreeWalker()
    walker.walk(Traductor, tree)

    output.close()

if __name__ == '__main__':
    main(sys.argv)