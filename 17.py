import sys
A=B=C=0
A=37293246
iniA=483630
iniA=3831800
#print(oct(iniA))
pc=0
ins=[2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0]
def retoperand(a):
	if a==0 or a==1 or a==2 or a==3:
		return int(a)
	elif a==4:
		return int(A)
	elif a==5:
		return int(B)
	elif a==6:
		return int(C)
	
trobat=False
while trobat==False:
	ret=[]
	pc=0
	print("Analitzem amb A " , iniA)
	A=int(str(iniA)+"00000000")
	while pc<len(ins):	
		if ins[pc]==0:	#adv
			A=A//(2**retoperand(ins[pc+1]))
			pc=pc+2
		elif ins[pc]==1:	#bitwise XOR
			B=B^ins[pc+1]
			pc=pc+2
		elif ins[pc]==2:	#bst
			B=retoperand(ins[pc+1])%8
			pc=pc+2
		elif ins[pc]==3:	#jnz
			if A!=0:
				pc=ins[pc+1]
			else:
				pc=pc+2
		elif ins[pc]==4:	#bxc
			B=B^C
			pc=pc+2
		elif ins[pc]==5:	#out
			ret.append(retoperand(ins[pc+1])%8)
			pc=pc+2
		elif ins[pc]==6:	#bdv	
			B=A//(2**retoperand(ins[pc+1]))
			pc=pc+2
		elif ins[pc]==7:	#cdv	
			C=A//(2**retoperand(ins[pc+1]))
			pc=pc+2
	print(ret)
	iniA=iniA+1
	if ret[-4::]==ins[-4::]:
		trobat=True
		print("Trobat a A=", iniA)
		break
	


	

	

