menu = '''
******** sistema Bancario - V1 ******** 

(d) depositar
(s) sacar
(e) extrato
(q) sair

==> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:
    opcao =  input(menu).lower()

    if opcao == 'd':
        dep  = float(input ('Informe o valor do deposito: '))
        if dep > 0:
            saldo  += dep
            extrato += f'Deposito: R$ {dep:.2f} \n'
            print(f'Realizado o Deposito no Valor de R$ {dep:.2f}')
            
            #print (saldo)
        else:
            print ('Valor invalido')
    elif opcao == 's':
        if numero_saques < limite_saques:
        
            saque = float(input( 'Digite o Valor de Saque: '))

            if saque > 0:
        
                if saque > limite:
                    print(f'O valor excede o limite de saque, valor permitido por saque R$ {limite:.2f}')
                elif saque > saldo:
                    print('Sem saldo disponivel para o valor doe saque')
                else:
                    saldo -= saque
                    extrato += f'Saque: R$ {saque:.2f} \n'
                    print(f'Realizado o Saque no Valor de R$ {saque:.2f}')
                    numero_saques += 1
                    #print (saldo)
            else:
                print('Tentativa de Saque excede o limite de 3 saques diarios')
    elif opcao == 'e':
        if len(extrato) == 0:
            print("Não foram realizadas movimentações")
        else:
            extrato += f'Saldo: R$ {saldo:.2f} \n'
            print('************* EXTRATO *************')
            print(extrato)


            print('***********************************')
            

    elif opcao == 'q':
        break
    else:
        print('Opcao invalida!!!')
    
    #print (extrato)




