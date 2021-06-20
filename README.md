# Traductor Psicoder -> Python3 

Esta aplicacion permite traducir del lenguaje Psicoder al lenguage Python3. Su uso es muy facil, simplemente es hacer doble click el ejecutable llamado "main" para correr la aplicación. Se abrira una ventana con dos bloques negros, el bloque de la izquierda es para que el usuario entre el codigo ya sea escribiendo directamente en el bloque o por medio del boton "De archivo" se puede elegir un archivo txt que tenga el codigo a traducir. Ya el usuario teniendo el codigo en el bloque izquierdo puede darle click en "Traducir :D", este boton hará que la respectiva traduccion del codigo aparezca en el bloque derecho de la pantalla, adicionalmente se crea un archivo de tipo .py del codigo de salida en la misma carpeta en donde se encuentra el ejecutable

```
funcion entero sum(entero a, entero b) hacer
    retornar a + b;
    // fin
fin_funcion

funcion_principal
  imprimir( sum(1,2));
fin_principal

estructura Point
    entero a;
    entero b;
fin_estructura

```

```python
##New python script
def sum(a,b) : 
 	return a+b

def main():
	print(sum(1,2))

if __name__ == '__main__':
	main() 

class Point: 
	a=0
	b=0


##Termine :)
```

link repositorio git: https://github.com/alzambranolu13/TraductorPsicoder
