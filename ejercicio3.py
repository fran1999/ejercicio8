lista = ['Auto', '123', 'Viaje', '50', '120']
list = []
for each in lista:
	if each.isdecimal() :
		list.append((int(each)))
list.sort()
print(list)