print('ingrese un numers')
n = int(input())

print('precione 1 para sumar')
print('precione 2 para restar')
print('precione 3 para multiplicar')
print('precione 4 para dividir')

x = input()
print ('ingrese un numero para realizar la operacion')
m = int(input())
if x == '1' :
	print('entro')
	print(m+n)
elif x == '2' :
	print('entro')
	print(n-m)
elif x == '3' :
	print('entro')
	print(m*n)
elif x == '4' :
	 try:
	   print('entro')
	   print(n/m)
	 except ZeroDivisionError:
		 print ('No se permite la división por cero')
input()