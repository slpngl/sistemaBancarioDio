i = True
isaque = 0
saldo = 0
transacoes = []
idtransacao = 0


while i == True :

    print("Qual opção deseja escolher?")
    print("E - Extrato")
    print("D - Depósito")
    print("S - Saque")
    print("X - Sair")

    
    entrada = input() 
    
    if entrada == "E" or entrada == "e" :
        print("EXTRATO")
        print("Saldo atual : R$ %.2f"  %saldo)
        print(transacoes)
        for idtransacao, transacoes in enumerate(transacoes):
            print(f"Índice: {idtransacao}, Transação: {transacoes}")
        

    elif entrada == "D" or entrada == "d" : 

        print("DEPÓSITO")
        print("Quanto deseja depositar?")
        deposito = float(input())
        saldo = saldo + deposito
        print("Saldo atual :: R$ %.2f"  %saldo) 
        idtransacao == transacoes.count 
        idtransacao = (idtransacao + 1 ) 
        transacoes.append('Depósito realizado com sucesso .')
        

    elif entrada == "S" or entrada == "s" : 

        print("SAQUE")
        print("Saldo atual : R$ %.2f"  %saldo)
        print("Quanto deseja sacar?")
        saque = float(input())
        print("Saque : R$ %.2f"  %saque)
        if saque<0 or saque>500:
            print("Saque inválido, valor inexistente ou excedente")
        elif saldo<saque:
            print("Saldo insuficiente")
        else:
           if isaque > 2:
               print("Operação não realizadas. Quantidade de saques no dia excedido!")
           else:   
                saldo = (saldo-saque)
                isaque = isaque + 1
                print("saque realizado")
                print("Saldo atual :: R$ %.2f"  %saldo)
                print("saques realizados no dia : %i" %isaque)
                idtransacao == transacoes.count 
                idtransacao = (idtransacao + 1)
                print("id  : %i" %idtransacao)
                transacoes.append('Saque realizado com sucesso .')

                # transacoes.append("Id : %i  Saque número : %i Valor : %.2f " %idtransacao )
                                 
    elif entrada == "X" : 
        i = False

    else :
        print("OPÇÃO INVALIDA")

        

    