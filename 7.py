total=0

def dec2tric(num):
    octal = ''
    while num > 0:
        octal = str(num % 3) + octal
        num //= 3
    return octal

with open("7.in") as file:
	for line in file:
		res,numbers = line.strip().split(": ")
		numbers=numbers.split(" ")
		#print(numbers)		
		for p in range(0,3**(len(numbers)-1)):
			t = int(numbers[0])
			#ops=bin(p)[2:].rjust(len(numbers)-1, '0')
			ops=dec2tric(p).rjust(len(numbers)-1, '0')
			#print("operacio" , ops)
			for op in range(0,len(ops)):
				if ops[op]=="0":
					t = int(t) + int(numbers[op+1])				
				elif ops[op]=="1":
					t = int(t) * int(numbers[op+1])
				elif ops[op]=="2":
					t = int(str(t) + numbers[op+1])
			#print(t)				
			if int(t)==int(res):
				print(res)
				total=total+int(t)
				break
		
print(total)
		
			
		
