amp=101
alc=103
pos=[]
vs=[]
fi=[]
with open("14.in") as file:
	for line in file:
		p,v = line.replace("p=", "").replace("v=","").strip().split()		
		p=list(map(int,p.split(",")))
		v=list(map(int,v.split(",")))
		pos.append(p)
		vs.append(v)
		
for sec in range(0,1000000):
	for p in range(0, len(pos)):
		pos[p][0]=(pos[p][0]+vs[p][0])%amp
		pos[p][1]=(pos[p][1]+vs[p][1])%amp
		#p[0]=(p[0]+v[0])%amp
		#p[1]=(p[1]+v[1])%alc
	
	if sec==8:	
		for x in range(0,amp):
			for y in range(0,alc):
				if [y,x] in pos:
					print("X",end='')
				else:
					print(".", end='')
			print("")
		
	q1=q2=q3=q4=0
	for f in pos:	
		if f[0]<amp//2 and f[1]<alc//2:
			q1=q1+1
		elif f[0]<amp//2 and f[1]>alc//2:
			q2=q2+1
		elif f[0]>amp//2 and f[1]>alc/2:
			q4=q4+1
		elif f[0]>amp//2 and f[1]<alc//2:
			q3=q3+1
	fi.append([sec,q1*q2*q2*q4])
	
print(fi)
mini=fi[0]
for i in fi:
	if i[1]<mini[1]:
		mini=i
print(mini)
	

	

