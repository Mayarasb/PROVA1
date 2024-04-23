populacaoA = 80000
taxa_popA = 3/100

populacaoB = 200000
taxa_popB = 1.5/100

qnt_anos = 1

while populacaoA <= populacaoB:
    crescimentoA = populacaoA * taxa_popA
    crescimentoB = populacaoB * taxa_popB
    populacaoA = populacaoA + crescimentoA
    populacaoB = populacaoB + crescimentoB
    qnt_anos = qnt_anos + 1


print(f"Será necessário {qnt_anos} anos para que a  população A ultrapasse ou iguale a população B")