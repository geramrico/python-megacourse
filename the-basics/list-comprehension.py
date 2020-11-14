"""
temps = [221,234,120,432]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)


print(new_temps)

"""


#Hay una mejor manera más limpia, se genera la lista de manera dinámica.

temps = [221,234,120,432]

new_temps = [temp/10 for temp in temps]  #[temp/10 for temp in temps if condicion]  --> aplica agregar condicionales

print(new_temps)







