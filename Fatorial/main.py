#função fatorial
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n *calcular_fatorial(n-1)
#programa principal
n = int (input('Informe um número inteiro: '))

#exibe o resultado do fatorial
print(f"fatorial de {n}: {calcular_fatorial(n)}.")