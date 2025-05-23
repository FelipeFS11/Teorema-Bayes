"""
Em uma escola, sabe-se que:
45% dos alunos estudam regularmente para as provas.
Entre os que estudam, 90% tiram nota acima de 7. 
Entre os que não estudam, apenas 20% tiram nota acima de 7.
Pergunta:
Um aluno tirou nota acima de 7. Qual é a probabilidade de ele ter estudado? E de não ter estudado?
"""

# probabilidades
aluno_estudou = 0.45 # estudam regularmente
aluno_nao_estudou = 1 - aluno_estudou # não estudam regularmente

p_nota_alta_estudou = 0.9 # tiraram nota alta dado que estudou
p_nota_alta_nao_estudou = 0.2 # tiraram nota alta, mas não estudou

# Teorema de Bayes
# probabilidade de ter estudado
p_estudou_dado_nota_alta = (p_nota_alta_estudou * aluno_estudou) / (
    p_nota_alta_estudou * aluno_estudou + p_nota_alta_nao_estudou * aluno_nao_estudou)

# probabilidade de não ter estudado
p_nao_estudou_dado_nota_alta = (p_nota_alta_nao_estudou * aluno_nao_estudou) / (
    p_nota_alta_nao_estudou * aluno_nao_estudou + p_nota_alta_estudou * aluno_estudou)

# resultado
print(f"Probabilidade de o aluno ter estudado dado que tirou nota acima de 7: {p_estudou_dado_nota_alta:.2%}")
print(f"Probabilidade de o aluno não ter estudado dado que tirou nota acima de 7: {p_nao_estudou_dado_nota_alta:.2%}")