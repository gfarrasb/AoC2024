mapa=[]
pos=[94,73]
#pos=[6,4]
dir=[-1,0]
mides=[130,130]
posdif=[]

#5243 massa alt

def ShowMap():
	for e in mapa:
		print(e)
		
with open("f.txt") as file:
	for line in file:
		mapa.append(line.strip())

#print map
while pos[0]>=0 and pos[0]<mides[0]-1 and pos[1]>=0 and pos[1]<mides[1]-1:
	print(pos)	
	if mapa[pos[0]+dir[0]][pos[1]+dir[1]]!="#":
		pos[0]=pos[0]+dir[0]
		pos[1]=pos[1]+dir[1]
	else:
		if dir[0]==-1 and dir[1]==0:
			dir[0]=0
			dir[1]=1
		elif dir[0]==0 and dir[1]==1:
			dir[0]=1
			dir[1]=0
		elif dir[0]==0 and dir[1]==-1:
			dir[0]=-1
			dir[1]=0
		elif dir[0]==1 and dir[1]==0:
			dir[0]=0
			dir[1]=-1
print(pos)
			
		
