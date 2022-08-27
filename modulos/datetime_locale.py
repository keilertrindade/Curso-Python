from datetime import datetime,  date
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange #'monthrange = pega o numero do dia na semana, e ultimo dia do mês'



setlocale(LC_ALL, 'pt_BR.utf-8') #String vazia muda para o local padrão do computador

dt = date.today
print(dt)
formatacao = dt.strftime('%A, %d de %B de %Y')
# print(formatacao)

# ULTIMO DIA DE CADA MÊS

mes_atual = int(dt.strftime('%m'))
# print(mes_atual, mdays[mes_atual])

# Último dia do mês em ano bissexto
print(monthrange(2022, 2))
dia_semana, ultimo_dia = monthrange(2020, 2)
dia_semana_2, ultimo_dia_2 = monthrange(2024, 2)
