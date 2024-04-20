# Criando um sistema bancário com as operações: sacar, depositar e visualizar
import textwrap
from datetime import datetime
import os
def menu():
    menu = """\n
    ------------------- MENU ------------------------
    1 -\tDepositar
    2 -\tSacar
    3 -\tExtrato
    4 -\tNova conta
    5 -\tListar contar
    6 -\tNovo usuário
    7 -\tSair

    ==> """
    return input(textwrap.dedent(menu))

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato, /):
    os.system('cls')
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito efetuado. Volte sempre! ====")

    else:
        print("\n=== Falha na operação! O valor digitado é inválido. ===")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    os.system('cls')
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n=== Falha na operação! Seu saldo é insuficiente. ===")
            
    elif excedeu_limite:
            print("\n=== Falha na operação! O valor do saque excede o limite. ===")

    elif excedeu_saques:
            print("\n Falha na Operação! Número máximo de saques excedido. @@@")
            
    elif valor > 0:
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\t{data_hora}\n"
        numero_saques += 1
        print("=== Saque efetuado. Volte sempre! ===")

    else:
        print("\n=== Operação falhou! O valor é inválido. ===")

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
        os.system('cls')
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("=================================================")

def criar_usuario(usuarios):
    os.system('cls')
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Operação falhou! Já existe usuário com esse CPF! ===")
        return
    
    nome = input("Informe seu nome completo: ")
    data_de_nascomento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascomento, "cpf": cpf, "endereco": endereco })

    print("=== Usuário criado com sucesso ===")

def filtrar_usuario(cpf, usuarios):
    os.system('cls')
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    os.system('cls')
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== conta criado com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    os.system('cls')
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
        
        if opcao == '1':
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        
        elif opcao == '2':
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limites_saques = LIMITE_SAQUES
            )
            
        elif opcao == '3':
            mostrar_extrato(saldo, extrato = extrato)
            
        elif opcao == '6':
            criar_usuario(usuarios)
        
        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if contas:
                consta.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '7':
            break
    
    else:
        print("Operação inválida, por favor selecione a opração correta.")

main()

print('Obridado por usar nosso sistema, volte sempre!')