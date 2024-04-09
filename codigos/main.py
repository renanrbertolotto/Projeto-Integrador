#importação
import time

#projeto Integrador
print('''\n\t 
========================================================================== 
|    BBBBB   EEEEE   M   M         V   V   IIIII   N   N   DDDD    OOOO   |
|    B    B  E       MM MM         V   V     I     NN  N   D   D  O    O  |
|    BBBBB   EEEE    M M M          V V      I     N N N   D   D  O    O  |
|    B    B  E       M   M          V V      I     N  NN   D   D  O    O  |
|    BBBBB   EEEEE   M   M           V     IIIII   N   N   DDDD    OOOO   |
==========================================================================
      |                 SISTEMA DE CADASTRO DE PRODUTOS            |
      |                     PARA SISTEMAS DE ESTOQUE               |  
      ==============================================================''')
time.sleep(2.5)
init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
time.sleep(1)
while init == 's':
    menu = int(input('''\n\t 
            --------------------------------------
            |     DIGITE A OPÇÃO QUE DESEJAR!    |
            --------------------------------------
        1- Cadastrar Produto   2- Ver Produtos Castrados

        3- Alterar Produto     4- Exclusão de Produto
          
                        5- Sair
    '''))
    if menu == 1:
        numero_produto = int(input('Númrero do produto: '))
        nome_produto = str(input('Nome do produto: '))
        descrição_produto = str(input('Detalhamento: '))
        custo_produto = float(input('Custo do produto: '))
        custo_imposto = float(input('Imposto: '))
        comissão_vendas = float(input('Comissão da venda: '))
        custo_fixo = float(input('Custo fixo: '))
        margem_lucro = float(input('Rentabilidade: '))



        print(numero_produto)
        print(nome_produto)
        print(descrição_produto)
        print(custo_produto)
        print(custo_imposto)
        print(comissão_vendas)
        print(margem_lucro)
        print(custo_fixo)
        totalPorcentagens =custo_produto * ((custo_fixo/100) + (comissão_vendas/100) + (custo_imposto/100))
        totalGastos = totalPorcentagens +custo_produto
        pv  = totalPorcentagens+(custo_produto * ((margem_lucro/100)+1))
        print(f"{pv}")

        if pv > (totalGastos *1.2):
            print('Margem de lucro alta')
        elif pv <= (totalGastos *1.2) and pv > (totalGastos *1.1):
            print('Margem de lucro média')
        elif pv <= (totalGastos *1.1) and pv > (totalGastos *1):
            print('Margem de lucro baixa')
        elif pv == totalGastos:
            print('Equilibrio')
        else:
            print('Prejuizo')        
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
    elif menu == 2:
        print('\n\t Em processo...') 
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
        pass
    elif menu == 3:
        print('\n\t Em processo...')
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
        pass
    elif menu == 4:
        print('\n\t Em processo...')
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] ')) 
        pass
    elif menu == 5:
        init = 'n'
        
    else:
        print('\n\t DIGITE UM NUMERO CORRESPONDENTE A UMA AÇÃO DO MENU')    
        
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
        