#=============Cabeçalho==================
#==Professor: Rodrigo Medeiros Vilela ==
#==Aluno: Gabriel Carneiro Barros ==
#==Componente: Python Básico ==
#==Dados: 26/06/2026 ==
#===========================


#===========================
# Sistemas De Computação De Games
# Autor: Gabarito do Professor
# Conteúdos:
# - print /input
# - variáveis
# - listas e dicionários
# - if / elif / else
# - for / while / break
# - funções
# - parâmetros e return
# - import random
#===========================

import random

#==================
# ESTRUTURAS DE DADOS
#==================

catalogo = {}
vendas = []
clientes = []
ranking = {}

#===================
# FUNÇÕES DO CATÁLOGO
#===================

def cadastrar_jogo():
    titulo = input("Título do jogo: ")
    plataforma = input("Plataforma (PC/PS5/Xbox): ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    catalogo[titulo] = {
        "plataforma": plataforma,
        "preco": preco,
        "estoque": estoque
    }

    print("Jogo cadastrado com sucesso!")


def listar_catalogo():
    if len(catalogo) == 0:
        print("Nenhum jogo cadastrado.")
    else:
        print("\nCATÁLOGO DE JOGOS")
        print("-" * 35)

        for titulo, dados in catalogo.items():
            print("Jogo:", titulo)
            print("Plataforma:", dados["plataforma"])
            print("Preço: R$", dados["preco"])
            print("Estoque:", dados["estoque"])
            print("-" * 35)


def consultar_jogo():
    titulo = input("Título do jogo: ")

    if titulo in catalogo:
        dados = catalogo[titulo]
        print("\nJogo:", titulo)
        print("Plataforma:", dados["plataforma"])
        print("Estoque:", dados["estoque"])
    else:
        print("Jogo não encontrado.")


def atualizar_estoque():
    titulo = input("Título do jogo: ")

    if titulo in catalogo:
        nova_qtd = int(input("Nova quantidade em estoque: "))
        catalogo[titulo]["estoque"] = nova_qtd
        print("Estoque atualizado!")
    else:
        print("Jogo não encontrado.")


# ============================
# FUNÇÕES DE CLIENTES
#============================

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    nivel = input("Nível gamer (Iniciante/Intermediário/Pro): ")

    cliente = {
        "nome": nome,
        "nivel": nivel
    }

    clientes.append(cliente)
    print("Cliente cadastrado!")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLISTA DE CLIENTES")
        print("-" * 30)

        for cliente in clientes:
            print("Nome:", cliente["nome"])
            print("Nível:", cliente["nivel"])
            print("-" * 30)


def sortear_cliente():
    if len(clientes) == 0:
        print("Cadastre clientes primeiro.")
    else:
        sorteado = random.choice(clientes)
        print("Cliente sorteado:", sorteado["nome"])
        print("Nível:", sorteado["nivel"])


#========================
# FUNÇÕES DE VENDAS
#========================

def registrar_venda():
    cliente = input("Nome do cliente: ")
    titulo = input("Título do jogo: ")

    if titulo not in catalogo:
        print("Jogo não encontrado no catálogo.")
        return

    if catalogo[titulo]["estoque"] == 0:
        print("Jogo fora de estoque.")
        return

    preco = catalogo[titulo]["preco"]
    catalogo[titulo]["estoque"] -= 1

    venda = {
        "cliente": cliente,
        "jogo": titulo,
        "valor": preco
    }

    vendas.append(venda)

    if titulo in ranking:
        ranking[titulo] += 1
    else:
        ranking[titulo] = 1

    print("Venda registrada!")
    print("Jogo:", titulo)
    print("Valor: R$", preco)


def aplicar_cupom():
    if len(vendas) == 0:
        print("Nenhuma venda registrada.")
        return

    ultima = vendas[-1]
    cupom = random.choice([10, 15, 20, 25])

    desconto = ultima["valor"] * (cupom / 100)
    total = ultima["valor"] - desconto

    print("\nCLIENTE:", ultima["cliente"])
    print("Jogo:", ultima["jogo"])
    print("Valor original: R$", ultima["valor"])
    print("Cupom sorteado:", cupom, "%")
    print("Valor final: R$", round(total, 2))


def relatorio_vendas():
    if len(vendas) == 0:
        print("Nenhuma venda encontrada.")
        return

    total = 0

    print("\nRELATÓRIO DE VENDAS")
    print("-" * 35)

    for venda in vendas:
        print(venda["cliente"], "->", venda["jogo"], "- R$", venda["valor"])
        total += venda["valor"]

    print("-" * 35)
    print("TOTAL VENDIDO: R$", round(total, 2))


# ==========================
# FUNÇÕES DE RANKING
# ==========================

def ver_ranking():
    if len(ranking) == 0:
        print("Nenhuma venda registrada ainda.")
        return

    print("\nRANKING DE JOGOS MAIS VENDIDOS")
    print("-" * 35)

    for jogo, quantidade in ranking.items():
        print(jogo, "->", quantidade, "venda(s)")


def jogo_destaque():
    if len(ranking) == 0:
        print("Nenhuma venda registrada ainda.")
        return

    mais_vendido = ""
    maior = 0

    for jogo, quantidade in ranking.items():
        if quantidade > maior:
            maior = quantidade
            mais_vendido = jogo

    print("\nJOGO DESTAQUE DO MÊS")
    print("Título:", mais_vendido)
    print("Vendas:", maior, "unidade(s)")


def sorteio_brinde():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    brindes = ["Controle", "Headset", "Gift card R$ 50", "Camiseta Gamer"]

    ganhador = random.choice(clientes)
    brinde = random.choice(brindes)

    print("\nSORTEIO DE BRINDES")
    print("Ganhador:", ganhador["nome"])
    print("Brinde:", brinde)


# ==========================
# RELATÓRIO GERAL
# ==========================

def relatorio_geral():
    total_vendido = 0

    for venda in vendas:
        total_vendido += venda["valor"]

    print("\nRELATÓRIO GERAL DA LOJA")
    print("-" * 40)
    print("Jogos no catálogo:", len(catalogo))
    print("Clientes cadastrados:", len(clientes))
    print("Total de vendas:", len(vendas))
    print("Receita total: R$", round(total_vendido, 2))
    print("Títulos no ranking:", len(ranking))


# ==========================
# SUBMENUS
# ==========================

def menu_catalogo():
    while True:
        print("\n=== MENU CATÁLOGO ===")
        print("1 - Cadastrar Jogo")
        print("2 - Listar Catálogo")
        print("3 - Consultar Jogo")
        print("4 - Atualizar Estoque")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_jogo()
        elif op == "2":
            listar_catalogo()
        elif op == "3":
            consultar_jogo()
        elif op == "4":
            atualizar_estoque()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_clientes():
    while True:
        print("\n=== MENU CLIENTES ===")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Sortear Cliente")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            sortear_cliente()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_vendas():
    while True:
        print("\n=== MENU VENDAS ===")
        print("1 - Registrar Venda")
        print("2 - Aplicar Cupom")
        print("3 - Relatório de Vendas")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            registrar_venda()
        elif op == "2":
            aplicar_cupom()
        elif op == "3":
            relatorio_vendas()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_ranking():
    while True:
        print("\n=== MENU RANKING ===")
        print("1 - Ver Ranking")
        print("2 - Jogo Destaque")
        print("3 - Sorteio de Brinde")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            ver_ranking()
        elif op == "2":
            jogo_destaque()
        elif op == "3":
            sorteio_brinde()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


# ==========================
# MENU PRINCIPAL
# ==========================

while True:
    print("\n" + "=" * 50)
    print("    SISTEMA LOJA DE GAMES")
    print("=" * 50)
    print("1 - Catálogo de Jogos")
    print("2 - Gestão de Clientes")
    print("3 - Vendas")
    print("4 - Ranking")
    print("5 - Relatório Geral")
    print("0 - Encerrar")

    opcao = input("Escolha: ")

    if opcao == "1":
        menu_catalogo()
    elif opcao == "2":
        menu_clientes()
    elif opcao == "3":
        menu_vendas()
    elif opcao == "4":
        menu_ranking()
    elif opcao == "5":
        relatorio_geral()
    elif opcao == "0":
        print("Sistema encerrado. Game over!")
        break
    else:
        print("Opção inválida.")
