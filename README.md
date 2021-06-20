# Traductor Psicoder -> Python3 

Esta aplicacion permite traducir del lenguaje Psicoder al lenguage Python3. Su uso es muy facil, simplemente es hacer doble click el ejecutable llamado "main" para correr la aplicación. Se abrira una ventana con dos bloques negros, el bloque de la izquierda es para que el usuario entre el codigo ya sea escribiendo directamente en el bloque o por medio del boton "De archivo" se puede elegir un archivo txt que tenga el codigo a traducir. Ya el usuario teniendo el codigo en el bloque izquierdo puede darle click en "Traducir :D", este boton hará que la respectiva traduccion del codigo aparezca en el bloque derecho de la pantalla, adicionalmente se crea un archivo de tipo .py del codigo de salida en la misma carpeta en donde se encuentra el ejecutable


Ahora presentaremos 10 casos de prueba del traductor

1. Entrada
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
Salida
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

2. Entrada 
```
funcion_principal
    si ( num1 > num2 ) entonces
       res = num1;
       si( res == b ) entonces
            imprimir("Test if");
        si_no
            imprimir("Test sino");
        fin_si
    si_no
       res = num2;
    fin_si

    si ( num1 > num2 ) entonces
       res = num1;
       si( res == b ) entonces
            imprimir("Test if");
       fin_si
    si_no
       res = num2;
    fin_si
fin_principal
```
Salida

```python
##New python script
def main():
	if num1>num2:
		res=num1
		if res==b:
			print("Test if")
		else:
			print("Test sino")
	else:
		res=num2
	if num1>num2:
		res=num1
		if res==b:
			print("Test if")
	else:
		res=num2

if __name__ == '__main__':
	main() 


##Termine :)
```

3. Entrada

```
//Mayor entre 2 numeros - Funciones
//Llamado a una Función, valor de retorno

funcion_principal
    entero num1,num2,may;
    imprimir( "digite un numero entero positivo " );
    leer( num1 );
    imprimir( "digite un numero entero positivo " );
    leer( num2 );
    may = mayor(num1,num2);
    imprimir ("El numero mayor es ", may);
fin_principal

funcion entero mayor(entero num1, entero num2) hacer
    entero res;
    si ( num1 > num2 ) entonces
       res = num1;
    si_no
       res = num2;
    fin_si
    retornar res;
fin_funcion
```
Salida

```python 
##New python script
def main():
	num1, num2, may = 0, 0, 0
	print("digite un numero entero positivo ")
	num1 = input()
	print("digite un numero entero positivo ")
	num2 = input()
	may=mayor(num1,num2)
	print("El numero mayor es ",may)

if __name__ == '__main__':
	main() 

def mayor(num1,num2) : 
 	res=0
	if num1>num2:
		res=num1
	else:
		res=num2
	return res


##Termine :)
```

4. Entrada
```
funcion_principal
    entero a = 3;
    entero p = 2;
    entero j = 2;
    para ( entero i = 0 ; i < a ; 1 ) hacer
        imprimir(i);
    fin_para

    para ( j = 0 ; i < a || j  < 100  ; p ) hacer
        imprimir(j);
    fin_para
fin_principal
```
Salida
```python
##New python script
def main():
	a=3
	p=2
	j=2
	i=0
	while i<a: 
		print(i)
		i+=1
	j=0
	while i<a or j<100: 
		print(j)
		j+=p

if __name__ == '__main__':
	main() 


##Termine :)
```

5. Entrada

```
funcion_principal
    entero a = 3;
    leer(a);
    seleccionar ( a ) entre
        caso 0 :
            imprimir(a);
            romper;
        caso 1:
            imprimir(a*2);
            romper;
        defecto:
    fin_seleccionar
fin_principal
```
Salida
```python
##New python script
def main():
	a=3
	a = input()
	if a: 
		if a==0: 
			print(a)
		elif a==1: 
			print(a*2)
		else:
			pass

if __name__ == '__main__':
	main() 


##Termine :)
```





link repositorio git: https://github.com/alzambranolu13/TraductorPsicoder
