import pandas as pd
import matplotlib.pyplot as plt
from data import formula_e_drivers, events_data, participants_data
import os
import random

# Para exibir todas as linhas do DataFrame
pd.set_option('display.max_rows', None)

def pedir_entrada(prompt, opcoes_validas=None, eh_numerico=False):
    while True:
        entrada_usuario = input(prompt).strip()

        if opcoes_validas:
            if entrada_usuario in opcoes_validas:
                return entrada_usuario
            else:
                print(f"Ops! Escolha uma das opções: {', '.join(opcoes_validas)}")
        else:
            if entrada_usuario:
                if eh_numerico:
                    try:
                        return int(entrada_usuario)
                    except ValueError:
                        print("Não entendi. Tente digitar um número mesmo.")
                else:
                    return entrada_usuario
            else:
                print("Você precisa digitar alguma coisa!")

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criar DataFrames a partir dos dados
def pegar_dataframe_pilotos():
    dados = [{'Piloto': piloto, **info} for piloto, info in formula_e_drivers.items()]
    return pd.DataFrame(dados)

def pegar_dataframe_eventos():
    dados = [{'Evento': evento, **info} for evento, info in events_data.items()]
    return pd.DataFrame(dados)

def pegar_dataframe_participantes():
    return pd.DataFrame(participants_data)

# Menu principal
def menu():
    print('Bem-vindo à Fórmula E!')
    print('1. Listar todos os pilotos.')
    print('2. Filtrar pilotos.')
    print('3. Datas dos próximos eventos.')
    print('4. Tabela de Classificação.')
    print('5. Quiz sobre Fórmula E.')
    print('6. Gráfico de Classificação dos Pilotos.')
    escolha = pedir_entrada('Escolha uma opção: ', opcoes_validas=['1', '2', '3', '4', '5', '6'])
    return escolha

# Mostrar os pilotos
def mostrar_pilotos():
    df = pegar_dataframe_pilotos()
    print(df[['Piloto', 'Nationality', 'Championship_titles']])
    piloto_escolhido = pedir_entrada("Qual piloto você quer saber mais? ")
    if piloto_escolhido in df['Piloto'].values:
        mostrar_info(piloto_escolhido)
    else:
        print("Piloto não encontrado.")

# Mostrar informações detalhadas dos pilotos
def mostrar_info(escolha):
    info = formula_e_drivers[escolha]
    print(f"\nPiloto: {escolha}")
    print(f"Nacionalidade: {info['Nationality']}")
    print(f"Temporadas: {', '.join(info['Seasons'])}")
    print(f"Títulos de campeonato: {info['Championship_titles']}")
    print(f"Entradas: {info['Entries']}")
    print(f"Starts: {info['Starts']}")
    print(f"Poles: {info['Poles']}")
    print(f"Vitórias: {info['Wins']}")
    print(f"Pódiums: {info['Podiums']}")
    print(f"Voltas mais rápidas: {info['Fastest_Laps']}")
    print(f"FanBoosts: {info['FanBoosts']}")
    print(f"Pontos: {info['Points']}")

def filtrar_pilotos():
    df = pegar_dataframe_pilotos()

    # Remover espaços em branco e garantir que a coluna Points é numérica
    df['Points'] = df['Points'].astype(str).str.strip()  # Remove espaços em branco
    df['Points'] = pd.to_numeric(df['Points'], errors='coerce')  # Converte para numérico

    # Filtrar os pilotos com base no filtro escolhido
    print("Filtros que você pode usar:")
    print("1. Nacionalidade")
    print("2. Títulos de campeonato")
    print("3. Entradas")
    print("4. Starts")
    print("5. Poles")
    print("6. Vitórias")
    print("7. Pódios")
    print("8. Voltas mais rápidas")
    print("9. FanBoosts")
    print("10. Pontos")

    escolha_filtro = pedir_entrada("Qual filtro você quer usar? (1-10): ", opcoes_validas=[str(i) for i in range(1, 11)])

    if escolha_filtro == '1':  # Nacionalidade
        nacionalidade = pedir_entrada("Digite a nacionalidade: ")
        df_filtrado = df[df['Nationality'].str.contains(nacionalidade, case=False, na=False)]
    elif escolha_filtro == '2':  # Títulos de campeonato
        df_filtrado = df[df['Championship_titles'] >= 0]  # Filtra todos com títulos
    elif escolha_filtro == '3':  # Entradas
        df_filtrado = df.nlargest(10, 'Entries')  # Top 10 por Entradas
    elif escolha_filtro == '4':  # Starts
        df_filtrado = df.nlargest(10, 'Starts')  # Top 10 por Starts
    elif escolha_filtro == '5':  # Poles
        df_filtrado = df.nlargest(10, 'Poles')
    elif escolha_filtro == '6':  # Vitórias
        df_filtrado = df.nlargest(10, 'Wins')
    elif escolha_filtro == '7':  # Pódios
        df_filtrado = df.nlargest(10, 'Podiums')
    elif escolha_filtro == '8':  # Voltas mais rápidas
        df_filtrado = df.nlargest(10, 'Fastest_Laps')
    elif escolha_filtro == '9':  # FanBoosts
        df_filtrado = df.nlargest(10, 'FanBoosts')
    elif escolha_filtro == '10':  # Pontos
        df_filtrado = df.nlargest(10, 'Points')
    else:
        print("Filtro inválido.")
        return

    if not df_filtrado.empty:
        # Exibir dados dos pilotos com base no filtro escolhido
        filtro_coluna = ''
        if escolha_filtro == '2':
            filtro_coluna = 'Championship_titles'
            coluna_nome = 'Títulos de campeonato'
        elif escolha_filtro == '3':
            filtro_coluna = 'Entries'
            coluna_nome = 'Entradas'
        elif escolha_filtro == '4':
            filtro_coluna = 'Starts'
            coluna_nome = 'Starts'
        elif escolha_filtro == '5':
            filtro_coluna = 'Poles'
            coluna_nome = 'Poles'
        elif escolha_filtro == '6':
            filtro_coluna = 'Wins'
            coluna_nome = 'Vitórias'
        elif escolha_filtro == '7':
            filtro_coluna = 'Podiums'
            coluna_nome = 'Pódios'
        elif escolha_filtro == '8':
            filtro_coluna = 'Fastest_Laps'
            coluna_nome = 'Voltas mais rápidas'
        elif escolha_filtro == '9':
            filtro_coluna = 'FanBoosts'
            coluna_nome = 'FanBoosts'
        elif escolha_filtro == '10':
            filtro_coluna = 'Points'
            coluna_nome = 'Pontos'

        # Exibe os resultados com o filtro apropriado
        df_filtrado[coluna_nome] = df_filtrado[filtro_coluna]  # Renomeia a coluna para exibir
        print(df_filtrado[['Piloto', 'Nationality', coluna_nome]])

        piloto_escolhido = pedir_entrada("Qual piloto você quer saber mais? ")
        if piloto_escolhido in df_filtrado['Piloto'].values:
            mostrar_info(piloto_escolhido)
        else:
            print("Piloto não encontrado.")
    else:
        print("Nenhum piloto encontrado com esse filtro.")

# Mostrar datas dos próximos eventos
def mostrar_datas():
    df = pegar_dataframe_eventos()
    print(df[['Evento', 'Date', 'Time']])

# Mostrar tabela de classificação
def mostrar_classificacao():
    df = pegar_dataframe_participantes()
    print(df[['Position', 'Name', 'Team', 'Points']])

# Mostrar gráfico da classificação dos pilotos
def plotar_classificacao():
    df = pegar_dataframe_participantes()
    plt.barh(df['Name'], df['Points'], color='blue')
    plt.xlabel('Pontos')
    plt.ylabel('Pilotos')
    plt.title('Pontuação da Temporada')
    plt.show()

# Quiz sobre a Fórmula E
def quiz():
    perguntas = [
        "Quem é o atual campeão da Fórmula E?",
        "Qual cidade teve a primeira corrida da Fórmula E?",
        "Quantas etapas tem uma temporada padrão da Fórmula E?",
        "Qual é o recorde de vitórias numa única temporada da Fórmula E?",
        "Qual equipe tem mais títulos de construtores na Fórmula E?",
        "Quem foi o primeiro campeão da Fórmula E?",
        "Qual equipe venceu o primeiro título de construtores da Fórmula E?",
        "Qual é o circuito mais curto da Fórmula E?",
        "Qual é o nome do carro usado na primeira geração da Fórmula E?",
        "Quantas equipes competem na temporada 2023-24?",
        "Quem é o piloto com mais vitórias na história da Fórmula E?",
        "Em que ano foi realizada a primeira temporada da Fórmula E?",
        "Quantos carros uma equipe podia usar até a temporada 2017-18?",
        "Qual equipe venceu o título de construtores na temporada 2022-23?",
        "Quantas cidades sediaram corridas de Fórmula E até 2024?",
        "Qual a velocidade máxima dos carros da Gen2 da Fórmula E?",
        "Qual piloto tem o maior número de GPs disputados na Fórmula E?",
        "Em qual cidade a primeira corrida da temporada 2019-20 foi realizada?"
    ]

    respostas = [
        "Nyck de Vries",
        "Pequim",
        "Tem 15 etapas por temporada",
        "Jean-Éric Vergne ganhou 4 corridas na temporada 2017–18",
        "DS Techeetah",
        "Nelson Piquet Jr.",
        "Renault e.dams",
        "Mônaco",
        "Spark-Renault SRT 01E",
        "11 equipes",
        "Lucas di Grassi e Sébastien Buemi com 13 vitórias",
        "2014",
        "4 carros por equipe",
        "Envision Racing",
        "33 cidades",
        "220 km/h",
        "Lucas di Grassi",
        "Riade, Arábia Saudita"
    ]

    opcoes = [
        ["Nyck de Vries", "António Félix da Costa", "Jean-Éric Vergne", "Lucas di Grassi"],
        ["Pequim", "Paris", "Nova York", "Londres"],
        ["Tem 10 etapas por temporada", "Tem 12 etapas por temporada", 
         "Tem 15 etapas por temporada", "Tem 20 etapas por temporada"],
        ["Sebastien Buemi ganhou 3 corridas na temporada 2016–17", 
         "Jean-Éric Vergne ganhou 4 corridas na temporada 2017–18", 
         "Lucas di Grassi ganhou 5 corridas na temporada 2018–19", 
         "António Félix da Costa ganhou 6 corridas na temporada 2019–20"],
        ["DS Techeetah", "Audi Sport ABT Schaeffler", 
         "Mercedes-EQ Formula E Team", "Envision Virgin Racing"],
        ["Nelson Piquet Jr.", "Lucas di Grassi", "Sébastien Buemi", "Jean-Éric Vergne"],
        ["Renault e.dams", "Audi Sport ABT Schaeffler", 
         "DS Techeetah", "Mercedes-EQ Formula E Team"],
        ["Mônaco", "Berlim", "Nova York", "Cidade do México"],
        ["Spark-Renault SRT 01E", "Spark SRT05e", 
         "Porsche 99X Electric", "Jaguar I-Type 6"],
        ["10 equipes", "11 equipes", "12 equipes", "13 equipes"],
        ["Lucas di Grassi", "Sébastien Buemi", "Mitch Evans", "Jean-Éric Vergne"],
        ["2013", "2014", "2015", "2016"],
        ["2 carros por equipe", "3 carros por equipe", 
         "4 carros por equipe", "5 carros por equipe"],
        ["DS Techeetah", "Envision Racing", 
         "Mercedes-EQ Formula E Team", "Jaguar TCS Racing"],
        ["30 cidades", "31 cidades", "32 cidades", "33 cidades"],
        ["200 km/h", "210 km/h", "220 km/h", "230 km/h"],
        ["Lucas di Grassi", "Sébastien Buemi", 
         "Stoffel Vandoorne", "Jake Dennis"],
        ["Berlim, Alemanha","Londres, Reino Unido","Riade, Arábia Saudita","Mônaco, Monte Carlo"]
    ]

    # Sortear 5 perguntas aleatórias
    indices_sorteados = random.sample(range(len(perguntas)), 5)
    pontuacao = 0

    for i in indices_sorteados:
        print(f"\nPergunta: {perguntas[i]}")
        for j, opcao in enumerate(opcoes[i]):
            print(f"{j + 1}. {opcao}")

        resposta_usuario = pedir_entrada("Escolha a alternativa certa (1, 2, 3 ou 4): ", opcoes_validas=['1', '2', '3', '4'])

        # Verifica se a resposta está correta
        correta = opcoes[i].index(respostas[i]) + 1

        if resposta_usuario == str(correta):
            print("Acertou! 🎉")
            pontuacao += 1
        else:
            print(f"Errou! A resposta certa era: {respostas[i]}")

    # Exibe a pontuação ao final do quiz
    print(f"\nVocê acertou {pontuacao} de 5 perguntas. Fim do quiz.")

# Loop do programa
while True:
    limpar_tela()
    escolha = menu()

    if escolha == '1':
        mostrar_pilotos()
    elif escolha == '2':
        filtrar_pilotos()
    elif escolha == '3':
        mostrar_datas()
    elif escolha == '4':
        mostrar_classificacao()
    elif escolha == '5':
        quiz()
    elif escolha == '6':
        plotar_classificacao()
    else:
        print("Opção inválida.")
    
    if pedir_entrada("Deseja continuar? (s/n) ", opcoes_validas=['s', 'n']) == 'n':
        break
