#Variable declaration
num1 = 42  #Data types: Primitive: Numbers
num2 = 2.3 #Data types: Primitive: Numbers
boolean = True #Data types: Primitive: boolean
string = 'Hello World' #Data types: Primitive: Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Data types: composite: list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Data types: composite: Dictonary
fruit = ('blueberry', 'strawberry', 'banana') #Data types: composite: tuples


print(type(fruit)) # log statement/ #Data types: composite: tuples
print(pizza_toppings[1]) # log statement/ #Data types: composite: list/ access value
pizza_toppings.append('Mushrooms')  # pizza_toppings es una lista/ append agrega un valor al final/  add value
print(person['name']) # log statement/  #Data types: composite: Dictonary/ access value
person['name'] = 'George' #Data types: composite: Dictonary/ change value 
person['eye_color'] = 'blue' #Data types: composite: Dictonary/ add value
print(fruit[2]) # log statement/ #Data types: composite: tuples/ access value

# conditional if - else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# conditional if - ifelese- else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#  for loop incrementa de 1. Considera desde el 0  y el numero 5 no es considerado, es hasta el 4. 
for x in range(5):
    print(x) # se imprime la variable x

#  for loop incrementa de 1. Considera desde el 2 (incluyendolo)  y el numero 5 no es considerado, es hasta el 4. 
for x in range(2,5):
    print(x)# se imprime la variable x

#  for loop incrementa de 3. Considera desde el 2 (incluyendolo)  hasta el numero 10 (no es considerado)  
for x in range(2,10,3):
    print(x)# se imprime la variable x


#while loop - incrementa de 1, parte del 0 hasta 5(no lo inclye)
x = 0
while(x < 5):
    print(x)
    x += 1

# POP remueve el ultimo elemento de esta lista/  #Data types: composite: list/ delete LAST element 
pizza_toppings.pop()
# POP(1) remueve el segundo elemento de esta lista/  #Data types: composite: list/ delete element con indice 1 
pizza_toppings.pop(1)


print(person)  # se imprime el diccionario
#Data types: composite: Dictonary/ delete value
person.pop('eye_color')
print(person) # se imprime el diccionario

print (pizza_toppings)

#for loo que recorre la lista
for topping in pizza_toppings:
    #if condicional, si el topping es pepperoni continua a los siguientes toppings 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    # hay tres toppigns siguientes antes de que sea olives, en olive se termina el for looop
    if topping == 'Olives':
        break

#Funcion imprime hello 10 veces. Gracias a la declaracion de range
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

print("primera funcion")

#Funcion imprime la cantidad que se le entregue en el (), ya que el range sera definido por ese valor.
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

print("segunda funcion")

#Funcion que si no contiene NADA en el () imprime 10 veces y si se le ingresa un numero en el (4) imprime las cantidades del numero. Las dos opciones en una.

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
""" #tirara error porque la variable esta definida despues de imprimirla
print(num3)
num3 = 72
"""

""" # No se puede cambiar un valor tupla
fruit[0] = 'cranberry'
"""
""" # no exite favorite_team "esa llave no esta definida"
print(person['favorite_team'])
"""
"""# list index out of range
print(pizza_toppings[7])
"""
"""Mal identado
    print(boolean)
"""
""" # AttributeError: 'tuple' object has no attribute 'append' no se puede modificar tupla
fruit.append('raspberry') 
"""

"""  AttributeError: 'tuple' object has no attribute 'pop' no se puede modificar tupla

fruit.pop(1)
"""
