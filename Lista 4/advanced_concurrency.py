#### Lista 4 - Nome: João Vitor Ramos Chaves
import threading
import numpy as np
from typing import Dict

## 5. Processamento Paralelo de Dados de Múltiplas Ações
def calcular_medias_moveis(
    acoes: Dict[str, np.ndarray],
    janela: int
) -> Dict[str, np.ndarray]:
    """
    Usa múltiplas threads para calcular a média móvel de várias ações concorrentemente.

    Args:
        acoes (Dict[str, np.ndarray]): Dicionário com nomes de ações e arrays de preços.
        janela (int): Tamanho da janela para a média móvel.

    Returns:
        Dict[str, np.ndarray]: Dicionário com as médias móveis calculadas para cada ação.
    """
    # Worker para cálculo da média móvel de cada ação
    def media_movel_worker(
        acao: str,
        precos: np.ndarray,
        janela: int,
        resultados: Dict[str, np.ndarray],
        lock: threading.Lock
    ):
        """Função que calcula a média móvel para uma única ação."""
        
        print(f"Thread para '{acao}' iniciada...")
        # Usando a técnica de convolução para o cálculo da média móvel, que é eficiente.
        soma_movel = np.convolve(precos, np.ones(janela), 'valid')
        media_movel = soma_movel / janela
        
        # O lock só é adquirido para a operação rápida de escrita no dicionário
        with lock:
            resultados[acao] = media_movel

        print(f"Thread para '{acao}' concluída.")

    # Inicializando as variáveis
    resultados: Dict[str, np.ndarray] = {}
    lock = threading.Lock()
    
    # Itera sobre cada ação e inicializa uma thread para processá-la
    threads = []
    for acao, precos in acoes.items():
        thread = threading.Thread(
            target=media_movel_worker,
            args=(acao, precos, janela, resultados, lock)
        )
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    return resultados
## 5. Teste para Processamento Paralelo de Dados de Múltiplas Ações
def test_calcular_medias_moveis():
    dados_acoes = {
        "PETR4": np.random.rand(105) * 4,
        "ITUB4": np.random.rand(110) * 8.7,
        "SANB11": np.random.rand(115) * 52,
    }
    janela = 15

    print("Iniciando cálculo de médias móveis em paralelo...")
    resultado_paralelo = calcular_medias_moveis(dados_acoes, janela)
    print("\nCálculo paralelo concluído.")

    for acao, sma in resultado_paralelo.items():
        print(f"Resultado para {acao}: array de médias móveis com shape {sma.shape}")

## 6. Simulação de Cálculo de Volatilidade Concorrente
def calcular_volatilidade(
    retornos: np.ndarray,
    janela: int,
    num_threads: int
) -> np.ndarray:
    """
    Calcula a volatilidade móvel de uma série de retornos usando múltiplas threads.

    Args:
        retornos (np.ndarray): Array de retornos diários.
        janela (int): Tamanho da janela para o cálculo da volatilidade.
        num_threads (int): Número de threads a serem usadas.

    Returns:
        np.ndarray: Um array com as volatilidades calculadas para cada janela.
    """
    # Worker de cálculo da volatilidade
    def volatilidade_worker(
        retornos: np.ndarray,
        janela: int,
        output_array: np.ndarray,
        indices_a_calcular: np.ndarray
    ):
        """Função que calcula a volatilidade para uma fatia de índices."""
        # Itera apenas sobre os índices que esta thread é responsável
        for i in indices_a_calcular:
            # Seleciona a janela de dados do array de retornos original
            janela_de_dados = retornos[i : i + janela]
            # Calcula a volatilidade e armazena no array de saída
            output_array[i] = np.std(janela_de_dados)

    # Inicializando variáveis
    num_resultados = len(retornos) - janela + 1 # Numero do tamanho que será o resultado para a janela indicada
    if num_resultados < 1: # Condição para verificar se a array de retornos é válida para a janela indicada
        return np.array([])
    
    # Cria o array de saída compartilhado
    output_volatilidade = np.full(num_resultados, np.nan)
    
    # Divide os ÍNDICES do trabalho em 'num_threads' partes
    indices_de_trabalho = np.arange(num_resultados) # Ex.: [0, 1, 2]
    grupo_de_indices = np.array_split(indices_de_trabalho, num_threads)
    
    # Cria e inicia uma thread para cada grupo de índices
    threads = []
    for grupo in grupo_de_indices:
        thread = threading.Thread(
            target=volatilidade_worker,
            args=(retornos, janela, output_volatilidade, grupo)
        )
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    return output_volatilidade
## 6. Teste de Simulação de Cálculo de Volatilidade Concorrente
def test_calcular_volatilidade():
    retornos_grandes = np.random.randn(1_000_000) * 0.05
    janela = 31 # 1 mes
    num_threads = 4

    print(f"\nIniciando cálculo de volatilidade com {num_threads} threads...")
    vol_paralela = calcular_volatilidade(retornos_grandes, janela, num_threads)
    print(f"Shape do resultado: {vol_paralela.shape}")

if __name__ == '__main__':
    # test_calcular_medias_moveis()
    test_calcular_volatilidade()