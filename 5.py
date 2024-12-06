total=0
conditions=[]
pages=[]
condBool=True
with open("t.xt") as file:
	for line in file:
		if line.strip()=="":
			condBool=False    		   		
		if condBool:
			conditions.append(line.strip())
		else:
			if line.strip()!="":
				pages.append(line.strip().split(","))

for n in pages:
	correcta=0
	for e in range(0,len(n)-1):
		if (n[e+1]+"|"+n[e]) in conditions:
			correcta=correcta+1
	if correcta==0:
		print("",end='')
	else:
		#print("incorrecta2" , n)
		while correcta>0:
			for e in range(0,len(n)-1):
				if (n[e+1]+"|"+n[e]) in conditions:
					#print("Trenca2" , n[e+1]+"|"+n[e])
					n[e+1],n[e]=n[e],n[e+1]
					#print(n)
					correcta=correcta-1
					if correcta<0:
						correcta=0
			for t in range(0,len(n)-1):
				#print(n)
				#print(conditions)
				if (n[t+1]+"|"+n[t]) in conditions:
					#print("no entro??" + (n[t+1]+"|"+n[t]))
					correcta=correcta+1
					#print(correcta)		
	
		#print("arreglada " , n)				
		print( n[int(len(n)/2)] )
		
		
		
		
    

	

	
	
	

	

		
    		
