import numpy as np
t=0
with open("13.in") as file:
	a=b=r=False
	for line in file:
		line = line.strip()		
		if line.startswith("Button A: X+"):
			line=line.replace("Button A: X+", "")
			line=line.replace("Y+","")
			a1,a2=line.split(",")
			a1,a2=int(a1),int(a2)
			#print(a1,a2)			
			a=True
		if line.startswith("Button B: X+"):
			line=line.replace("Button B: X+", "")
			line=line.replace("Y+","")
			b1,b2=line.split(",")
			b1,b2=int(b1),int(b2)
			#print(b1,b2)	
			b=True
		if line.startswith("Prize: X="):
			line=line.replace("Prize: X=", "")
			line=line.replace("Y=","")
			r1,r2=line.split(",")
			r1 = int(r1)+10000000000000
			r2 = int(r2)+10000000000000
			r2 = int (r2)
			#print(r1,r2)
			r=True	
		if a and b and r:			
			a=b=r=False
			detm=a1*b2-b1*a2
			print("det" , detm)				
			sol1=(r1*b2)//detm - (r2*b1)//detm
			sol2=(a1*r2)//detm - (a2*r1)//detm
			print(sol1*a1+sol2*b1,r1)
			print(sol1*a2+sol2*b2,r2)
			if (sol1*a1 + sol2*b1==r1) and (sol1*a2 + sol2*b2==r2):
				print("Solucio")
				t=t+3*sol1 + 1*sol2
			#if sol[0].is_integer() and sol[1].is_integer() and sol[0]>=0 and sol[1]>=0:
			#if sol[0].is_integer() and sol[1].is_integer():
			#	print("la sumo" , sol)
			#	
	
						
print(t)	
#340240803616514	large
 103570327981381
#15601	low
		
