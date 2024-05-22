def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    saldo_disponivel = saldo + limite
    excedeu_saldo = valor > saldo_disponivel
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print(f"Operação falhou! Você não tem saldo suficiente. Saldo disponível (incluindo limite): R$ {saldo_disponivel:.2f}.")
    elif excedeu_saques:
        print(f"Operação falhou! Número máximo de {LIMITE_SAQUES} saques excedido.")
    elif valor > 0:
        if valor > saldo:
            limite_usado = valor - saldo
            saldo = 0
            limite -= limite_usado
        else:
            saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques, limite

def exibir_extrato(saldo, extrato, limite):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Limite disponível: R$ {limite:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques, limite = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato, limite)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()