saldo = 1000.0
extrato_produtos = []

print("Olá, bem-vindo ao app Brazexcco")
print(f"Seu saldo disponível é R$ {saldo:.2f}")
print("(1) Extrato (2) Depósito (3) Saque")

escolha = int(input("Selecione qual função você deseja utilizar: "))

while escolha < 1 or escolha > 3:
    print("Esta escolha é inválida. Por favor, digite um número válido.")
    escolha = int(input("Selecione qual função você deseja utilizar: "))

# Interface de Saque
if escolha == 3:
    confirmacao = input("Você escolheu a opção saque, deseja continuar? ").lower()
    
    while confirmacao != "sim":
        print("(1) Extrato (2) Depósito (3) Saque")
        escolha = int(input("Selecione qual função você deseja utilizar: "))
        confirmacao = input("Você escolheu a opção saque, deseja continuar? ").lower()
    
    print(f"O seu saldo disponível: R$ {saldo:.2f}")
    valor = float(input("Quanto deseja retirar: "))
    
    while valor > saldo:
        print("Você não possui este saldo disponível :/.")
        valor = float(input("Por favor, informe quanto você deseja retirar: "))
         
    saldo -= valor
    extrato_produtos.append(f"Saque: R$ {valor:.2f}")
    print(f"Você retirou R$ {valor:.2f} e seu saldo atual é R$ {saldo:.2f}")

# Interface de Depósito
elif escolha == 2: 
    confirmacao = input("Você escolheu a opção depósito, deseja continuar? ").lower()
    
    while confirmacao != "sim":
        print("(1) Extrato (2) Depósito (3) Saque")
        escolha = int(input("Selecione qual função você deseja utilizar: "))
        confirmacao = input("Você escolheu a opção depósito, deseja continuar? ").lower()
    
    print(f"Saldo disponível: R$ {saldo:.2f}")
    valor = float(input("Quanto deseja depositar: "))
    
    while valor <= 0:
        print("Valor inválido. Por favor, informe um valor positivo.")
        valor = float(input("Quanto deseja depositar: "))
    
    saldo += valor
    extrato_produtos.append(f"Depósito: R$ {valor:.2f}")
    print(f"Você depositou R$ {valor:.2f} e seu saldo atual é R$ {saldo:.2f}")

# Interface de Extrato
elif escolha == 1:
    print("Bem-vindo ao seu extrato")
    if extrato_produtos:
        for transacao in extrato_produtos:
            print(transacao)
    else:
        print("Nenhuma transação realizada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
