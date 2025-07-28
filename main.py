

# F - String
# name = input('Qual é o seu nome?')
# idade = input('Qual é sua idade?')
# fruta_favorita = input('Qual é sua fruta favorita')

# print(f'Olá {name}, vote tem {idade} e sua fruta favorita é {fruta_favorita}')


# produto_porcoes = int(input('Quantas porçoes o produto tem?'))
# uso_diario = int(input('Quantas porçoes vc usar por dia?'))

# dias = produto_porcoes / uso_diario
# print(f') produtudo vai durar {dias:.0f} dias')
# print(f') produtudo vai durar {int(dias)} dias')


nota_aluno = float(input('Qual foi sua nota no exame'))

if nota_aluno >= 7:
    print('Você esta aprovado!')
elif nota_aluno >= 5:
    print('Você esta de recuperação')
else:
    print('Você esta reprovado!')
