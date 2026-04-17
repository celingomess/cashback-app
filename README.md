Questão 1


def calcular_cashback(valor_compra, percentual_cashback, is_vip=False, desconto=0):
    # 1. Aplicar desconto
    valor_final = valor_compra * (1 - desconto)
    cashback = valor_final * percentual_cashback
    # 3. Regra de promoção (dobro)
    if valor_final > 500:
        cashback *= 2
    # 4. Bônus VIP (10% sobre o cashback)
    if is_vip:
        cashback *= 1.10
    return round(cashback, 2)
