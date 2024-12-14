with open("9.in") as file:
	for line in file:
		mapa=line.strip()
disc=[]
id=0
files=[]
for e in range(0,len(mapa)):
	if e%2!=0:
		for p in range(0,int(mapa[e])):
			disc.append(".")	
	else:
		for p in range(0,int(mapa[e])):
			disc.append(id)
		files.insert(0,[id, int(mapa[e]), len(disc)-int(mapa[e])])
		id=id+1	
print(disc)
print(files)
for f in files:
	print("processs , " , f)
	p=0
	canviat=False
	while p<f[2] and canviat==False:
		if disc[p]==".":
			t=0
			while disc[p+t]==".":
				t=t+1
			print("hem trobat " , t , " punts continues comencant a " ,  p)
			if t >= f[1]:
				print("CANVI")
				canviat=True				
				for i in range(0,f[1]):
					disc[p+i]=f[0]
				for i in range(0,f[1]):
					disc[ f[2] + i ]='.'
				print(disc)
		p=p+1

print(disc)
#too low 111277776728
t=0
for i in range(0,len(disc)):
	if disc[i] != ".":
		t=t+(i*disc[i])
print(t)
	
		
	
			
	
		




	



