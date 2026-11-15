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

def menor_caminho_bfs(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        print("Erro: Vértice inicial ou destino não existe no grafo.")
        return []
        
    fila = [[inicio, [inicio]]]
    visitados = []
    
    while len(fila) > 0:
        item = fila.pop(0)
        vertice = item[0]
        caminho = item[1]
        
        if vertice == destino:
            return caminho
            
        if vertice not in visitados:
            visitados.append(vertice)
            
            lista_vizinhos = vizinhos(grafo, vertice)
            
            for vizinho in lista_vizinhos:
                vertice_na_fila = False
                for f in fila:
                    if f[0] == vizinho:
                        vertice_na_fila = True
                        break
                        
                if not vertice_na_fila and vizinho not in visitados:
                    novo_caminho = caminho + [vizinho]
                    fila.append([vizinho, novo_caminho])
                    
    return []

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
        print("\n=== MENU DO GRAFO (MENOR CAMINHO BFS) ===")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Encontrar Menor Caminho (BFS)")
        print("0 - Sair")
        print("========================================")
        
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
            inicio = input("Digite o vértice inicial: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            resultado = menor_caminho_bfs(grafo, inicio, destino)
            if resultado:
                print(f"Menor caminho de '{inicio}' até '{destino}': {resultado}")
            else:
                print(f"Não existe caminho entre '{inicio}' e '{destino}'.")
                
        elif opcao == '0':
            print("Encerrando o programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()