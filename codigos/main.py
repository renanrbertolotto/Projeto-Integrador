
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

menu = int(input('''\n\t 
            --------------------------------------
            |     DIGITE A OPÇÃO QUE DESEJAR!    |
            --------------------------------------
        1- Cadastrar Produto   2- Ver Produtos Castrados

        3- Alterar Produto     4- Exclusão de Produto
          
                        5- Sair
    '''))
time.sleep(1)
while menu != 5:
    if menu == 1:
        criar_tabela(connection)
        id_produto = int(input('Númrero do produto: '))
        nome_produto = str(input('Nome do produto: '))
        descricao_produto = str(input('Detalhamento: '))
        custo_produto = float(input('Custo do produto: '))
        custo_imposto = float(input('Imposto: '))
        comissão_vendas = float(input('Comissão da venda: '))
        custo_fixo = float(input('Custo fixo: '))
        margem_lucro = float(input("Rentabilidade: %"))
        while comissão_vendas+custo_fixo+custo_imposto+margem_lucro>100: 
            print("Digite um valor válido de rentabilidade")
            margem_lucro = float(input("Rentabilidade: %"))    
        pv = 100*custo_produto/(100 -(custo_fixo+  comissão_vendas + custo_imposto + margem_lucro))
        print(f"pv = {pv}")

        
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO PIProdutos (idProduto, nome, descricao, custoProduto, custofixo, comissao, imposto, margemLucro)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
            """, (id_produto, nome_produto, descricao_produto, custo_produto,custo_fixo, comissão_vendas,custo_imposto ,margem_lucro))
        connection.commit()

        print('\nDados inseridos com sucesso.')      
        
    elif menu == 2:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM piprodutos")
        for row in cursor:
            if row == 0 or None or '':
                id_produto=row[0]
                nome_produto=row[1]
                descricao_produto=row[2]
                custo_produto=row[3]
                custo_imposto=row[4]
                comissão_vendas=row[5]
                custo_fixo=row[6]
                margem_lucro=row[7]
                pv = 100*custo_produto/(100 -(custo_fixo+  comissão_vendas + custo_imposto + margem_lucro))

                totalPorcentagens =custo_produto * ((custo_fixo/100) + (comissão_vendas/100) + (custo_imposto/100))
                totalGastos = totalPorcentagens +custo_produto
                D = pv*custo_fixo/100
                E = pv*comissão_vendas/100
                F = pv*custo_imposto/100
                OC = D+E+F
                C = pv-custo_produto
                H = C-OC
                CP_porcentagem = 100*custo_produto/pv
                custo_porcentagem = 100*C/pv
                CF_porcentagem = custo_fixo*pv/100
                CV_porcentagem = comissão_vendas*pv/100
                IV_porcentagem = custo_imposto*pv/100
                OC_porcentagem = 100*OC/pv 
                margem_reais = margem_lucro*pv/100
        
                if margem_lucro>20:
                        Rentabilidade = 'Margem de lucro alta'
                elif margem_lucro <= 20 and margem_lucro > 10:
                            Rentabilidade = 'Margem de lucro média'
                elif margem_lucro <=10 and margem_lucro > 0:
                            Rentabilidade = 'Margem de lucro baixa'
                elif margem_lucro == 0:
                            Rentabilidade = 'Equilibrio'
                else:
                        Rentabilidade = 'Prejuizo'
                print(f"\t\t{id_produto} {nome_produto}\t\t{descricao_produto} ")
                print("\nDescrição          Valor                       %")
                print(f"Preço de venda:     R${pv:.2f}                    100% ")
                print(f"Preço de compra:    R${custo_produto:.2f}                    {CP_porcentagem:.2f}%")
                print(f"Receita bruta:      R${C:.2f}                    {custo_porcentagem:.2f}%")
                print(f"Custo fixo:         R${CF_porcentagem:.2f}                    {custo_fixo:.2f}%")
                print(f"Comissão de vendas: R${CV_porcentagem:.2f}                     {comissão_vendas:.2f}%")
                print(f"Impostos:           R${IV_porcentagem:.2f}                     {custo_imposto:.2f}% ")
                print(f"Outros custos:      R${OC:.2f}                    {OC_porcentagem:.2f}%")
                print(f"H.Rentabilidade     R${margem_reais:.2f}              {margem_lucro:.2f}%")
                print(f"Lucro: {Rentabilidade}") 
            else:
                print('\n\n\tNão ha produtos cadastrados!')

    elif menu == 3:
        print('\n\t Em processo...')

    elif menu == 4:
        idExcluir = int(input("\n\tDigite o ID do produto q deseja excluir: "))
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM PIProdutos WHERE idProduto = {idExcluir}")
        connection.commit()
        print('\t\tProduto excluido com sucesso!')
    
    elif menu == 5:
        break
        
    else:
        print('\n\t DIGITE UM NUMERO CORRESPONDENTE A UMA AÇÃO DO MENU')    
        
    menu = int(input('''\n\t 
            --------------------------------------
            |     DIGITE A OPÇÃO QUE DESEJAR!    |
            --------------------------------------
        1- Cadastrar Produto   2- Ver Produtos Castrados

        3- Alterar Produto     4- Exclusão de Produto
          
                        5- Sair
    '''))
cursor.close()
connection.close()