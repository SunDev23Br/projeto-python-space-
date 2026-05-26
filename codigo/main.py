import math

print("\n<<<<<<<<< SPACE GUARDIAN >>>>>>>>>>>\n")
print("Bem-vindo ao Space Guardian, o sistema de proteção espacial!")


def ativar_sistema():

    detritos = [
        {"id_detrito":"satelite_desativado",
        "coordenadas_xyz":[1500,200,400],
        "velocidade": 5000,},

        {"id_detrito":"lixo_espacial",
        "coordenadas_xyz":[3000,500,100],
        "velocidade": 2000,},

        {"id_detrito":"foguete_descartado",
        "coordenadas_xyz":[1000,300,200],
        "velocidade": 500,}

        ,{"id_detrito":"apolo_11",
        "coordenadas_xyz":[1000,100,-450],
        "velocidade": 10,},

        {"id_detrito":"lixo_espacial",
        "coordenadas_xyz":[1459,350,-5],
        "velocidade": 100,},

        {"id_detrito":"foguete_descartado",
        "coordenadas_xyz":[500,0,100],
        "velocidade": 50,}


    ]

    return detritos

def calcular_distancia(coordenadas):
    x = coordenadas[0]
    y = coordenadas[1]
    z = coordenadas[2]
    distancia = math.sqrt (x**2 + y**2 + z**2) ** 0.5

    return distancia

def classificar_risco(distancia, velocidade):

    if distancia < 50:

        if velocidade > 1000:
            return "CRÍTICO"

        else:
            return "ALTO"

    elif distancia < 200:
        return "MÉDIO"

    elif distancia < 500:
        return "BAIXO"

    else:
        return "SEGURO"

def analisar_detritos(detritos):
    resultados = []
    for objeto in detritos:
        distancia = calcular_distancia(
            objeto["coordenadas_xyz"]
        )
        risco = classificar_risco(distancia, objeto["velocidade"])
        resultado = {
            "id_detrito": objeto.get("id_detrito"),
            "coordenadas_xyz": objeto.get("coordenadas_xyz"),
            "distancia": round(distancia, 2),
            "velocidade": objeto.get("velocidade"),
            "risco": risco
        }

        resultados.append(resultado)

    return resultados

def exibir_relatorio(resultados):

    print("\n<<< RELATÓRIO DE DETECÇÃO ORBITAL >>>\n")

    for detrito in resultados:
        print(f"Detrito: {detrito['id_detrito']}")
        print(f"Coordenadas: {detrito['coordenadas_xyz']}")
        print(f"Distância: {detrito['distancia']} unidades")
        print(f"Velocidade: {detrito['velocidade']}")
        print(f"Risco: {detrito['risco']}")
        print("-" * 40)

        if detrito['risco'] == "CRÍTICO":
            print("Alerta: Detrito de alta velocidade detectado! Risco de colisão iminente.")


def main():

    detritos = ativar_sistema()

    resultados = analisar_detritos(detritos)

    exibir_relatorio(resultados)

main()