# README - Projeto Fórmula E em Python

## Descrição
Este projeto é uma aplicação de console interativa que apresenta dados sobre a Fórmula E, como informações detalhadas dos pilotos, eventos futuros, tabela de classificação e um quiz interativo. O projeto utiliza bibliotecas como `pandas` e `matplotlib` para manipulação e visualização de dados. O programa permite ao usuário explorar informações sobre a Fórmula E por meio de um menu principal que oferece diferentes funcionalidades.

## Funcionalidades
1. **Listar Pilotos**: Exibe uma lista de todos os pilotos da Fórmula E, permitindo que o usuário selecione um piloto para ver mais detalhes.
2. **Filtrar Pilotos**: Oferece filtros para classificar os pilotos com base em várias métricas, como nacionalidade, vitórias e pontos.
3. **Datas dos Próximos Eventos**: Mostra as datas e horários dos próximos eventos da Fórmula E.
4. **Tabela de Classificação**: Exibe a classificação dos participantes da temporada atual.
5. **Quiz**: Um quiz interativo com perguntas aleatórias sobre a Fórmula E.
6. **Gráfico de Classificação**: Mostra um gráfico horizontal da pontuação dos pilotos da temporada atual.

## Requisitos
- Python 3.6 ou superior
- Bibliotecas:
  - `pandas`
  - `matplotlib`
  - `os`
  - `random`

### Instalação de Dependências
Execute o comando abaixo para instalar as dependências:
```bash
pip install pandas matplotlib
```

## Estrutura de Dados
Os dados utilizados no projeto estão armazenados nos arquivos do módulo `data.py`:
- **formula_e_drivers**: Um dicionário contendo informações sobre os pilotos.
- **events_data**: Um dicionário com informações dos eventos futuros.
- **participants_data**: Dados da tabela de classificação da temporada.

## Execução
Para executar o projeto, basta rodar o script principal:
```bash
python main.py
```

O programa apresenta um menu interativo que permite escolher entre as várias funcionalidades disponíveis. Após cada ação, o usuário tem a opção de continuar navegando ou encerrar o programa.

## Funcionalidades Detalhadas
### 1. Listar Todos os Pilotos
Exibe uma lista com o nome, nacionalidade e títulos de campeonato dos pilotos. O usuário pode selecionar um piloto para ver mais detalhes, como número de vitórias, poles, pódios, etc.

### 2. Filtrar Pilotos
Permite aplicar diferentes filtros para ordenar os pilotos, como nacionalidade, número de vitórias, poles, pontos, e outros. Após aplicar o filtro, o usuário pode escolher um piloto para visualizar mais informações.

### 3. Datas dos Próximos Eventos
Exibe uma tabela com os eventos futuros, incluindo o nome do evento, data e hora.

### 4. Tabela de Classificação
Mostra a classificação dos pilotos na temporada atual, incluindo posição, nome, equipe e pontos acumulados.

### 5. Quiz
Um quiz interativo sobre a Fórmula E, onde o usuário responde perguntas de múltipla escolha. Ao final, é exibida a pontuação.

### 6. Gráfico de Classificação
Exibe um gráfico horizontal (`barh`) com a pontuação dos pilotos da temporada atual, gerado com a biblioteca `matplotlib`.
