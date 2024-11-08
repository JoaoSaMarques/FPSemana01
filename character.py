#Lista de criaturas
criaturas = []

# input para cada monstro até termos 3
for i in range(3):
    nome = input("Nome: ")
    vida = int(input("Vida: "))
    nível = int(input("Nível: "))
        
    #organiza os monstros
    criaturas.append([nome, (vida, nível)])

#Monstra os montros na consola
print(criaturas)

#organiza por nível
for i in range(len(criaturas)):
    for j in range(i + 1, len(criaturas)):
        if criaturas[i][1][1] < criaturas[j][1][1]:
            criaturas[i], criaturas[j] = criaturas[j], criaturas[i]  

#por cada organização, faz print descente
for criatura in criaturas:
    print(criatura[0])