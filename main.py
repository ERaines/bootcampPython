

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

# cor_cliente = input('Digite a cor desejada: ')
# cores = ['amarelo', 'verde', 'azul', 'vermelho', 'laranja']

# if cor_cliente.lower() in cores:
#     print('Em estoque')

# else:
#     print('Não temos esta cor em estoque')


def mostrar_menu() -> None:
    print("\n==== Lista de Compras ====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")


def ler_escolha() -> str:
    return input("Escolha: ").strip()


def normalizar_nome(nome: str) -> str:
    """Remove espaços extras e padroniza para comparação."""
    return " ".join(nome.strip().split())


def encontrar_indice(itens: list[dict], nome: str) -> int | None:
    """Retorna o índice do item pelo nome (case-insensitive) ou None se não existir."""
    chave = normalizar_nome(nome).casefold()
    for i, item in enumerate(itens):
        if normalizar_nome(item["nome"]).casefold() == chave:
            return i
    return None


def ler_quantidade(prompt: str = "Digite a quantidade: ") -> int:
    while True:
        valor = input(prompt).strip()
        if not valor.isdigit():
            print("Por favor, digite um número inteiro positivo.")
            continue
        qtd = int(valor)
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
            continue
        return qtd


def adicionar_item(itens: list[dict]) -> None:
    nome = input("Digite o nome do item: ").strip()
    nome = normalizar_nome(nome)
    if not nome:
        print("Nome não pode ser vazio.")
        return

    quantidade = ler_quantidade()

    idx = encontrar_indice(itens, nome)
    if idx is None:
        itens.append({"nome": nome, "quantidade": quantidade})
        print("Item adicionado com sucesso!")
    else:
        itens[idx]["quantidade"] += quantidade
        print("Item já existia. Quantidade atualizada!")


def remover_item(itens: list[dict]) -> None:
    if not itens:
        print("A lista está vazia.")
        return

    nome = input("Digite o nome do item a remover: ").strip()
    idx = encontrar_indice(itens, nome)
    if idx is None:
        print("Item não encontrado.")
    else:
        removido = itens.pop(idx)
        print(f'Removido: {removido["nome"]} - {removido["quantidade"]}')


def listar_itens(itens: list[dict]) -> None:
    if not itens:
        print("Nenhum item na lista.")
        return

    print("\n-- Itens --")
    for i, item in enumerate(sorted(itens, key=lambda x: x["nome"].casefold()), start=1):
        unidade = "unidade" if item["quantidade"] == 1 else "unidades"
        print(f'{i}. {item["nome"]} - {item["quantidade"]} {unidade}')


def main() -> None:
    itens: list[dict] = []

    while True:
        mostrar_menu()
        escolha = ler_escolha()

        if escolha == "4":
            print("Até logo!")
            break
        elif escolha == "1":
            adicionar_item(itens)
        elif escolha == "2":
            remover_item(itens)
        elif escolha == "3":
            listar_itens(itens)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
