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
6. Entrada
```
funcion entero sum(entero a, entero b) hacer
    a = a + b;
fin_funcion

funcion_principal

    imprimir (sum(3,5));

fin_principal
```
Salida
```python
##New python script
def sum(a,b) : 
 	a=a+b
	

def main():
	print(sum(3,5))

if __name__ == '__main__':
	main() 


##Termine :)
 
```
7. Entrada
```
funcion_principal
    entero tipo = 0;
    entero option = 0;
    entero altura;
    real radio ;
     entero base;
     entero lado;
     entero baseMayor;
     entero baseMenor;
    entero arista;
    imprimir("0 Area volumen");
    leer(tipo);
    seleccionar ( tipo ) entre
        caso 0 :
            imprimir("0 Triangulo Cuadrado Circulo Trapecio");
            leer(option);
            seleccionar ( option ) entre
                caso 0 :

                    imprimir("ingrese la base");
                    leer(base);
                    imprimir("ingrese la altura");
                    leer(altura);
                    imprimir(base*altura/2);
                caso 1 :
                   imprimir("ingrese el lado");
                    leer(lado);
                    imprimir(lado*lado);
                caso 2 :
                    imprimir("ingrese el radio");
                    leer(radio);
                    imprimir(3.14 * radio*radio);

                caso 3 :
                    imprimir("ingrese la base mayor");
                    leer(baseMayor);
                    imprimir("ingrese la base menor");
                    leer(baseMenor);
                    imprimir("ingrese la altura");
                    leer(altura);
                    imprimir((baseMayor+baseMenor)/2 * altura);
                defecto:
            fin_seleccionar

        caso 1 :
            imprimir(" Piramide Cubo Esfera");
            leer(option);
            seleccionar ( option ) entre
                caso 0 :
                    imprimir("ingrese la arista");
                    leer(arista);
                    imprimir("ingrese la altura");
                    leer(altura);
                    imprimir(arista*altura/3);
                caso 1 :
                    imprimir("ingrese el lado");
                    leer(lado);
                    imprimir(lado*lado*lado);
                caso 2 :
                    imprimir("ingrese el radio");
                    leer(radio);
                    imprimir(4/3 * 3.14 * radio*radio*radio);
            fin_seleccionar

        defecto:

    fin_seleccionar


fin_principal
```
Salida
```python
##New python script
def main():
	tipo=0
	option=0
	altura=0
	radio=0.0
	base=0
	lado=0
	baseMayor=0
	baseMenor=0
	arista=0
	print("0 Area volumen")
	tipo = input()
	if tipo: 
		if tipo==0: 
			print("0 Triangulo Cuadrado Circulo Trapecio")
			option = input()
			if option: 
				if option==0: 
					print("ingrese la base")
					base = input()
					print("ingrese la altura")
					altura = input()
					print(base*altura/2)
				elif option==1: 
					print("ingrese el lado")
					lado = input()
					print(lado*lado)
				elif option==2: 
					print("ingrese el radio")
					radio = input()
					print(3.14*radio*radio)
				elif option==3: 
					print("ingrese la base mayor")
					baseMayor = input()
					print("ingrese la base menor")
					baseMenor = input()
					print("ingrese la altura")
					altura = input()
					print((baseMayor+baseMenor)/2*altura)
				else:
					pass
		elif option==1: 
			print(" Piramide Cubo Esfera")
			option = input()
			if option: 
				if option==0: 
					print("ingrese la arista")
					arista = input()
					print("ingrese la altura")
					altura = input()
					print(arista*altura/3)
				elif option==1: 
					print("ingrese el lado")
					lado = input()
					print(lado*lado*lado)
				elif option==2: 
					print("ingrese el radio")
					radio = input()
					print(4/3*3.14*radio*radio*radio)
		else:
			pass

if __name__ == '__main__':
	main() 


##Termine :)
```
8. Entrada
```
funcion_principal

    entero n;
    booleano flag = falso;
    leer( n );
    real x,y= 0;
    cadena s = false;

    imprimir();



fin_principal
```
Salida
```python
##New python script
def main():
	n=0
	flag=False
	n = input()
	x, y = 0.0, 0
	s=false
	print()

if __name__ == '__main__':
	main() 


##Termine :)
```
9. Entrada
```
funcion_principal
    entero a;
    real x,y= 0,0;
fin_principal
```
Salida
```python
##New python script
def main():
	a=0
	x, y = 0, 0

if __name__ == '__main__':
	main() 


##Termine :)
 
```
10. Entrada
```
//Estructura
//Conceptos Basicos

estructura Fecha
    entero dd;
    entero mm;
    entero aa;
fin_estructura

estructura Estudiante
    cadena cedula;
    cadena nombre;
    entero edad;
    real definitiva;
    Fecha fingreso;
fin_estructura

funcion_principal
    Estudiante estudiante;
    entero opcion;

    hacer
        opcion = menu();
        seleccionar ( opcion ) entre
           caso 1 : estudiante = capturar(estudiante);
                    romper;
           caso 2 : mostrar(estudiante);
                    romper;
           caso 3 : romper;
           defecto :imprimir("Digite una opcion entre 1 y 3 ");
                    romper;
       fin_seleccionar
    mientras ( opcion != 3) ;
fin_principal

funcion entero menu() hacer
    entero opcion;
    imprimir("menu de estructuras ");
    imprimir("1  Capturar el registro ");
    imprimir(" 2 Imprimir el registro ");
    imprimir(" 3  Salir ");
    imprimir(" digite su opcion entre 1 y 3  ");
    leer (opcion);
    retornar opcion;
fin_funcion

funcion Estudiante capturar(Estudiante estudiante) hacer
  entero i;
  real def = 0.0;
  imprimir("digite la cedula del estudiante  ");
  leer(estudiante.cedula);
  imprimir("digite el nombre del estudiante ");
  leer(estudiante.nombre);

  para(i=0; i<3; 1) hacer
    imprimir ("digite la nota ",i+1, " del estudiante");
    leer(estudiante.nota);
    def = def + estudiante.nota;
  fin_para

  imprimir("digite la edad del estudiante ");
  leer(estudiante.edad);
  estudiante.definitiva = def / 3;

  imprimir("digite el dia de ingreso a la Universidad ");
  leer(estudiante.fingreso.dd);
  imprimir("digite el mes de ingreso a la Universidad  ");
  leer(estudiante.fingreso.mm);
  imprimir("digite el ako de ingreso a la Universidad  ");
  leer(estudiante.fingreso.aa);
  retornar estudiante;
fin_funcion

funcion entero mostrar(Estudiante estudiante) hacer
  entero i;
  imprimir("");
  imprimir("Cedula  ", estudiante.cedula);
  imprimir("Nombre  ", estudiante.nombre,"");
  para (i=0; i<3; 1) hacer
    imprimir("Nota ",estudiante.nota, " ");
  fin_para
  imprimir("Edad  ",estudiante.edad);
  imprimir("Definitiva  ",estudiante.definitiva);
  imprimir("Fecha de Ingreso ddmmaaaa  ",estudiante.fingreso.dd,estudiante.fingreso.mm,estudiante.fingreso.aa);
  retornar i;
fin_funcion

```
Salida
```python
##New python script
class Fecha: 
	dd=0
	mm=0
	aa=0

class Estudiante: 
	cedula=""
	nombre=""
	edad=0
	definitiva=0.0
	fingreso=Fecha()

def main():
	estudiante=Estudiante()
	opcion=0
	while True:
		opcion=menu()
		if opcion: 
			if opcion==1: 
				estudiante=capturar(estudiante)
			elif opcion==2: 
				mostrar(estudiante);
			elif opcion==3: 
			else:
				print("Digite una opcion entre 1 y 3 ")
		if opcion!=3: 
 			break 

if __name__ == '__main__':
	main() 

def menu() : 
 	opcion=0
	print("menu de estructuras ")
	print("1  Capturar el registro ")
	print(" 2 Imprimir el registro ")
	print(" 3  Salir ")
	print(" digite su opcion entre 1 y 3  ")
	opcion = input()
	return opcion

def capturar(estudiante) : 
 	i=0
	def=0.0
	print("digite la cedula del estudiante  ")
	estudiante.cedula = input()
	print("digite el nombre del estudiante ")
	estudiante.nombre = input()
	i=0
	while i<3: 
		print("digite la nota ",i+1," del estudiante")
		estudiante.nota = input()
		def=def+estudiante.nota
		i+=1
	print("digite la edad del estudiante ")
	estudiante.edad = input()
	estudiante.definitiva=def/3
	print("digite el dia de ingreso a la Universidad ")
	estudiante.fingreso.dd = input()
	print("digite el mes de ingreso a la Universidad  ")
	estudiante.fingreso.mm = input()
	print("digite el ako de ingreso a la Universidad  ")
	estudiante.fingreso.aa = input()
	return estudiante

def mostrar(estudiante) : 
 	i=0
	print("")
	print("Cedula  ",estudiante.cedula)
	print("Nombre  ",estudiante.nombre,"")
	i=0
	while i<3: 
		print("Nota ",estudiante.nota," ")
		i+=1
	print("Edad  ",estudiante.edad)
	print("Definitiva  ",estudiante.definitiva)
	print("Fecha de Ingreso ddmmaaaa  ",estudiante.fingreso.dd,estudiante.fingreso.mm,estudiante.fingreso.aa)
	return i


##Termine :)
 
```




link repositorio git: https://github.com/alzambranolu13/TraductorPsicoder
