import re
total=0
f=[]

total=0
with open("f4.txt") as file:
    for line in file:    	
    	f.append(line.strip())
    
for l in range(1,len(f)-1):
	print(l)
	c=1
	a=0
	cros1=cros2=""
	a = f[l].find("A",c,len(f[l])-1)
	c = a + 1
	while a!=-1:
		cros1=f[l-1][a-1] + f[l][a] + f[l+1][a+1]
		cros2=f[l-1][a+1] + f[l][a] + f[l+1][a-1]
		print(cros2, " " , ''.join(sorted(cros2)))
		if ''.join(sorted(cros1))=="AMS" and ''.join(sorted(cros2))=="AMS":
			total=total+1
		a = f[l].find("A",c,len(f[l])-1)
		c = a + 1
	
print(total)
	

	
	
	

	

		
    		
