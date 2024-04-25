def fatorial (n):
  if n == 0:
    return 1
  resultado = 1
  for i in range(1, n + 1):
    resultado *= i
  return resultado

def calcular_combinacoes(n, k):
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))

def calcular_probabilidade(n, k=1):
    return k / n


total_combinacoes = calcular_combinacoes(10, 3)
print("Total de combinações possíveis para escolher 3 ganhadores de 10 participantes:", total_combinacoes)

probabilidade = calcular_probabilidade(total_combinacoes,3)
print("Probabilidade de uma combinação específica ser sorteada:", f"{probabilidade:.2%}")
