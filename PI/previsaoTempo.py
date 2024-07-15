tempo = input().lower()
graus = int(input())

if tempo == "chuvoso" and graus > 15:
    print("Sugiro assistir filmes")
elif tempo == "chuvoso" and graus <= 15:
    print("Sugiro chocolate quente")
elif tempo == "nublado" and graus >= 20:
    print("Sugiro museu")
elif tempo == "nublado" and graus <= 20:
    print("Sugiro shopping")
elif tempo == "ensolarado" and graus >= 30:
    print("Sugiro praia")
elif tempo == "ensolarado" and graus >= 20 and graus < 30:
    print("Sugiro parque")
elif tempo == "ensolarado" and graus < 20:
    print("Sugiro caminhada")
