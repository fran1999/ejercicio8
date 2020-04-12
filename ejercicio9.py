guesssesTaken = 0
print ('¡Hola! ¿Cuál es tu nombre?')
myName = input ()

número = random.randint (1, 20)
print ('Bueno,' + myName + ', estoy pensando en un número entre 1 y 20.')

print ('Adivina') # Cuatro espacios delante de "print"
guess = input ()
guess = int (guess)

if guess <número:
	print ('Your guess is too low')


if guess == number:
	break

if guess == number:
	guesssesTaken = str (guesssesTaken + 1)
	print ('Buen trabajo' + myName + '¡Adivinaste mi número en '+ 'conjeturas ¡Toma' +' conjeturas! ')

if guess != número:
	 número = str (número)
 	 print (' No, el número en el que estaba pensando era '+ número +'.')

