mapa=[]
ant=[]
anodes=[]
with open("8.in") as file:
	for line in file:
		mapa.append(line.strip())

mides=[len(mapa), len(mapa[0])]
print(mides)
for c in range(0,mides[0]):
	for r in range(0,mides[1]):
		if mapa[c][r] != ".":
			ant.append([mapa[c][r], c, r])
print(ant)
for a in range(0,len(ant)):
	for o in range(a+1, len(ant)):
		if ant[a][0] == ant[o][0]:
		
			if [ant[a][1],ant[a][2]] not in anodes:
				anodes.append([ant[a][1],ant[a][2]])
			
			if [ant[o][1],ant[o][2]] not in anodes:
				anodes.append([ant[o][1],ant[o][2]])
			
			print("calculem antinodes per " , ant[a], " i " , ant[o] )
			vect=[ant[a][1]-ant[o][1],ant[a][2]-ant[o][2]]	
			print(vect)
			n=1
			
			while ant[a][1]+(vect[0]*n)>=0 and ant[a][1]+(vect[0]*n)<mides[0] and ant[a][2]+(vect[1]*n)<mides[0] and ant[a][2]+(vect[1]*n)>=0:					
				antinode1=[ant[a][1]+vect[0]*n,ant[a][2]+vect[1]*n]
				print(antinode1)				
				if antinode1[0]>=0 and antinode1[0]<mides[0] and antinode1[1]<mides[0] and antinode1[1]>=0 and antinode1 not in anodes:
					anodes.append(antinode1)
				n=n+1
			n=1		
			while ant[o][1]-(vect[0]*n)>=0 and ant[o][1]-(vect[0]*n)<mides[0] and ant[o][2]-(vect[1]*n)<mides[0] and ant[o][2]-(vect[1]*n)>=0:					
				antinode2=[ant[o][1]-vect[0]*n,ant[o][2]-vect[1]*n]
				print(antinode2)				
				if antinode2[0]>=0 and antinode2[0]<mides[0] and antinode2[1]<mides[0] and antinode2[1]>=0 and antinode2 not in anodes:
					anodes.append(antinode2)			
				n=n+1


print(anodes)
print(len(anodes))
			
				
	
			

		
			
		
