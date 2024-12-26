from functools import lru_cache

@lru_cache(maxsize=None)
def compta(pedra, passos):
	if passos==0:
		return 1
	elif pedra==0:		
		return compta(1,passos-1)
	elif len(str(pedra))%2 == 0:
		mitat=int(len(str(pedra))/2)
		return compta(int(str(pedra)[0:mitat]), passos-1)+compta(int(str(pedra)[mitat::]), passos-1)
	else:
		return compta(int(pedra)*2024, passos-1)
		
inp="0 27 5409930 828979 4471 3 68524 170"
#inp="125 17"
ent=[int(x) for x in inp.split(" ")]
print(ent)
r=[compta(pedra,75) for pedra in ent]
print(sum(r))
