#### Lista 1 - Nome: João Vitor Ramos Chaves

### Parte 1 - Lista e Tuplas
## 1. Números Pares e Impares
def pares_e_impares(nums):
    # Duas listas de pares e ímpares que retornarão pós execução do código
    pares = []
    impares = []

    # Iterador for-loop para verificar a paridade de cada número com o método resto
    # Se o resto for zero é par; Se for diferente de zero é impar -> Com base nessas duas condições, pode-se
    # popular as duas listas de interesse
    for numero in nums:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    # Retorno com as duas listas
    return pares, impares
## 1. Teste dos Números Pares e Ímpares
def teste_pares_e_impares():
    list_teste = [1,2,3,4,5,6,7,8,9,10]
    pares, impares = pares_e_impares(list_teste)
    print(f"Lista: {', '.join(map(str, list_teste))}")
    print(f"Pares: {", ".join(map(str, pares))}")
    print(f"Ímpares: {", ".join(map(str, impares))}")

## 2. Filtrar por Comprimento
def filtrar_por_tamanho(lista_palavras, k):
    # Lista inicializada para armazenar apenas as palavras que possuem mais de k caracteres
    palavras_filtradas = []

    # Iteramos sobre cada palavra na lista de entrada e verificamos atraves do if se o comprimento da palavra é maior que k
    # Se sim, adicionamos a palavra à lista de palavras filtradas
    for palavra in lista_palavras:
        if len(palavra) > k:
            palavras_filtradas.append(palavra)

    # Retorno com a lista de palavras filtradas
    return palavras_filtradas
## 2. Teste do Filtro por Comprimento
def teste_filtrar_por_tamanho():
    lista_teste = ['abacaxi', 'banana', 'laranja', 'uva', 'kiwi']
    k = 5
    resultado = filtrar_por_tamanho(lista_teste, k)
    print(f"Lista original: {lista_teste}")
    print(f"Palavras com mais de {k} caracteres: {resultado}")

## 3. Rotação de Tupla
def rotate_tuple(tpl, n):
    # Retorna a tupla original se n for maior
    if n > len(tpl):
        return tpl  

    # Realiza a rotação da tupla
    return tpl[n:] + tpl[:n]
## 3. Teste da Rotação de Tupla
def teste_rotate_tuple():
    tpl_teste = (1, 2, 2, 1, 2)
    n = 2
    resultado = rotate_tuple(tpl_teste, n)
    print(f"Tupla original: {tpl_teste}")
    print(f"Tupla rotacionada por {n} posições: {resultado}")

## 4. Transposta de Matriz
def transpose(matrix):
    # Caso seja enviado uma matriz vazia ou com linhas vazias, retorna-se uma matriz vazia
    if not matrix or not matrix[0]:
        return []

    # Obtem-se o número de linhas e colunas da matriz original (pensando numa matriz m x n)
    num_linhas = len(matrix)
    num_colunas = len(matrix[0])

    # A solucao foi usar o metodo de  "list comprehension".
    # Em que a matriz transposta sera dada agora por matriz n x m
    transposta = [[matrix[j][i] for j in range(num_linhas)] for i in range(num_colunas)]

    # Retorna-se entao a matriz transposta já preenchida
    return transposta
## 4. Teste da Transposta de Matriz
def teste_transpose():
    matriz_teste = [
        [1, 2, 2],
        [4, 3, 1],
        [7, 5, 6]
    ]
    resultado = transpose(matriz_teste)
    print("Matriz original:")
    for linha in matriz_teste:
        print(linha)
    print("Matriz transposta:")
    for linha in resultado:
        print(linha)

## 5. Alisamento de Lista Aninhada
def flatten(lst):
    # Inicializa-se uma lista que será o resultado achatado
    lista_achatada = []

    # Itera-se sobre cada item na lista de entrada
    for item in lst:
        # Verificamos se o item atual é do tipo 'list'
        # Se for, chamamos recursivamente a função 'flatten' para achatar esse item
        if isinstance(item, list):
            lista_achatada.extend(flatten(item))
        else:
            # Se o item não for uma lista, então basta adicioná-lo na lista de resultado
            lista_achatada.append(item)

    # Retorna-se a lista achatada
    return lista_achatada
## 5. Teste do Alisamento de Lista Aninhada
def teste_flatten():
    lista_teste = [1, [3, 2], [6, [5, 1]], 7]
    resultado = flatten(lista_teste)
    print(f"Lista original: {lista_teste}")
    print(f"Lista achatada: {resultado}")

### Parte 2 - Dicionários
## 1. Agrupamento por Chave
def group_by(pairs):
    # Inicializa-se um dicionário vazio que irá armazenar o resultado agrupado
    grouped_dict = {}

    # Itera-se sobre cada tupla (que contém uma chave e um valor) na lista de entrada
    for key, value in pairs:
        # Verifica-se se a chave já foi adicionada ao dicionário
        if key not in grouped_dict:
            # Se for a primeira vez que vemos essa chave, cria-se uma nova entrada e associa-se a ela uma lista contendo o valor atual
            grouped_dict[key] = [value]
        else:
            # Se a chave já existe, significa que já temos uma lista para ela, entao basta adicionar o valor atual a essa lista
            grouped_dict[key].append(value)

    # \Retornamos o dicionário com todos os valores devidamente agrupados
    return grouped_dict
## 1. Teste do Agrupamento por Chave
def teste_group_by():
    lista_teste = [('A', 1), ('B', 2), ('A', 1), ('C', 3), ('B', 5)]
    resultado = group_by(lista_teste)
    print("Lista original:")
    print(lista_teste)
    print("Dicionário agrupado:")
    for key, values in resultado.items():
        print(f"{key}: {values}")

## 2. Inversão de Mapeamento
def invert_map(d):
    # Inicializa-se o dicionário que armazenará o resultado invertido
    inverted_dict = {}

    # Através do método .items() é possível iterar sobre par-valor. Com isso, basta inverter valor e chave na
    # variável inverted_dict
    for key, value in d.items():
        inverted_dict[value] = key

    # Retorna-se o dicionário invertido
    return inverted_dict
## 2. Teste da Inversão de Mapeamento
def teste_invert_map():
    d_teste = {'a': 1, 'b': 2, 'c': 3}
    resultado = invert_map(d_teste)
    print("Dicionário original:")
    print(d_teste)
    print("Dicionário invertido:")
    print(resultado)

## 3. Índices por Valor
def indices_of(lst):
    # Inicializa-se o dicionário para mapeamento dos valores a suas listas de índices
    indices_dict = {}

    # Através da enumerate() podemos saber o índice onde está cada item e o também acesso ao próprio item
    for i, item in enumerate(lst):
        # Verifica-se primeiramente se o item já foi adicionado como chave ao dicionário, se não foi, então
        # criamos uma nova entrada com o item como chave e uma lista contendo o índice atual
        if item not in indices_dict:
            indices_dict[item] = [i]
        else:
            # Se o item já existe como chave, apenas adicionamos o novo índice à sua lista
            indices_dict[item].append(i)

    # Retorna-se o dicionário completo
    return indices_dict
## 3. Teste dos Índices por Valor
def teste_indices_of():
    lista_teste = ['a', 'b', 'a', 'c', 'b', 'a']
    resultado = indices_of(lista_teste)
    print("Lista original:")
    print(lista_teste)
    print("Dicionário de índices por valor:")
    for key, indices in resultado.items():
        print(f"{key}: {indices}")

## 4. Fusão com Resolução de Conflitos
def merge_dicts(dicts):
    # Inicializa-se o dicionário que conterá a fusão de todos os outros
    merged_dict = {}

    # Itera-se sobre cada um dos dicionários da lista de entrada
    for d in dicts:
        for key, value in d.items():
            # Verifica-se se a chave já está no dicionário de resultado. Se não estiver, colocar como valor
            # Se já estiver, então somamos o valor atual ao valor que já estava lá
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value

    # Retorna-se o dicionário finalizado.
    return merged_dict
## 4. Teste da Fusão com Resolução de Conflitos
def teste_merge_dicts():
    dicts_teste = [
        {'a': 1, 'b': 2},
        {'b': 8, 'c': 4},
        {'a': 5, 'd': 5}
    ]
    resultado = merge_dicts(dicts_teste)
    print("Dicionários originais:")
    for d in dicts_teste:
        print(d)
    print("Dicionário mesclado:")
    print(resultado)

## 5. Contador de Dígitos
def conta_digitos(n):
    # Inicializa-se o dicionário para a contagem dos dígitos
    digit_counts = {}

    # Convertemos o número para sua representação em string. Atraves do abs() podemos passar a aceitar numeros negativos
    # para a entrada
    number_as_string = str(abs(n))

    # Com esse for-loop é possível iterar sobre cada caractere. No resultado de resultado, a chave é cada caractere
    # e o valor é a contagem de quantas vezes esse caractere aparece no número
    # Se o dígito ainda não está no dicionário, colocamos como 1 o valor inicial. Se estiver, somamos 1
    for digit_char in number_as_string:
        if digit_char in digit_counts:
            digit_counts[digit_char] += 1
        else:
            digit_counts[digit_char] = 1

    # Retorna-se o dicionário com as contagens.
    return digit_counts
## 5. Teste do Contador de Dígitos
def teste_conta_digitos():
    numero_teste = 454643549687154
    resultado = conta_digitos(numero_teste)
    print(f"Número: {numero_teste}")
    print("Contagem de dígitos:")
    for digit, count in resultado.items():
        print(f"{digit}: {count}")

### Parte 3: Desafios de Funções
## 1. Contador de Anagramas
def count_anagrams(words):
    # Dicionário para agrupar os anagramas. A chave será a palavra ordenada em ordem alfabética
    anagrams_dict = {}

    # Itera sobre cada palavra na lista de entrada
    for word in words:
        # Cria a "chave canônica" do anagrama
        # sorted(word) retorna uma lista de caracteres em ordem alfabética
        # "".join() é usado para transformar essa lista de volta em uma string
        # Ex: "lobo" -> ['b', 'l', 'o', 'o'] -> "bloo"
        sorted_word = "".join(sorted(word))

        # Comentário: Verifica se a chave canônica já existe no dicionário
        # Se a palavra ordenada nao existe, inicia uma lista com a palavra atual
        # Se já existe, adiciona a palavra atual à lista de anagramas
        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        else:
            anagrams_dict[sorted_word].append(word)

    return anagrams_dict
## 1. Teste do Contador de Anagramas
def teste_count_anagrams():
    lista_teste = ['lobo', 'bolo', 'olbo', 'gato', 'toga', 'atog']
    resultado = count_anagrams(lista_teste)
    print("Lista original:")
    print(lista_teste)
    print("Anagramas encontrados:")
    for key, anagrams in resultado.items():
        print(f"{key}: {anagrams}")

## 2. Parser de CSV
def parse_csv(text, sep=','):
    # Aqui na solucao, o strip() é usado para remover espaços em branco no início e no final do texto
    # Divide o texto em linhas, removendo espaços/linhas em branco
    lines = text.strip().split('\n')

    # A primeira linha contém os cabeçalhos (representando a primeira linha com o indice 0)
    # E Inicializa o dicionário usando os cabeçalhos como chaves
    headers = [h.strip() for h in lines[0].split(sep)]
    data_dict = {header: [] for header in headers}

    # Itera sobre as linhas de dados (todas, exceto a primeira de cabeçalho)
    for line in lines[1:]:
        # Divide a linha em valores usando o separador
        values = line.split(sep)

        # Itera sobre os cabeçalhos usando o índice para alinhar com os valores
        for i, header in enumerate(headers):
            value_str = values[i].strip()
            # Tenta converter o valor para inteiro. Se falhar, mantém como string 
            # (poderia usar isinstance, mas essa essan solucao é mais simples)
            try:
                value = int(value_str)
            except ValueError:
                value = value_str

            # Adiciona o valor processado à lista da coluna correta
            data_dict[header].append(value)

    return data_dict
## 2. Teste do Parser de CSV
def teste_parse_csv():
    csv_text = """
    Altura, Nome, Idade
    177, Pedro, 21
    191, Carlos, 33
    169, Alice, 23
    """
    dados_extraidos = parse_csv(csv_text)
    print("Texto CSV Original:")
    print(csv_text)
    print("\nDicionário Resultante:")
    print(dados_extraidos)

## 3. Validação de Soduku
def validar_sudoku(tabuleiro):
    # Módulo auxiliar para verificar uma única unidade (linha, coluna ou bloco 3x3)
    def tem_duplicatas(unidade):
        # Comentário: 'vistos' será um conjunto para armazenar os números que já encontramos
        # A ideia de um set() é que eles são eficientes para verificar a existência de um item
        vistos = set()
        for num in unidade:
            # Ignoramos os espaços vazios, representados por 0 (dito no enunciado)
            if num == 0:
                continue
            # Comentário: Se o número já está no conjunto 'vistos', encontramos uma duplicata.
            if num in vistos:
                return True # Retorna True para indicar que HÁ duplicatas
            # Adicionamos o número ao conjunto de números já vistos
            vistos.add(num)
        # Retorna-se False se não houver duplicatas na unidade
        return False

    # 1. Validação de linhas - Sabemos que o tabuleiro dado são de 9 linhas no total, então para verificar as linhas
    # iterar sobre as linhas
    for i in range(9):
        if tem_duplicatas(tabuleiro[i]):
            return False

    # 1. Validação de Colunas - Mesma coisa com as colunas
    for j in range(9):
        coluna = [tabuleiro[i][j] for i in range(9)]
        if tem_duplicatas(coluna):
            return False

    # 3. Validação dos blocos 3x3 - itera-se sobre os cantos superiores esquerdos de cada bloco (0, 3, 6).
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Extraímos todos os 9 elementos do bloco atual em uma lista.
            bloco = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    bloco.append(tabuleiro[x][y])
            if tem_duplicatas(bloco):
                return False

    # Retorna True se todas as linhas, colunas e blocos forem válidos
    return True
### 3. Teste da Validação de Sudoku
def teste_validar_sudoku():
    tabuleiro_teste = [
        [0, 0, 3, 0, 5, 0, 6, 0, 0],
        [1, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 2, 1, 8, 0, 4, 0, 0, 0],
        [0, 0, 8, 1, 0, 2, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 5, 7, 0, 1, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [6, 0, 0, 2, 4, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]
    ]
    resultado = validar_sudoku(tabuleiro_teste)
    print("Tabuleiro de Sudoku:")
    for linha in tabuleiro_teste:
        print(linha)
    print(f"Tabuleiro é válido? {'Sim' if resultado else 'Não'}")

if __name__ == '__main__':
    # Part 1
    # teste_pares_e_impares()
    # teste_filtrar_por_tamanho()
    # teste_rotate_tuple()
    # teste_transpose()
    # teste_flatten()
    # Part 2
    # teste_group_by()
    # teste_invert_map()
    # teste_indices_of()
    # teste_merge_dicts()
    # teste_conta_digitos()
    # Part 3
    # teste_count_anagrams()
    # teste_parse_csv()
    teste_validar_sudoku()
