##New python script
def main():
	while True:
		a=a/2
		while a>0: 
		e: 
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
 