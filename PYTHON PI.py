codigo_produto = int(input("Código do produto: "))
nome_produto = str(input("Nome do produto: "))
desc_produto = str(input("Descrição do produto: "))
CP = float(input("Custo do produto:R$"))
CV = float(input("Comissão de vendas: %"))
CF = float(input("Custo fixo: %"))
IV = float(input("Impostos: %"))
ML = float(input("Rentabilidade: %"))
pv = 100*CP/(100 - (CF + CV + IV + ML))
print("-------------------------------------")  
print(f"\tPreço de venda: R${pv:.2f}")
print("--------------------------------------")
D = pv*CF/100
E = pv*CV/100
F = pv*IV/100
OC = D+E+F
C = pv-CP
H = C-OC
CP_porcentagem = 100*CP/pv
custo_porcentagem = 100*C/pv
CF_porcentagem = CF*pv/100
CV_porcentagem = CV*pv/100
IV_porcentagem = IV*pv/100
OC_porcentagem = 100*OC/pv
ML_porcentagem = ML*pv/100
print("\nDescrição          Valor                       %")
print(f"Preço de venda:     R${pv:.2f}                    100% ")
print(f"Preço de compra:    R${CP:.2f}                    {CP_porcentagem:.2f}%")
print(f"Receita bruta:      R${C:.2f}                    {custo_porcentagem:.2f}%")
print(f"Custo fixo:         R${CF_porcentagem:.2f}                    {CF:.2f}%")
print(f"Comissão de vendas: R${CV_porcentagem:.2f}                     {CV:.2f}%")
print(f"Impostos:           R${IV_porcentagem:.2f}                     {IV:.2f}% ")
print(f"Outros custos:      R${OC:.2f}                    {OC_porcentagem:.2f}%")
print(f"Rentabilidade:      R${ML_porcentagem:.2f}                    {ML:.2f}%")
if ML>20:
    print("\nLucro alto")
elif ML<=20 and ML>10:
    print("\nLucro médio")
elif ML<=10 and ML>0: 
    print("\nLucro baixo")
elif ML==0:
    print("\nEquilíbrio")
else:
    print("\nPrejuízo")