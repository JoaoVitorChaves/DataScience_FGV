#### Lista 4 - Nome: João Vitor Ramos Chaves
import threading
import random
import uuid
import time
from typing import Dict, List, Any

## 1. Simulação de Traders Colocando Ordens Concorrentemente
def simular_traders(num_traders: int, num_ordens: int) -> Dict[str, List[Dict[str, Any]]]:
    """
    Simula traders colocando ordens concorrentemente.
    
    Args:
        num_traders (int): Número de threads (traders) a serem criadas.
        num_ordens (int): Número de ordens que cada trader deve colocar. 

    Returns:
        Dict[str, List[Dict[str, Any]]]: O estado final do livro de ordens.
    """
    # Função que será executada por cada thread (trader no caso), que no caso insere ordens de
    # compra ou venda em uma estrutura compartilhada (ordem_book), que consiste em dois dicionários
    # (um para compras - chave 'Compra' - e outro para vendas - chave 'Venda' -).
    # Como cada ordem necessita de um identificado unico, estou utilizando a biblioteca uuid para a geração do id.
    def trader_worker(
        num_ordens: int,
        order_book: Dict[str, List[Dict[str, Any]]],
        book_lock: threading.Lock
    ):
        """Função que simula um trader."""
        for _ in range(num_ordens):
            # Ordem aleatória
            price = round(random.uniform(1.0, 1_000_000.0), 2)
            quantity = random.randint(1, 50000)
            order = {'id': str(uuid.uuid4()), 'price': price, 'quantity': quantity}

            # Adquire o lock para acesso exclusivo ao livro de ordens
            with book_lock:
                order_type = random.choice(['buy', 'sell'])
                order_book[order_type].append(order)
    
    # Inicializando variáveis
    order_book: Dict[str, List[Dict[str, Any]]] = {'buy': [], 'sell': []} # Livro de ordens
    lock = threading.Lock() # Lock para garantir acesso exclusivo ao livro de ordens

    # Inicializando cada uma das threads
    threads = []
    for _ in range(num_traders):
        thread = threading.Thread(
            target=trader_worker,
            args=(num_ordens, order_book, lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Aguarda a finalização de cada thread

    return order_book
## 1. Teste Simulação de Traders Colocando Ordens Concorrentemente
def test_simular_traders():
    num_traders = 33
    ordens_per_trader = 111
    final_book = simular_traders(num_traders, ordens_per_trader)

    total_ordens = len(final_book['buy']) + len(final_book['sell'])
    print(f"Total de ordens no livro: {total_ordens}")
    print(f"Total de traders: {num_traders}")
    print(f"Ordens por trader: {ordens_per_trader}")
    print(f"Ordens de compra: {len(final_book['buy'])}")
    print(f"Ordens de venda: {len(final_book['sell'])}")

## 2. Simulação  de Feeds de Dados Concorrentes
def simular_feeds_de_dados(acoes: List[str], tempo_total: int) -> Dict[str, float]:
    """
    Simula feeds de dados concorrentes que atualizam um dicionário de preços.

    Args:
        acoes (List[str]): Lista de nomes de ações a serem monitoradas.
        tempo_total (int): Tempo total de simulação em segundos.

    Returns:
        Dict[str, float]: O dicionário final de preços após a simulação.
    """
    # Worker que simula o feed de dados para uma ação específica
    def feed_worker_data(
        acao: str,
        prices: Dict[str, float],
        lock: threading.Lock,
        stop_event: threading.Event
    ):
        """Thread que simula um feed de dados, atualizando o preço de uma ação."""
        while not stop_event.is_set(): # Em caso de parada, sai do loop e, consequentemente, encerra a thread
            novo_preco = round(random.uniform(1, 1000.0), 2)
            with lock:
                prices[acao] = novo_preco
            # Dorme por um período aleatório entre 1 e 3 segundos
            time.sleep(random.uniform(1, 3))
    # Worker que imprime os preços atuais a cada 5 segundos
    def printer_worker_data(
        prices: Dict[str, float],
        lock: threading.Lock,
        stop_event: threading.Event
    ):
        """Thread que imprime os preços atuais a cada 5 segundos."""
        while not stop_event.is_set():
            if stop_event.wait(timeout=5.0):
                break  # Encerra se o evento de parada foi acionado
            
            with lock:
                current_prices = dict(prices)

            print(f"\n--- Preços das ações às {time.strftime('%H:%M:%S')} ---")
            for acao, preco in current_prices.items():
                print(f" {acao}: ${preco:.2f}")
            print("---------------------------------------------")

    # Inicializando variáveis
    prices: Dict[str, float] = {acao: 0.0 for acao in acoes}
    lock = threading.Lock()
    stop_event = threading.Event()

    # Cria as threads de feed
    threads = []
    for acao in acoes:
        thread = threading.Thread(
            target=feed_worker_data,
            args=(acao, prices, lock, stop_event)
        )
        threads.append(thread)

    # Cria a thread de impressão
    printer = threading.Thread(
        target=printer_worker_data,
        args=(prices, lock, stop_event)
    )
    threads.append(printer)

    # Inicia todas as threads
    for thread in threads:
        thread.start()

    # Deixa a simulação rodar
    time.sleep(tempo_total)

    # Sinaliza o fim da simulação
    stop_event.set()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    return prices
## 2. Teste Simulação de Feeds de Dados Concorrentes
def test_simular_feeds_de_dados():
    acoes = ["BMGB4", "SANB11", "AMBP3"]
    duracao = 30  # segundos

    print(f"\nIniciando simulação de feeds de dados por {duracao} segundos...")
    precos_finais = simular_feeds_de_dados(acoes, duracao)
    print("Preços Finais:", precos_finais)

if __name__ == '__main__':
    # test_simular_traders()
    test_simular_feeds_de_dados()