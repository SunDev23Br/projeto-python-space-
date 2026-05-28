# projeto-python-space-
Global solution FIAP


# SPACE GUARDIAN

## Descrição da Missão

O projeto SPACE GUARDIAN foi desenvolvido para simular um sistema de rastreamento de detritos espaciais em órbita terrestre.

O objetivo da missão é monitorar objetos espaciais, calcular a distância entre os detritos e uma estação orbital de referência, além de classificar automaticamente o nível de risco de colisão.

O sistema analisa os dados recebidos e gera relatórios contendo informações sobre:
- posição espacial dos objetos
- velocidade relativa
- distância calculada
- nível de risco orbital

Caso um objeto apresente risco crítico, o sistema emite um alerta de colisão iminente.

---

## Formato dos Dados Consumidos

Os dados são armazenados utilizando listas e dicionários em Python.

Exemplo:

```python
detritos = [
    {
        "id_detrito": "satelite_desativado",
        "coordenadas_xyz": [1500, 200, 400],
        "velocidade": 5000
    },

    {
        "id_detrito": "lixo_espacial",
        "coordenadas_xyz": [3000, 500, 100],
        "velocidade": 2000
    }
]

Estrutura dos campos
Campo	Descrição
id_detrito :	Nome ou identificação do objeto
coordenadas_xyz	Coordenadas espaciais X, Y e Z
velocidade :	Velocidade relativa do objeto

Como Executar o Projeto :

Requisitos :
Python 3 instalado

Execução :
Salve o código em um arquivo chamado main.py
Abra o terminal na pasta do projeto
Execute o comando:
python main.py

O sistema irá processar os dados dos detritos espaciais e exibir o relatório orbital no terminal.