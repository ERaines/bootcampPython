

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


# nota_aluno = float(input('Qual foi sua nota no exame'))

# if nota_aluno >= 7:
#     print('Você esta aprovado!')
# elif nota_aluno >= 5:
#     print('Você esta de recuperação')
# else:
#     print('Você esta reprovado!')


# def calcular_porcentagem(preco, porcentagem):
#     return preco - (preco * porcentagem / 100)


# valor_final = calcular_porcentagem(1010, 25)
# print(f'O valor Final com desconto é de R${valor_final:.2f}')


# Listas


# cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0               1             2         3

# cidades.append('Santa Catarina')
# cidades.remove('Salvador')
# cidades.insert(1, 'Santa Catarina')
# cidades.pop(0)
# cidades.sort()

# print(cidades)

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho', 'laranja']

if cor_cliente.lower() in cores:
    print('Em estoque')

else:
    print('Não temos esta cor em estoque')
