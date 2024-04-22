#importação
import time
import oracledb
from conexao import conectar_banco
from conexao import criar_tabela

#conecta com banco de dados
connection = conectar_banco()

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
init = str(input('\n\t DESEJA FAZER ALGUMA AÇÃO: s[SIM]/n[NÃO] '))
time.sleep(1)
while init == 's' or "sim":
    menu = int(input('''\n\t 
            --------------------------------------
            |     DIGITE A OPÇÃO QUE DESEJAR!    |
            --------------------------------------
        1- Cadastrar Produto   2- Ver Produtos Castrados

        3- Alterar Produto     4- Exclusão de Produto
          
                        5- Sair
    '''))
    if menu == 1:
        criar_tabela(connection)
        id_produto = int(input('Númrero do produto: '))
        nome_produto = str(input('Nome do produto: '))
        descricao_produto = str(input('Detalhamento: '))
        custo_produto = float(input('Custo do produto: '))
        custo_imposto = float(input('Imposto: '))
        comissão_vendas = float(input('Comissão da venda: '))
        custo_fixo = float(input('Custo fixo: '))
        margem_lucro = float(input('Rentabilidade: '))
        if margem_lucro <= 100:
            


            totalPorcentagens =custo_produto * ((custo_fixo/100) + (comissão_vendas/100) + (custo_imposto/100))
            totalGastos = totalPorcentagens +custo_produto
            pv  = totalPorcentagens+(custo_produto * ((margem_lucro/100)+1))
            print(f"{pv}")

            if pv > (totalGastos *1.2):
                Rentabilidade = 'Margem de lucro alta'
                print(Rentabilidade)
            elif pv <= (totalGastos *1.2) and pv > (totalGastos *1.1):
                Rentabilidade = 'Margem de lucro média'
                print(Rentabilidade)
            elif pv <= (totalGastos *1.1) and pv > (totalGastos *1):
                Rentabilidade = 'Margem de lucro baixa'
                print(Rentabilidade)
            elif pv == totalGastos:
                Rentabilidade = 'Equilibrio'
                print(Rentabilidade)
            else:
                Rentabilidade = 'Prejuizo'
                print(Rentabilidade)

            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO PIProdutos (idProduto, nome, descricao, custoProduto, custofixo, comissao, imposto, margemLucro, rentabilidade, precoVenda)
                    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
                """, (id_produto, nome_produto, descricao_produto, custo_produto,custo_imposto,comissão_vendas, custo_fixo,margem_lucro, Rentabilidade, pv))
                connection.commit()
                cursor.close()
                print('Dados inseridos com sucesso.')
            except oracledb.DatabaseError as erro:
                    print('Erro:', erro)
        else: 
            print('A margem de lucro não pode ser maior q 100%\n')        
        init = str(input('\n\t DESEJA FAZER ALGUMA AÇÃO: s[SIM]/n[NÃO] '))
        
    elif menu == 2:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM piprodutos")
            for row in cursor:
                print(f'''
            ID  | Nome  | Descrição | Custo Produto  | Custo Imposto   | Comissão Vendas | Custo Fixo | Margem deLucro  |   Rentabilidade      | Preço de Venda
            =============================================================================================================================================
            {row[0]:<4} | {row[1]:<8} | {row[2]:<10} | {row[3]:<13.2f} | {row[4]:<13.2f} | {row[5]:<16.2f} | {row[6]:<11.2f} | {row[7]:<14.2f} | {row[8]} | {row[9]}
            =============================================================================================================================================
            ''')
                if row =='':
                     print('Não ha produtos cadastrados!')
        except oracledb.DatabaseError as erro:
                print('Erro:', erro)

        init = str(input('\n\t DESEJA FAZER ALGUMA AÇÃO: s[SIM]/n[NÃO] '))

    elif menu == 3:
        print('\n\t Em processo...')
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))

    elif menu == 4:
        idExcluir = int(input("\n\tDigite o ID do produto q deseja excluir: "))
        try:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM PIProdutos WHERE idProduto = {idExcluir}")
            print('\t\tProduto excluido com sucesso!')
        except oracledb.DatabaseError as erro:
                print('Erro:', erro)

        init = str(input('\n\t DESEJA FAZER ALGUMA AÇÃO: s[SIM]/n[NÃO] ')) 
    
    elif menu == 5:
        init = 'n'
        break
        
    else:
        print('\n\t DIGITE UM NUMERO CORRESPONDENTE A UMA AÇÃO DO MENU')    
        
        init = str(input('\n\t DESEJA FAZER ALGUMA ALTERAÇÃO: s[SIM]/n[NÃO] '))
        