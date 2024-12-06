import re
total=0
f=[]

def countXMAS(l):
	r1 = re.findall(r"XMAS",l)
	r2 = re.findall(r"XMAS",l[::-1])
	return len(r1)+len(r2)
	

with open("f4.txt") as file:
    for line in file:    	
    	f.append(line.strip())

#print(f)  
print("long" , len(f), len(f[0]))
#hor
for h in f:
    	total=total+countXMAS(h)
#print(total)

#ver
for v in range(0,len(f[0])):
	hl=""
	for l in f:
		hl=hl+l[v]
	total=total+countXMAS(hl)
#print(total)

#diago
for d in range(1,len(f)):
	print("diago" , d)
	hd=""
	for l in f:
		hd=hd+l[d]
		d=d+1
		if d >= len(f):
			break;
	print(hd)
	total=total+countXMAS(hd)
	
#diago
print("diago")
for d in range(0,len(f)):
	print("diago" , d)
	hd=""
	for l in f[::-1]:
		hd=hd+l[d]
		d=d+1
		if d >= len(f):
			break;
	print(hd)
	total=total+countXMAS(hd)

#diago2
#print("diago reves")
for d in range(1,len(f)):
	print("diago" , d)
	hd=""
	for l in f:
		hd=hd+l[len(f)-d-1]
		d=d+1
		if d >= len(f):
			break;
	print(hd)
	total=total+countXMAS(hd)

for d in range(0,len(f)):
	print("diago" , d)
	hd=""
	for l in f[::-1]:
		hd=hd+l[len(f)-d-1]
		d=d+1
		if d >= len(f):
			break;
	print(hd)
	total=total+countXMAS(hd)
print(total)


	
	

	

		
    		
