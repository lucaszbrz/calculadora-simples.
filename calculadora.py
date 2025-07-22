def bemvindo():
    print("Bem-vindo à Calculadora! ")

def menu():
    print("Escolha uma opção:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    opcao = input("Digite o número da opção: ")
    if opcao == "5":
        return opcao, 0
    quantidade_numeros = int(input("Quantos números você quer calcular? "))
    return opcao, quantidade_numeros

lista_de_opções = ["1", "2", "3", "4", "5"]

def operações(opcao, quantidade_numeros):
    if opcao not in lista_de_opções:
        print("Opção inválida. Tente novamente.")
        return
    if opcao == "1":
        resultado = 0
        for i in range(1, quantidade_numeros + 1):
            numero = float(input(f"Digite o {i}º número: "))
            resultado += numero
        print(f"O resultado da adição é: {resultado}\n")
        deseja_continuar = input("Deseja continuar? (s/n): ").lower()
        if deseja_continuar in ["s", "sim"]:
                print("Continuando...")
        elif deseja_continuar in ["n", "não"]:
                print("Saindo da calculadora. Até logo!\n")
                exit()
        while deseja_continuar not in ["s", "n", "sim", "não"]:
            print("Opção inválida. Por favor.")
            deseja_continuar = input("Deseja continuar? (s/n): ").lower()
    elif opcao == "2":
        resultado = float(input("Digite o 1º número: "))
        for i in range(2, quantidade_numeros + 1):
            numero = float(input(f"Digite o {i}º número: "))
            resultado -= numero
        print(f"O resultado da subtração é: {resultado}\n")
        deseja_continuar = input("Deseja continuar? (s/n): ").lower()
        if deseja_continuar in ["s", "sim"]:
                print("Continuando...")
        elif deseja_continuar in ["n", "não"]:
                print("Saindo da calculadora. Até logo!\n")
                exit()
        while deseja_continuar not in ["s", "n", "sim", "não"]:
            print("Opção inválida. Por favor.")
            deseja_continuar = input("Deseja continuar? (s/n): ").lower()
    elif opcao == "3":
        resultado = float(input("Digite o 1º número: "))
        for i in range(2, quantidade_numeros + 1):
            numero = float(input(f"Digite o {i}º número: "))
            resultado *= numero
        print(f"O resultado da multiplicação é: {resultado}\n")
        deseja_continuar = input("Deseja continuar? (s/n): ").lower()
        if deseja_continuar in ["s", "sim"]:
                print("Continuando...")
        elif deseja_continuar in ["n", "não"]:
                print("Saindo da calculadora. Até logo!\n")
                exit()
        while deseja_continuar not in ["s", "n", "sim", "não"]:
            print("Opção inválida. Por favor.")
            deseja_continuar = input("Deseja continuar? (s/n): ").lower()
    elif opcao == "4":
        resultado = float(input("Digite o 1º número: "))
        for i in range(2, quantidade_numeros + 1):
            numero = float(input(f"Digite o {i}º número: "))
            if numero == 0:
                print("Divisão por zero não é permitida.")
                return
            resultado /= numero
        print(f"O resultado da divisão é: {resultado}\n")
        deseja_continuar = input("Deseja continuar? (s/n): ").lower()
        if deseja_continuar in ["s", "sim"]:
                print("Continuando...")
        elif deseja_continuar in ["n", "não"]:
                print("Saindo da calculadora. Até logo!\n")
                exit()
        while deseja_continuar not in ["s", "n", "sim", "não"]:
            print("Opção inválida. Por favor.")
            deseja_continuar = input("Deseja continuar? (s/n): ").lower()
    elif opcao == "5":
        print("Saindo da calculadora. Até logo!\n")
        
bemvindo()
while True:
    opcao, quantidade_numeros = menu()
    if opcao == "5":
        print("Saindo da calculadora. Até logo!")
        break
    operações(opcao, quantidade_numeros)