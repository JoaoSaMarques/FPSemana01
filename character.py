#Lista de criaturas
criaturas = []

#
for i in range(3):
    nome = input("Nome: ")
    vida = int(input("Vida: "))
    nível = int(input("Nível: "))
        
    criaturas.append([nome, (vida, nível)])

print(criaturas)

for i in range(len(criaturas)):
    for j in range(i + 1, len(criaturas)):
        if criaturas[i][1][1] < criaturas[j][1][1]:
            criaturas[i], criaturas[j] = criaturas[j], criaturas[i]  


for criatura in criaturas:
    print(criatura[0])