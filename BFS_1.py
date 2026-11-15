def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    grafo[origem].append(destino)
    if nao_direcionado:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []

def busca_largura(grafo, inicio):
    if inicio not in grafo:
        print(f"Erro: O vértice inicial '{inicio}' não existe no grafo.")
        return []
        
    fila = [inicio]
    visitados = []

    while len(fila) > 0:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)

            lista_vizinhos = vizinhos(grafo, vertice)

            for vizinho in lista_vizinhos:
                if vizinho not in fila:
                    if vizinho not in visitados:
                        fila.append(vizinho)
                        
    return visitados

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
        print("\n=== MENU DO GRAFO (BFS) ===")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Executar Busca em Largura (BFS)")
        print("0 - Sair")
        print("===========================")
        
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
            nd = input("A aresta é não direcionada? (s/n): ").strip().lower()
            inserir_aresta(grafo, origem, destino, nao_direcionado=(nd == 's'))
            print(f"Aresta inserida entre {origem} e {destino}!")
            
        elif opcao == '4':
            inicio = input("Digite o vértice inicial para a busca: ").strip()
            resultado = busca_largura(grafo, inicio)
            if resultado:
                print(f"Ordem dos grafos visitados: {resultado}")
                
        elif opcao == '0':
            print("Encerrando o programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()