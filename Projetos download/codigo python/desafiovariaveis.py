id = int
nome = str
salario = float
brasileiro = bool

id = int(input("Informe o ID: "))
nome = input("Informe o nome: ")
salario = float(input("Informe o salário "))
brasileiro = bool(input("Digite sim caso seja brasileiro e não, caso contrário: "))

print("\nInformações inseridas:")
print(f"ID: {id}")
print(f"Nome: {nome}")
print(f"Salário: {salario: .3f}")
print(f"Brasileiro: {brasileiro}")
