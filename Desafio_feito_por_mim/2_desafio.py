import textwrap

def menu():
    menu = """
    ****MENU****
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Nova Conta
    5 - Listar Contas
    6 - Novo Usuário
    7 - Sair

    ** Escolha a opção para iniciar a operação **
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$: {valor:.2f}\n"
            print(f"Deposito realizado com sucesso. Valor do saldo atualizado R$: {saldo:.2f}")
    else:
        print("O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Erro de operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Erro de operação! Saque maior que o limite atual.")

        elif excedeu_saques:
            print("Erro de operação! Número de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saldo atual após saque R$: {saldo:.2f}")

        else:
            print("O valor informado é inválido.")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n###########EXTRATO###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu Saldo atual: R$ {saldo:.2f}")
        print("--------------------------------")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ### Já existe usuário com esse CPF! ###")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor a depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor a sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado pela operação!! Volte Sempre!!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()