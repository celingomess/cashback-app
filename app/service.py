def calcular_cashback(valor):
    if valor >= 500:
        return valor * 0.10
    elif valor >= 200:
        return valor * 0.05
    else:
        return valor * 0.02