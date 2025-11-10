from tabulate import tabulate

def registrar_viagem(listaViagens):
    print("\n--- Registrar nova viagem ---")
    motorista = input("Nome do motorista: ")
    destino = input("Destino: ")
    distancia = input("Distância percorrida (km): ")
    gasto = input("Valor gasto com combustível (R$): ")

    if distancia.isnumeric() and gasto.isnumeric():
        distancia = float(distancia)
        gasto = float(gasto)

        if distancia > 0:
            consumo = gasto / distancia
            viagem = {
                "motorista": motorista,
                "destino": destino,
                "distancia": distancia,
                "gasto": gasto,
                "consumo": round(consumo, 2)
            }
            listaViagens.append(viagem)
            print(" Viagem registrada com sucesso!")
        else:
            print(" A distância deve ser maior que zero.")
    else:
        print(" Digite apenas números válidos para distância e gasto.")


def exibir_viagens(listaViagens):
    print("\n--- Lista de Viagens ---")
    if len(listaViagens) == 0:
        print("Nenhuma viagem registrada.")
    else:
        tabela = []
        for v in listaViagens:
            tabela.append([v["motorista"], v["destino"], v["distancia"], v["gasto"], v["consumo"]])
        print(tabulate(tabela, headers=["Motorista", "Destino", "Distância (km)", "Gasto (R$)", "Consumo (R$/km)"], tablefmt="grid"))


def buscar_motorista(listaViagens):
    print(" Buscar viagens por motorista ")
    nome = input("Nome do motorista: ")
    encontrou = False

    for v in listaViagens:
        if v["motorista"].lower() == nome.lower():
            print(f"Motorista: {v['motorista']}")
            print(f"Destino: {v['destino']}")
            print(f"Distância: {v['distancia']} km")
            print(f"Gasto: R$ {v['gasto']}")
            print(f"Consumo: R$ {v['consumo']} por km\n")
            encontrou = True

    if not encontrou:
        print("Nenhuma viagem encontrada para esse motorista.")


def viagem_mais_cara(listaViagens):
    print(" Viagem mais cara ")
    if len(listaViagens) == 0:
        print("Nenhuma viagem registrada.")
    else:
        mais_cara = listaViagens[0]
        for v in listaViagens:
            if v["gasto"] > mais_cara["gasto"]:
                mais_cara = v

        print(f"Motorista: {mais_cara['motorista']}")
        print(f"Destino: {mais_cara['destino']}")
        print(f"Gasto: R$ {mais_cara['gasto']}")


def media_consumo(listaViagens):
    print(" Média geral de consumo ")
    if len(listaViagens) == 0:
        print("Nenhuma viagem registrada.")
    else:
        soma = 0
        for v in listaViagens:
            soma += v["consumo"]
        media = soma / len(listaViagens)
        print(f"Média geral de consumo: R$ {round(media, 2)} por km")
