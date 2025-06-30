#### Lista 4 - Nome: João Vitor Ramos Chaves
import threading
import time
import random
from typing import Dict, List, Tuple

## 3. Gerenciamento de Risco Concorrente
def gerenciar_risco(
    total_risco: float,
    estrategias: List[Tuple[str, float]],
    tempo_total: int
) -> Dict[str, float]:
    """
    Simula o gerenciamento de risco concorrente.

    Args:
        total_risco (float): Limite total de risco disponível.
        estrategias (List[Tuple[str, float]]): Lista com nome e risco de cada estratégia.
        tempo_total (int): Tempo total de simulação em segundos.

    Returns:
        Dict[str, float]: Dicionário com o risco alocado por cada estratégia.
    """
    # Worker que aloca risco para cada estratégia
    def strategy_worker(
        nome_estrategia: str,
        risco_a_alocar: float,
        limite_total: float,
        risco_alocado_total: List[float],
        risco_por_estrategia: Dict[str, float],
        lock: threading.Lock,
        stop_event: threading.Event
    ):
        """Função para cada thread de estratégia de risco."""
        while not stop_event.is_set():
            with lock:
                # Verifica se há espaço para alocar o risco
                if risco_alocado_total[0] + risco_a_alocar <= limite_total:
                    # Aloca o risco
                    risco_alocado_total[0] += risco_a_alocar
                    risco_por_estrategia[nome_estrategia] = risco_a_alocar
                    print(f"Estratégia '{nome_estrategia}' alocou {risco_a_alocar:.2f} de risco. "
                        f"Total agora: {risco_alocado_total[0]:.2f}")
                    return  # Encerra a thread após alocar com sucesso

            # Comentário: Se não conseguiu alocar, espera um pouco antes de tentar de novo.
            time.sleep(random.uniform(0.1, 0.5))

        print(f"Estratégia '{nome_estrategia}' não conseguiu alocar risco.")

    # Inicializando variáveis
    # Obs.: Usamos uma lista com um item para que o float seja mutável entre as threads
    risco_alocado_total = [0.0]
    risco_por_estrategia: Dict[str, float] = {}
    lock = threading.Lock()
    stop_event = threading.Event()

    # Cria as threads para cada estratégia
    threads = []
    for nome, risco in estrategias:
        thread = threading.Thread(
            target=strategy_worker,
            args=(nome, risco, total_risco, risco_alocado_total, risco_por_estrategia, lock, stop_event)
        )
        threads.append(thread)
        thread.start()

    time.sleep(tempo_total)
    stop_event.set()

    for thread in threads:
        thread.join()

    return risco_por_estrategia
## 3. Teste Gerenciamento de Risco Concorrente
def test_gerenciar_risco():
    limite = 170.0
    estrategias = [
        ("ZerarUSDBRL", 100.0),
        ("ZerarEURUSD", 50.0),
        ("ZerarGBPUSD", 20.0),
        ("ZerarUSDZAR", 40.0)
    ]
    duracao_simulacao = 10 # segundos

    print(f"Iniciando gerenciamento de risco com limite de {limite:.2f}...")
    alocacao_final = gerenciar_risco(limite, estrategias, duracao_simulacao)
    print("\nAlocação Final de Risco:", alocacao_final)
    print(f"Risco Total Alocado: {sum(alocacao_final.values()):.2f}")

## 4. Monitoramento Concorrente de Ações
def monitorar_acoes(acoes: List[str], valor_alvo: float) -> List[str]:
    """
    Simula o monitoramento concorrente de ações para verificar se atingem um valor alvo.

    Args:
        acoes (List[str]): Lista de nomes de ações a serem monitoradas.
        valor_alvo (float): Valor a ser monitorado.

    Returns:
        List[str]: Lista com os nomes das ações que atingiram o valor alvo.
    """
    # Monitor worker
    def _monitor_worker(
        acao: str,
        valor_alvo: float,
        acoes_atingidas: List[str],
        lock: threading.Lock
    ):
        """Função alvo que monitora uma única ação."""
        # Simula a obtenção de um preço inicial
        preco_anterior = round(random.uniform(1000.0, 1005.0), 2)
        # Simula a latência da rede antes de obter o novo preço
        time.sleep(random.uniform(0.1, 2.0))
        # Simula a obtenção de um preço atual
        preco_atual = round(random.uniform(1000.0, 1005.0), 2)
        
        print(f"Ação [{acao}] -> Preços: Anterior={preco_anterior:.2f}, Atual={preco_atual:.2f}")
        
        # Comentário: Verifica se o valor alvo está entre o preço anterior e o atual.
        limite_inferior = min(preco_anterior, preco_atual)
        limite_superior = max(preco_anterior, preco_atual)
        
        if limite_inferior <= valor_alvo <= limite_superior:
            with lock:
                acoes_atingidas.append(acao)
                print(f"ALVO ATINGIDO! Ação '{acao}' adicionada à lista.")

    # Inicializando as variáveis
    acoes_que_atingiram_alvo: List[str] = []
    lock = threading.Lock()

    # Criando as threads
    threads = []
    for acao in acoes:
        thread = threading.Thread(
            target=_monitor_worker,
            args=(acao, valor_alvo, acoes_que_atingiram_alvo, lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return acoes_que_atingiram_alvo
## 4. Teste de Monitoramento Concorrente de Ações
def test_monitorar_acoes():
    acoes = ["PETR4", "VALE3", "ITUB4", "BBDC4", "WEGE3"]
    valor_alvo = 1002.0

    print(f"\nIniciando monitoramento de ações para o valor alvo de ${valor_alvo:.2f}...")
    resultado_monitoramento = monitorar_acoes(acoes, valor_alvo)
    print("Ações que atingiram o alvo:", resultado_monitoramento)

if __name__ == '__main__':
    # test_gerenciar_risco()
    test_monitorar_acoes()
