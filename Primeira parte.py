#Projeto Integrador
nome_produto = str(input('\n\t Nome do produto: '))
codigo_produto = int(input('\n\t Código do produto: '))
descriçao_produto = str(input('\n\t Descrição do produto: '))
custo_produto = float(input('\n\t Custo do produto: '))
custo_fixo = float(input('\n\t Custo administrativo: '))
comissao = float(input('\n\t Comissão de vendas: '))
imposto = float(input('\n\t Imposto impregado no produto: '))
margem_lucro = float(input('\n\t Margem do lucro do produto: '))
#Formula da rentabilidade
pv = custo_produto/(1-((custo_fixo/100)+(comissao/100)+(imposto/100)+(margem_lucro/100)/1))
outros_custos = (pv*custo_fixo/100 + pv*comissao/100 + pv*imposto/100)
renda_bruta = (pv - custo_produto)
rentabilidade = (renda_bruta - outros_custos)
#Regra de 3 para calcular porcentagem dos custos
CP = custo_produto*100/pv
RB = renda_bruta*100/pv
CF = pv*custo_fixo/100
CV = pv*comissao/100
IM = pv*imposto/100
OC = outros_custos*100/pv
RE = rentabilidade*100/pv
#Montagem da tela para mostrar os preços 
print(f'\n\t Preço de venda R${pv} Porcentagem de venda 100%')
print(f'\n\t Custo de aquisição R${custo_produto} Porcentagem de custo {CP}%')
print(f'\n\t Renda Bruta R${renda_bruta} Porcentagem {RB}%')
print(f'\n\t Custo Fixo R${CF} Porcentagem {custo_fixo}%')
print(f'\n\t Comissão R${CV} Porcentagem {comissao}%')
print(f'\n\t Imposto R${IM} Porcentagem {imposto}%')
print(f'\n\t Outros custos R${outros_custos} Porcentagem {OC}%')
print(f'\n\t Rentabilidade R${rentabilidade} Porcentagem {RE}%')
#Classificação de lucro dos Produtos 
if (RE > 20):
    print('\n\t Renda alta')
elif (RE > 10 and RE <= 20):
    print('\n\t Renda média')
elif (RE > 0 and RE < 10):
    print('\n\t Renda Baixa')
elif (RE == 0):
    print('\n\t Equilibrio')
else:
    print('\n\t Prejuizo')