criaturas = []

for i in range(3):
    nome = input("Nome: ")
    vida = int(input("Vida: "))
    nível = int(input("Nível: "))
        
    criaturas.append([nome, (vida, nível)])

print(criaturas)


criaturas.sort(key=lambda x: x[1][1], reverse=True)


for criatura in criaturas:
    print(criatura[0])