menu = '''
        SEJA BEM VINDO AO PY BANK!
    
    Qual operação deseja realizar? Digite:
    [d] Depositar
    [s] Sacar
    [e] Consultar extrato
    [q] Sair
    
    =>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    operacao = input(menu)
    
    if operacao == "d":
        valor_depositado = float(input("Insira o valor que deseja depositar: "))
        
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print(f"Operação concluída! Saldo atual: R${saldo:.2f}\n")
        else:
            print("Valores negativos não são permitidos! Tente novamente.")        
        
    
    elif operacao == "s":
        valor_sacado = float(input("Insira o valor que deseja sacar: "))
        
        excedeu_saldo = valor_sacado > saldo
        
        excedeu_limite = valor_sacado > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print(f" Não foi possível sacar R${valor_sacado:.2f}. Saldo insuficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite permitido.")
            
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor_sacado > 0:
            saldo -= valor_sacado
            numero_saques += 1
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            print(f"Operação concluída! Saldo atual: R${saldo:.2f}\n")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif operacao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    
    elif operacao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        