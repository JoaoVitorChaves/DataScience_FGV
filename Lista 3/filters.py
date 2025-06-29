#### Lista 3 - Nome: João Vitor Ramos Chaves
import numpy as np
from typing import Tuple

### Parte 3 - Filtragem e Picos
## 1. Substituição condicional em vetores
def replace_negatives(v: np.ndarray, new_value: float) -> np.ndarray:
    # Passo 1 - Criar uma cópia do vetor para não modificar o original
    v_copy = v.copy()
    # Passo 2 - Criar uma máscara booleana. A máscara terá 'True' nas posições onde o valor em v_copy é menor que 0
    mask_negativos = v_copy < 0
    # Passo 3 - Usar a máscara para atribuir o novo valor. Apenas os elementos onde a máscara é 'True' serão modificados
    v_copy[mask_negativos] = new_value
    
    return v_copy
## 1. Teste Substituição condicional em vetores
def test_replace_negatives():
    vetor_original = np.array([10.0, -5.0, 0.0, 3.5])
    valor_substituto = 0.0
    vetor_modificado = replace_negatives(vetor_original, valor_substituto)

    print("Vetor original:")
    print(vetor_original)
    print(f"\nVetor com negativos substituídos por {valor_substituto}:")
    print(vetor_modificado)

## 2. Identificação de Máximos Locais em Série Temporal
def local_peaks(series: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Condição 1 - o ponto atual é maior que o vizinho da esquerda
    # series[1:-1] > series[:-2] compara x_t com x_{t-1} para todos os t possíveis
    condicao_esquerda = series[1:-1] > series[:-2]
    # Condição 2 - o ponto atual é maior que o vizinho da direita
    # series[1:-1] > series[2:] compara x_t com x_{t+1} para todos os t possíveis
    condicao_direita = series[1:-1] > series[2:]
    # Combina as duas condições. Um pico existe onde ambas são verdadeiras
    mask_picos = condicao_esquerda & condicao_direita
    # np.where(mask_picos) retorna os índices onde a máscara é True (somamos 1 para obter os índices corretos na série original)
    indices = np.where(mask_picos)[0] + 1
    peaks = series[indices]
    
    return indices, peaks
## 2. Teste Identificação de Máximos Locais em Série Temporal
def test_local_peaks():
    serie_teste = np.array([1, 5, 3, 4, 6, 42, 71, 57, 26])
    indices_picos, valores_picos = local_peaks(serie_teste)

    print(f"Série Original: {serie_teste}")
    print(f"Índices dos picos encontrados: {indices_picos}")
    print(f"Valores dos picos encontrados: {valores_picos}")

if __name__ == '__main__':
    # test_replace_negatives()
    test_local_peaks()