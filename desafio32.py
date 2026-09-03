from datetime import date
ano = int(input('Digite seu ano (Coloque 0 para analisar o ano atual): '))
if ano ==0:
    ano = date.today().year
print('O ano {} eh bissexto!'.format(ano) if ano%4==0 and ano%100!=0 or ano%400==0 else 'O ano {} nao e bissexto!'.format(ano))