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
        {"id_detrito":"satelite_desativado",
        "coordenadas_xyz":[1000,300,200],
        "velocidade": 3000,}


    ]

    return detritos

def exibir_relatorio(resultados):

    print("\n<<<<<<<<<< RELATÓRIO DE DETECÇÃO ORBITAL >>>>>>>>>>>\n")

    for detrito in resultados:
        print(f"Detrito: {detrito['id_detrito']}")
        print(f"Coordenadas: {detrito['coordenadas_xyz']}")
        print(f"Velocidade: {detrito['velocidade']}")
        print("-" * 40)

        #if item['risco'] =="CRÍTICO":

           # print("Alerta: Detrito de alta velocidade detectado! Risco de colisão iminente.")


def main():

    detritos = ativar_sistema()

    #resultados = analisar_detritos(detritos)

    #exibir_relatorio(resultados)

main()