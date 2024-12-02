import numpy as np

def isSafe(l):
	x=np.array(l)
	if (all(x[:-1] <= x[1:]) or all(x[:-1] >= x[1:])):
		ordered=True
	else:
		ordered=False
	if (ordered==True):
        	gradual=True
        	for e in range(0,len(l)-1):
        		dif=abs(l[e]-l[e+1])
        		if dif<1 or dif>3:
        			gradual=False
        	if gradual==True:
        		return True
        	else:
        		return False
	return False
        
	
total=0

with open("f.txt") as file:
    for line in file:
        report=line.rstrip().split(" ")
        linia=[]
        for e in report:
        	linia.append(int(e))
        	
        if isSafe(linia)==True:
        	print(linia, " Safe!")
        	total=total+1
        else:
        	for elem in range(0,len(linia)):
        		backuplinia = linia.copy()
        		del(backuplinia[elem])
        		print("analitzem" , backuplinia)
        		if isSafe(backuplinia)==True:
        			print(linia, " Safe if I remove" , elem)
        			total=total+1 
        			break 
        		print(linia)   	
        		      	 
print(total)
