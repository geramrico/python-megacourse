

#READING A FILE
'''myfile = open('fruits.txt')

print(myfile.read())     --> el cursos se va al final del
archivo txt. '''

#guarda el contenido en una variable para imprimir varias veces

''' content = myfile.read()'''

#Cierra el archivo para que deje de ocupar RAM

''' myfile.close()'''


with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

