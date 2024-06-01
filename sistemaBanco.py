#interface basica 

saldo = 1000

print("olá bem-vindo ao app Brazexcco")
print(f"Seu saldo disponivel é R$ {saldo:.2f} ")
print(" (1) Extrato (2) Deposito (3) Saque ")

escolha = int(input("selecione qual função você deseja utilizar: "))

while escolha < 1 or escolha > 3:
    
    print("Esta escolhar é invalida. Por favor digite um numero valido")
    
    escolha = int(input("selecione qual função você deseja utilizar: "))

# Interface de Saque

if escolha ==  3:
    confirmacao = input("Você escolheu a opção saque, deseja continuar? ")
    
    #loop caso o cliente tenha errado a escolha
    
    while confirmacao == "não":
        print(" (1) Extrato (2) Deposito (3) Saque ")
        
        escolha = int(input("selecione qual função você deseja utilizar: "))
        confirmacao = input("Você escolheu a opção saque, deseja continuar? ")
    
    print(f"O seu saldo disponivel: R$ {saldo:.2f}")
    valor = int(input("Quanto deseja retirar: "))
    
    #loop caso o saque seja invalido
    
    while valor > saldo:
        print("você não possui este saldo disponivel :/.")
        valor = int(input("por favor informe quanto você deseja retirar: "))
         
    novo_saldo = saldo - valor
    
    print(f"Você retirou R$ {valor:.2f} e seu saldo atual é R$ {novo_saldo:.2f}")
    saldo = novo_saldo
    
if escolha == 2: 
    confirmacao = input("Você escolheu a opção deposito, deseja continuar? ")
    
    while confirmacao == "não":
        print(" (1) Extrato (2) Deposito (3) Saque ")
        
        escolha = int(input("selecione qual função você deseja utilizar: "))
        confirmacao = input("Você escolheu a opção deposito, deseja continuar? ")
    
    print(f"Saldo disponivel: R${saldo:.2f}")
    valor = float(input("quanto deseja depositar: "))
    
    #o codigo não ira aceitar valores negativos e o proprio zero
    while valor <= 0:
        
        print("Valor invalido. Por favor informe um valor positivo.")
        valor = float(input("quanto deseja depositar: "))
    
    novo_saldo = saldo + valor
    print(f"Você depositou R$ {valor:.2f} e seu saldo atual é R$ {novo_saldo:.2f}")
    
    saldo = novo_saldo
    
# escolha para voltar a interface inicial


    
        