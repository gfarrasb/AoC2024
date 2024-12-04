import re
total=0
switch=True
with open("f.txt") as file:
    for line in file:
    	#print(line)
    	r1 = re.findall(r"mul\(\d{0,9},\d{0,9}\)|don't\(\)|do\(\)",line)
    	print(r1)    	
    	for e in r1:
    		if e.startswith("don"):
    			switch=False
    		elif e.startswith("do("):
    			switch=True
    		elif e.startswith("mul"):
	    		e=e.replace('mul(','')
    			e=e.replace(')','')
    			print(e, switch)
    			a,b=e.split(",")
    			if int(a)<=1000 and int(b)<=1000 and switch==True:
    				total=total+int(a)*int(b)
print("el resultat es " , total)
    		
