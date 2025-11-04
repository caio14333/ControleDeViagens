from tabulate import tabulate

def registrar_viagens(listaViagens):
    nome_moto = input("digite o nome do motorista").strip()
    destino = input("qual é o seu destino?").strip()
    distancia = float(input("qual foi a distancia pecorrida"))
    valor_gasto = float(input("qual foi o valor gasto de combustivel?"))
    consumo = valor_gasto / distancia
    viagem = {
        "nome do motorista" : nome_moto,
        "destino" : destino,
        "distancia" : distancia,
        "consumo" : consumo
    }
    listaViagens.append(viagem)
    print(f"A viagem para o destino {destino} foi adicionada com sucesso")

 
def exibirViagens(listaViagens):
    tabela = [[livro["motorista"], livro["destino"], livro["distancia"], livro["consumo"]] for livro in listaViagens]
    print(" Lista de Livros:")
    print(tabulate(tabela, headers=["nome do motorista", "destino", "distancia", "consumo"], tablefmt="grid"))
    print()

def buscarMotorista(listaViagens):
    buscar = input("digite o motorista que voce deseja procurar")
    while True:
        for nome_moto in listaViagens:
            if ["nome do motorista"].lower() == buscar.lower:
                if nome_moto["distancia"] == "distancia":
                    if nome_moto["distancia"] : "distancia"
                    print(f"motorista encontrado com sucesso")
                    
  

    
