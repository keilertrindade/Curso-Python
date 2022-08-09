# 04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

import validação_cnpj_funções as funcoes

cnpj = '04.438.816/0001-51'
cnpj_validacao = funcoes.remover_caracteres(cnpj)

print(funcoes.validar(cnpj, cnpj_validacao))

# Commit para recolocar o código antes de dar merda