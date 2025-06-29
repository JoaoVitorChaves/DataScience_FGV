#### Lista 2 - Nome: João Vitor Ramos Chaves

### Parte 1 - Biblioteca math
## 1. Valor Futuro (Juros Compostos)
def future_value(pv, r, n, t):
    import math

    # A fórmula é FV = PV * (1 + r/n)^(n*t)
    # 'pv' é o valor presente
    # 'r' é a taxa de juros anual
    # 'n' é o número de vezes que o juro é capitalizado por ano
    # 't' é o número de anos

    # Usamos a função pow da biblioteca math para calcular a potência
    base = 1 + (r / n)
    exponent = n * t
    fv = pv * math.pow(base, exponent)

    return fv
## 1. Teste Valor Futuro
def test_future_value():
    valor_presente = 1000.0  # R$ 1000,00
    taxa_anual = 0.05        # 5% ao ano
    periodos_por_ano = 12    # Capitalização mensal
    tempo_em_anos = 10.0     # 10 anos

    valor_futuro = future_value(valor_presente, taxa_anual, periodos_por_ano, tempo_em_anos)

    print(f"Investindo R${valor_presente:.2f} a {taxa_anual*100}% ao ano, com capitalização mensal,")
    print(f"após {tempo_em_anos} anos, o valor futuro será de R${valor_futuro:.2f}.")

## 2. Desvio Padrão de Retornos
def standard_deviation(returns):
    import math

    # N é o número de retornos na lista
    n_count = len(returns)
    # 'x_barra' é a média dos retornos
    mean = sum(returns) / n_count

    # Calculamos a somatória dos quadrados das diferenças em relação à média
    sum_of_squared_diffs = sum(math.pow(xi - mean, 2) for xi in returns)
    # A variância é a soma dos quadrados das diferenças dividida por N
    variance = sum_of_squared_diffs / n_count
    # O desvio padrão é a raiz quadrada da variância
    sigma = math.sqrt(variance)

    return sigma
## 2. Teste Desvio Padrão
def test_standard_deviation():
    returns = [0.02, 0.01, -0.015, 0.0234, 0.025, -0.02]
    sigma = standard_deviation(returns)
    print(f"O desvio padrão dos retornos é: {sigma:.4f}")

## 3. Tempo para Dobrar (Capitalização Contínua)
def time_to_double(r):
    import math
    # Fórmula base t = ln(2) / ln(1 + r). 
    # 'ln', que é o logaritmo natural, em Python é a função math.log()

    # Indo direto na função, temos a seguinte implementação:
    log_de_2 = math.log(2)
    log_de_1_mais_r = math.log(1 + r)
    t = log_de_2 / log_de_1_mais_r

    return t
## 3. Teste Tempo para Dobrar
def test_time_to_double():
    taxa_juros = 0.15  # 15% ao ano
    tempo = time_to_double(taxa_juros)
    print(f"Com uma taxa de juros de {taxa_juros*100}%, o tempo para dobrar o investimento é de {tempo:.2f} anos.")

### Parte 2 - Biblioteca itertools
## 1. Combinações de Ativos
def portfolio_combinations(assets, k):
    import itertools
    # A função itertools.combinations(iterável, r) retorna um iterador
    # que produz tuplas de comprimento r com elementos do iterável, ou seja, a questao em si é uma simples demonstração
    # dessa função da biblioteca
    return list(itertools.combinations(assets, k))
## 1. Teste Combinações de Ativos
def test_portfolio_combinations():
    ativos = ['PETR4', 'PETR3', 'ITUB', 'SANT11']
    k = 2  # Número de ativos na combinação
    combinacoes = portfolio_combinations(ativos, k)

    print(f"Combinações de {k} ativos a partir da lista {ativos}:")
    for c in combinacoes:
        print(c)

## 2. Média Móvel
def moving_average(prices, window):
    import itertools
    # Criamos 'window' iteradores independentes a partir da lista de preços com a funcao
    # tee() 
    iterators = itertools.tee(prices, window)
    
    # O primeiro iterador começa na posição 0, o segundo na 1, e assim por diante
    for i, it in enumerate(iterators):
        # O _ é usado pois não precisamos do valor retornado por next()
        for _ in range(i):
            next(it, None) # Avança o iterador 'it' em uma posição.
            
    # zip(*iterators) agrupa os elementos dos iteradores
    # Ex: para window=3, ele cria tuplas (prices[0], prices[1], prices[2]), (prices[1], prices[2], prices[3])
    sliding_windows = zip(*iterators)
    
    # Usamos uma list comprehension para calcular a média de cada janela
    averages = [sum(w) / window for w in sliding_windows]
    
    return averages
## 2. Teste Média Móvel
def test_moving_average():
    precos = [100, 103, 101, 102, 107, 130]
    janela = 2
    medias_moveis = moving_average(precos, janela)

    print(f"Médias móveis com janela de {janela} dias para os preços {precos}:")
    print(medias_moveis)

### Parte 3 - Biblioteca random
## 1. Simulação de Preço de Ação
def simulate_stock_price(initial_price, mu, sigma, days):
    import random
    # Inicializamos a lista de preços com o valor inicial
    prices = [initial_price]
    # O preço atual começa como o preço inicial
    current_price = initial_price
    
    # Por meio do for loop em 'days', podemos simular a trajetória. Como dado no enunciado do exercício, geramos a variação diário 
    # usando uma distribuição normal (mu é a média da variação, sigma é a volatilidade)
    for _ in range(days):
        daily_change = random.gauss(mu, sigma)
        # O novo preço é o preço anterior mais a variação
        current_price += daily_change
        # Comentário: Adicionamos o novo preço à nossa lista de trajetória.
        prices.append(current_price)
        
    return prices
    
## 1. Teste Simulação de Preço de Ação
def test_simulate_stock_price():
    preco_inicial = 233.0
    tendencia_diaria = 0
    volatilidade_diaria = 1
    dias_simulados = 10

    trajetoria_preco = simulate_stock_price(preco_inicial, tendencia_diaria, volatilidade_diaria, dias_simulados)

    print(f"Preço Inicial: R${preco_inicial:.2f}")
    print(f"Simulação por {dias_simulados} dias:")
    formatted_prices = [f"R${p:.2f}" for p in trajetoria_preco]
    print(formatted_prices)

### Parte 4 - Bibliotecas urllib e os
## 1. Download e Concatenação de Dados do BLS QCEW
def download_and_merge(years_quarters, output_file):
    import os
    import urllib.request

    # Como especificado no enunciado, cria-se o diretório 'data/' se ele não existir
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Diretório '{data_dir}' criado.")

    # Download dos arquivos
    base_url = "https://data.bls.gov/cew/data/api/{year}/{quarter}/industry/10.csv"
    downloaded_files = []
    
    for year, quarter in years_quarters:
        # Monta a URL específica para o ano e trimestre. 
        url = base_url.format(year=year, quarter=quarter)
        
        # Comentário: Define o caminho local para salvar o arquivo. 
        local_filename = os.path.join(data_dir, f"{year}-q{quarter}.csv")
        
        try:
            print(f"Baixando dados de {year} Q{quarter} de {url}...")
            # Comentário: Usa urlretrieve para baixar o arquivo. [cite: 19]
            urllib.request.urlretrieve(url, local_filename)
            print(f"Salvo em {local_filename}")
            downloaded_files.append(local_filename)
        except Exception as e:
            print(f"Falha ao baixar {url}. Erro: {e}")

    # Se nenhum arquivo foi baixado, não há nada a concatenar
    if not downloaded_files:
        print("Nenhum arquivo foi baixado. Verifique os anos e trimestres fornecidos.")
        return

    # Garantindo que os arquivos baixados estejam ordenados por ano e trimestre
    downloaded_files.sort()
    header_written = False
    
    # Abre o arquivo de saída em modo de escrita ('w')
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Itera sobre cada arquivo baixado para ler seu conteúdo
        for filename in downloaded_files:
            with open(filename, 'r', encoding='utf-8') as infile:
                header = infile.readline()
                # Cabeçalho sendo escrito apenas uma vez do primeiro arquivo 
                if not header_written:
                    outfile.write(header)
                    header_written = True
                # Restante dos dados sendo escritos no arquivo
                for line in infile:
                    outfile.write(line)
                    
    print(f"\nDados foram concatenados com sucesso em '{output_file}'")
## 1. Teste Download e Concatenação de Dados
def test_download_and_merge():
    teste_de_anos = [(2022, 1), (2024, 2)] 
    arquivo_saida = 'bls_qcew_merged_data.csv'
    download_and_merge(teste_de_anos, arquivo_saida)

if __name__ == '__main__':
    # Part 1
    # test_future_value()
    # test_standard_deviation()
    # test_time_to_double()
    # Parte 2
    # test_portfolio_combinations()
    # test_moving_average()
    # test_simulate_stock_price()
    # Parte 3
    test_download_and_merge()