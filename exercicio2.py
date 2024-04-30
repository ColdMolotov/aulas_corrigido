
primos_acima_de_100 = []


def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = 101
while len(primos_acima_de_100) < 10:
    if eh_primo(numero):
        primos_acima_de_100.append(numero)
    numero += 1

tupla_primos = tuple(primos_acima_de_100)


print("Os 10 primeiros números primos acima de 100 são:")
print(tupla_primos)
