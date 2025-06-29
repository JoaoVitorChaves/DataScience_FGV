#### Lista 3 - Nome: João Vitor Ramos Chaves
import numpy as np

### Parte 1 - Simulação de Preços e Análise de Retornos
## 1. Simulação de Série de Preços com Ruído Gaussiano
def simular_precos(SO: float, sigma: float, days: int) -> np.ndarray:
    # É necessário retornar um array de tamanho 'days + 1', com o primeiro elemento sendo S0
    prices = np.zeros(days + 1)
    prices[0] = SO
    
    for t in range(days):
        ruido = np.random.normal(loc=0, scale=sigma)
        prices[t + 1] = prices[t] + ruido # Adicionando o ruido gaussiano ao preço anterior
        
    return prices
## 1. Teste Simulação de Série de Preços com Ruído Gaussiano
def test_simular_precos():
    # Comentário: Parâmetros para a simulação.
    preco_inicial = 245.2
    volatilidade = 1.63
    dias_simulados = 2
    precos_simulados = simular_precos(preco_inicial, volatilidade, dias_simulados)

    print(f"Simulação de preços por {dias_simulados} dias:")
    print(precos_simulados)

## 2.1 Cálculo de Retornos Simples
def calc_retornos_simples(prices: np.ndarray) -> np.ndarray:
    # prices[1:] -> P_t (preços de hoje em diante)
    # prices[:-1] -> P_t-1 (preços de ontem para trás)
    # Para resolução de retornos simples, usamos a fórmula: r_t = (P_t - P_t-1) / P_t-1 de forma vetorizada
    return (prices[1:] - prices[:-1]) / prices[:-1]
## 2.2 Cálculo de Retornos Logarítmicos
def calc_retornos_log(prices: np.ndarray) -> np.ndarray:
    # Partindo da mesma nomenclatura anterior, temos a seguinte implementação:
    # prices[1:] -> P_t (preços de hoje em diante)
    # prices[:-1] -> P_t-1 (preços de ontem para trás)
    # np.log aplica o logaritmo natural a cada elemento do resultado da divisão
    return np.log(prices[1:] / prices[:-1])
## 2. Teste Cálculo de Retornos
def test_calc_retornos():
    precos_teste = np.array([100.0, 102.0, 101.0, 103.0])
    retornos_s = calc_retornos_simples(precos_teste)
    retornos_l = calc_retornos_log(precos_teste)

    print(f"Preços: {precos_teste}")
    print(f"Retornos Simples: {retornos_s}")
    print(f"Retornos Logarítmicos: {retornos_l}")

## 3. Indicadores Moveis e Volatilidade
## 3.1 Média Móvel Simples (SMA)
def sma(returns: np.ndarray, window: int) -> np.ndarray:
    medias = []
    for i in range(len(returns) - window + 1):
        janela = returns[i : i + window] # Pega a fatia/janela
        media_da_janela = np.mean(janela) # Calcula a média
        medias.append(media_da_janela)
    return np.array(medias)
## 3.2 Desvio Padrão Móvel (Rolling Standard Deviation)
def rolling_std(returns: np.ndarray, window: int, days_size: int = 0) -> np.ndarray:
    # Como é o denominador de uma raiz, precisamos garantir que seja positivo e diferente de zero
    denominator = window - days_size
    if denominator <= 0:
        raise ValueError("O denominador (window - days_size) deve ser positivo.")

    # Itera-se pela série para calcular o desvio padrão de cada janela
    stds = []
    for i in range(len(returns) - window + 1):
        janela_atual = returns[i : i + window]        
        # Calcula a variância usando a fórmula do numpy (com denominador N)
        variance_np = np.var(janela_atual, ddof=0)
        # Ajusta a variância para o denominador desejado (window - days_size) - nesse caso, como 
        # Var do Numpy é 1/N somatorio de (x_i - media)^2, precisamos ajustar para com window multiplicando
        variance_ajustada = variance_np * (window / denominator)
        # O desvio padrão é a raiz quadrada da variância ajustada
        std_ajustado = np.sqrt(variance_ajustada)
        stds.append(std_ajustado)
        
    return np.array(stds)
## 3. Teste Indicadores Móveis e Volatilidade
def test_indicadores_moveis():
    retornos_teste = np.array([0.02, -0.04, 0.13, -0.22, 0.095, 0.055])
    janela = 4
    media_movel = sma(retornos_teste, janela)
    volatilidade_movel = rolling_std(retornos_teste, janela, days_size=1) # Exemplo com ddof=1

    print(f"Retornos: {retornos_teste}")
    print(f"Média Móvel (janela={janela}): {media_movel}")
    print(f"Volatilidade Móvel (janela={janela}): {volatilidade_movel}")

if __name__ == '__main__':
    # test_simular_precos()
    # test_calc_retornos()
    test_indicadores_moveis()