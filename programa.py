from funcoes import registrar_viagem, exibir_viagens, buscar_motorista, viagem_mais_cara, media_consumo

listaViagens = []

while True:
    print(" CONTROLE DE VIAGENS ")
    print("1 - Registrar nova viagem")
    print("2 - Exibir todas as viagens")
    print("3 - Buscar viagens por motorista")
    print("4 - Exibir viagem mais cara")
    print("5 - Mostrar média geral de consumo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_viagem(listaViagens)
    elif opcao == "2":
        exibir_viagens(listaViagens)
    elif opcao == "3":
        buscar_motorista(listaViagens)
    elif opcao == "4":
        viagem_mais_cara(listaViagens)
    elif opcao == "5":
        media_consumo(listaViagens)
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print(" Opção inválida. Tente novamente.")
