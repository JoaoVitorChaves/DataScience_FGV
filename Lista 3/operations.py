#### Lista 3 - Nome: João Vitor Ramos Chaves
import numpy as np

### Parte 2 - Operações em Vetores e Matrizes
## 1. Rotação de Matriz 90 no sentido horario
def rotate_90(A: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    # Cria-se uma matriz vazia para armazenar a transposta.
    B = np.zeros_like(A) 
    # Passo 1. Transpor a matriz A (trocar linhas por colunas), entao itera-se sobre cada elemento de A
    # E coloca-se na posição transposta em B 
    for i in range(n): # range(n) nos dois for-loops porque estamos trabalhando com matrizes quadradas
        for j in range(n):
            B[i, j] = A[j, i]
            
    # Passo 2: Inverter a ordem das colunas da matriz B
    A_rot = np.zeros_like(B)
    # Itera-se sobre cada elemento de B, a coluna 'j' da matriz final recebe a coluna 'n-1-j' da matriz B
    for i in range(n):
        for j in range(n):
            A_rot[i, j] = B[i, n - 1 - j]
            
    return A_rot
## 1. Teste Rotação de Matriz 90 graus no sentido horário
def test_rotate_90():
    A = np.array([[1, 1, 3],
                  [4, 4, 1],
                  [7, 3, 2]])
    A_rotated = rotate_90(A)
    
    print("Matriz Original:")
    print(A)
    print("Matriz Rotacionada 90 graus no sentido horário:")
    print(A_rotated)

## 2. Soma de subdiagonais de uma matriz
def sum_subdiagonals(A: np.ndarray, k: int) -> float:
    n = A.shape[0]
    soma = 0.0
    
    # Este loop segue diretamente a fórmula: soma de A[i, i-k] para i indo de k até n-1
    for i in range(k, n):
        soma += A[i, i - k]
        
    return soma
## 2. Teste Soma de subdiagonais
def test_sum_subdiagonals():
    matriz_teste = np.array([
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    k_val = 2

    soma_loops = sum_subdiagonals(matriz_teste, k_val)

    print(f"Soma da {k_val}ª subdiagonal (com loop): {soma_loops}")

## 3. Multiplicação de Matrizes em Blocos
def block_matmul(A: np.ndarray, B: np.ndarray, block_size: int) -> np.ndarray:
    m, p = A.shape
    q, n = B.shape
    C = np.zeros((m, n))

    # Restrições do exercício
    if (block_size <= 0 or p != q):
        print("Erro: As dimensões das matrizes não são compatíveis para multiplicação ou o tamanho do bloco é inválido.")
        return None
    
    # Os 3 loops aninhados correspondem aos índices i, j, k da multiplicação de matrizes, mas em nível de bloco
    # i0 e j0 varrem os blocos da matriz de resultado C
    for i0 in range(0, m, block_size):
        for j0 in range(0, n, block_size):
            # k0 varre a dimensão interna (colunas de A, linhas de B)
            for k0 in range(0, p, block_size):
                # Seleciona os blocos de A e B
                A_block = A[i0 : i0 + block_size, k0 : k0 + block_size]
                B_block = B[k0 : k0 + block_size, j0 : j0 + block_size]
                # Multiplica os blocos e soma o resultado
                C[i0 : i0 + block_size, j0 : j0 + block_size] += A_block @ B_block
                
    return C
## 3. Teste Multiplicação de Matrizes em Blocos
def test_block_matmul():
    A_teste = np.arange(16).reshape(4, 4)
    B_teste = np.identity(4) # Matriz identidade
    bl_size = 2

    C_resultado = block_matmul(A_teste, B_teste, bl_size)

    print(f"Resultado:\n{C_resultado}")
    # O resultado de A @ I é a própria matriz A
    print(f"O resultado é igual à matriz A? {np.array_equal(C_resultado, A_teste)}")

if __name__ == '__main__':
    # test_rotate_90()
    # test_sum_subdiagonals()
    test_block_matmul()