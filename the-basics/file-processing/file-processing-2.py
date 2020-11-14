'''with open("fruits.txt","r") as myfile:
    content = myfile.read()
    pass'''


#Crea documento vegetales con la funcion open y el modo W (writing)

'''with open("vegetales.txt","w") as myfile:
    myfile.write("Tomate")'''

#agregaría las cosas juntas si no agregsa /n o espacios, etc


with open("fruits.txt","a+") as mifile:
    mifile.write("\nOkra")
    mifile.seek(0)
    content = mifile.read()

print(content)