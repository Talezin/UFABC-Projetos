compra = float(input())
clienteOuro = input()
desconto = 0

if compra >= 1000 and compra < 10000:
    desconto = 5/100
elif compra >= 10000:
    desconto = 10/100
if clienteOuro.lower() == "s" and compra >= 50:
    desconto = desconto + 3/100

total = compra-(compra*desconto)

if clienteOuro.lower() == "s":
    print("Obrigado, cliente ouro")
    print("Valor final: R$%.2f" % total)
else:
    print("Valor final: R$%.2f" % total)
