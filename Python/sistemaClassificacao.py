idade = int(input())
x = 0
filmes = ["Shrek (2001)", "O Lar das Crianças Peculiares (2016)",
          "Pantera Negra (2018)", "Deadpool (2016)", "Kill Bill: Volume 1 (2003)"]

if idade < 12:
    x = 1
elif idade >= 12 and idade < 14:
    x = 2
elif idade >= 14 and idade < 16:
    x = 3
elif idade >= 16 and idade < 18:
    x = 4
elif idade >= 18:
    x = 5

print("Filmes que voce pode assistir:")
for i in range(x):
    print(filmes[i])
    i = i+1
