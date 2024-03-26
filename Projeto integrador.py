#Coisa de projeto
numero_produto = int(input('Númrero do produto: '))
nome_produto = str(input('Nome do produto: '))
descrição_produto = str(input('Detalhamento: '))
custo_produto = float(input('Custo do produto: '))
custo_imposto = float(input('Imposto: '))
comissão_vendas = float(input('Comissão da venda: '))
margem_lucro = float(input('Rentabilidade: '))
custo_fixo = float(input('Custo fixo: '))



print(numero_produto)
print(nome_produto)
print(descrição_produto)
print(custo_produto)
print(custo_imposto)
print(comissão_vendas)
print(margem_lucro)
print(custo_fixo)
l = (custo_fixo + comissão_vendas + custo_imposto + custo_produto )
pv  = l * ((margem_lucro/100)+1)
print(f"{pv}")

if pv> (l*1.2):
    print('Margem de lucro alta')
elif pv <= (l*1.2) and pv > (l*1.1):
    print('Margem de lucro média')
elif pv <= (l*1.1) and pv > (l*1):
    print('Margem de lucro baixa')
elif pv == l:
    print('Equilibrio')
else:
    print('Prejuizo')    