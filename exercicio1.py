tupla = ()
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    tupla += (elemento,)

print("Tupla na ordem inversa:")
for elemento in reversed(tupla):
    print(elemento)
