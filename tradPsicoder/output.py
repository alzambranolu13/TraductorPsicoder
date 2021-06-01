##New python script
##Empece :)
def main():
	n=0
	flag=False
	n = input()
	i=2
	while i<n: 
		if n%i==0:
			print("no es primo")
			flag=True
		i+=1
	if flag==False:
		print("es primo")
	else:
		pass 
if __name__ == '__main__':
	main()
##Termine :(
