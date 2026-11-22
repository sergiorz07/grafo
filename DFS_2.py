def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def inserir_aresta(grafo, origem, destino):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if origem not in grafo[destino]:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []

def vertice_na_pilha(pilha, vertice):
    for item in pilha:
        if item['vertice'] == vertice:
            return True
    return False

def detectar_ciclo(grafo, inicio, visitados=None):
    if inicio not in grafo:
        print(f"Erro: O vértice inicial '{inicio}' não existe no grafo.")
        return False

    pilha = [{'vertice': inicio, 'pai': None}]
    if visitados is None:
        visitados = []

    while len(pilha) > 0:
        item = pilha.pop()
        vertice = item['vertice']
        pai = item['pai']

        if vertice not in visitados:
            visitados.append(vertice)

        lista_vizinhos = vizinhos(grafo, vertice)

        for vizinho in lista_vizinhos:
            if not vertice_na_pilha(pilha, vizinho) and vizinho not in visitados:
                pilha.append({'vertice': vizinho, 'pai': vertice})
            else:
                if vizinho != pai:
                    print(f"Ciclo detectado na aresta '{vertice}' - '{vizinho}'.")
                    return True

    return False

def detectar_ciclo_grafo_todo(grafo):
    visitados = []
    for vertice in grafo:
        if vertice not in visitados:
            if detectar_ciclo(grafo, vertice, visitados):
                return True
    return False

def exibir_grafo(grafo):
    if not grafo:
        print("O grafo está vazio.")
        return
    print("\n--- Lista de Adjacência ---")
    for vertice in grafo:
        print(f"{vertice} -> {grafo[vertice]}")
    print("---------------------------\n")

def main():
    grafo = criar_grafo()

    while True:
        print("\n=== MENU DO GRAFO (DETECÇÃO DE CICLOS - DFS) ===")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta (não direcionada)")
        print("4 - Detectar ciclo a partir de um vértice")
        print("5 - Detectar ciclo no grafo inteiro")
        print("0 - Sair")
        print("================================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            exibir_grafo(grafo)

        elif opcao == '2':
            v = input("Digite o nome do vértice a ser inserido: ").strip()
            inserir_vertice(grafo, v)
            print(f"Vértice '{v}' inserido!")

        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            inserir_aresta(grafo, origem, destino)
            print(f"Aresta inserida entre {origem} e {destino}!")

        elif opcao == '4':
            inicio = input("Digite o vértice inicial para a busca: ").strip()
            if inicio in grafo:
                if detectar_ciclo(grafo, inicio):
                    print("Resultado: o grafo possui ciclo.")
                else:
                    print("Resultado: nenhum ciclo detectado.")
            else:
                print(f"Erro: O vértice '{inicio}' não existe no grafo.")

        elif opcao == '5':
            if detectar_ciclo_grafo_todo(grafo):
                print("Resultado: o grafo possui ciclo.")
            else:
                print("Resultado: nenhum ciclo detectado.")

        elif opcao == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()