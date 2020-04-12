import math
s = input()
def es_primo(a):
	if a == 2:
		return True
	n=2
	while n <= math.sqrt(a):
		if (a % n) == 0 :
			return False
		else:
			n+=1
	return True
list = {}
for i in s:
	if i in list:
		list[i]+=1
	else:
		list[i]=1

print(list)
input()
for i,j in list.items():
	if es_primo(j) :
		print('es primo '+i)
	
		