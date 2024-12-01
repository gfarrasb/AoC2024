left=[]
right=[]
with open('f.txt') as fp:
    for line in fp:
        a,b=line.split("   ")
        left.append(int(a))
        right.append(int(b))


#Part 1
left.sort()
right.sort()
d=0
for i in range(0,len(left)):
	#print(abs(left[i]-right[i]))
	d = d + abs(left[i]-right[i])
print("Part 1 " , d)

#Part 2
s=0
for i in range(0,len(left)):
	print(left[i]*(right.count(left[i])))
	s = s + left[i]*(right.count(left[i]))
print("Part 2 " , s)
	
	

