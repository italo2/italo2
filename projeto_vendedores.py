"""
Sistema de comissão de uma loja !

by italo a.

aprendizado de python if e else .
"""

valor_base_produto =float(input('Digite o valor do produto base :  '))

desconto_avista=valor_base_produto * -0.10 + valor_base_produto

input(f'valor com o desconto : {desconto_avista}')

valor_parcelado_sjuros=(input(f'valor da parcela em 3 vezes sem juros : {valor_base_produto / 3}'))

venda_vista=int(input( ' A venda realizada foi a vista sim (1) ou não (2) : '))



if venda_vista == 1:
    input(f'sua escolha foi de venda realizada à vista : {venda_vista}')
    valo_comissao=0

    valor_comissao=input(f'sua comissao será de : {desconto_avista * 0.05 }')
else:



 exit(input(f'sua comissão sobre a venda à vista é : {valor_base_produto * 0.05 }'))