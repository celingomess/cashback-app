Questão 1


def calcular_cashback(valor_compra, percentual_cashback, é_vip=False, desconto=0):

  # 1. Aplicar desconto
  valor_final = valor_compra * (1 - desconto)

  # 2. Cashback base
  cashback = valor_final * percentual_cashback

  # 3. Regra de promoção (dobro)
  if valor_final > 500:
      cashback *= 2

  # 4. Bônus VIP (10% sobre o cashback)
  if é_vip:
      cashback *= 1.10

  return round(cashback, 2)


Questão 2 

Valor com Desconto: R$ 600,00 - 20% = R$ 480,00  

Cashback Base (5%): R$ 480,00 x 0,05 = R$ 24,00  

Bônus VIP (10% sobre base): R$ 24,00 x 0,10 = R$ 2,40 

Total: R$ 26,40. 

 

Questão 3 

Valor com Desconto: R$ 600,00 - 10% = R$ 540,00  

Cashback Base (5%): R$ 540,00 x 0,05 = R$ 27,00  

Promoção Dobra: R$ 27,00 x 2 = R$ 54,00  

Total: R$ 54,00  

 
Questão 4 

Valor Final: R$ 600,00 - 15% = R$ 510,00  

Cashback Base (5%): R$ 510,00 x 0,05 = R$ 25,50  

Bônus VIP (10% sobre base): R$ 25,50 x 0,10 = R$ 2,55  

Subtotal (Base + VIP): R$ 25,50 + R$ 2,55 = R$ 28,05 

Dobra da Promoção (Valor > R$ 500): R$ 28,05 x 2 = R$ 56,10
