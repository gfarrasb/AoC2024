import time

mapa=[]
mides=[52,52]

def trailExists(init,next):
	a=[init[0], init[1]+1]
	b=[init[0], init[1]-1]
	c=[init[0]-1, init[1]]
	d=[init[0]+1, init[1]]
	pos=[]
	#print("busquem " , next , " , des de " , init )
	if a[1]<mides[1]:
		if int(mapa[a[0]][a[1]])==next:
			pos.append([a[0], a[1]])
	if b[1]>=0:
		if int(mapa[b[0]][b[1]])==next:
			pos.append([b[0], b[1]])
	
	if c[0]>=0:
		if int(mapa[c[0]][c[1]])==next:
			pos.append([c[0], c[1]])
	if d[0]<mides[0]:
		if int(mapa[d[0]][d[1]])==next:
			pos.append([d[0], d[1]])
			
	#print("estem a trail i tenim " , pos, " per " , next )
	if len(pos) > 0 and next==9:
		#print("aqui entro oi?")
		for p in pos:
			if p not in iaqui:
				iaqui.append(p)
		#print(iaqui , " amb len de pos" , len(pos))
		if len(iaqui)>ntrails[actualn]:
			ntrails[actualn]=len(iaqui)			
		return True
		
	if len(pos) > 0 and next < 9:
		for e in pos:
			trailExists(e,next+1)


with open("10.in") as file:
	for line in file:
		mapa.append(line.strip())
#print(mapa)
inis=[]
for r in range(0,len(mapa)):
	for c in range(0,len(mapa[0])):
		if mapa[r][c]=='0':
			inis.append([r,c])
#print(inis)
ntrails=[]
actualn=0
for i in inis:
	n=1
	#time.sleep(2)
	#print("processem " , i)
	ntrails.append(0)
	iaqui=[]
	trailExists(i,n)
	actualn=actualn+1

for i in ntrails:
	print(i)

