def criar_grafo():

    return {}

def inserir_vertice(grafo, vertice):

    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"Aviso: O vértice '{vertice}' já existe.")

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
        
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
        
    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)

def vizinhos(grafo, vertice):

    if vertice in grafo:
        return grafo[vertice]
    return []

def listar_vizinhos(grafo, vertice):

    if vertice not in grafo:
        print(f"Erro: O vértice '{vertice}' não existe no grafo.")
        return []
    
    lista = vizinhos(grafo, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista

def exibir_grafo(grafo):

    if not grafo:
        print("O grafo está vazio.")
        return
        
    for vertice, lista_vizinhos in grafo.items():
        print(f"{vertice} -> {lista_vizinhos}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem not in grafo:
        return
        
    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        
    if nao_direcionado and destino in grafo:
        if origem in grafo[destino]:
            grafo[destino].remove(origem)

def remover_vertice(grafo, vertice, nao_direcionado=True):

    if vertice not in grafo:
        print(f"Erro: O vértice '{vertice}' não existe.")
        return False
        
    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)
            
    del grafo[vertice]
    print(f"Vértice '{vertice}' removido com sucesso.")
    return True

def existe_aresta(grafo, origem, destino):

    if origem in grafo:
        return destino in grafo[origem]
    return False

def grau_vertices(grafo):

    graus = {}
    for v in grafo:
        graus[v] = {'in': 0, 'out': 0, 'total': 0}
        
    for u in grafo:
        graus[u]['out'] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]['in'] += 1
                
    for v in graus:
        graus[v]['total'] = graus[v]['in'] + graus[v]['out']
        
    return graus

def percurso_valido(grafo, caminho):

    if len(caminho) < 2:
        return True
        
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            return False
            
    return True

def main():

    grafo = criar_grafo()
    nao_direcionado = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
    
    while True:
        print("\n--- MENU GRAFOS ---")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Remover Vértice")
        print("4 - Inserir Aresta")
        print("5 - Remover Aresta")
        print("6 - Calcular Grau dos Vértices")
        print("7 - Verificar Aresta")
        print("8 - Listar Vizinhos de um Vértice")
        print("9 - Verificar Percurso")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            exibir_grafo(grafo)
            
        elif opcao == '2':
            v = input("Digite o nome do vértice a inserir: ")
            inserir_vertice(grafo, v)
            
        elif opcao == '3':
            v = input("Digite o nome do vértice a remover: ")
            remover_vertice(grafo, v, nao_direcionado)
            
        elif opcao == '4':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            inserir_aresta(grafo, origem, destino, nao_direcionado)
            print(f"Aresta {origem}-{destino} inserida.")
            
        elif opcao == '5':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            remover_aresta(grafo, origem, destino, nao_direcionado)
            print(f"Aresta {origem}-{destino} removida (se existia).")
            
        elif opcao == '6':
            graus = grau_vertices(grafo)
            for v, g in graus.items():
                print(f"Vértice {v}: Entrada={g['in']}, Saída={g['out']}, Total={g['total']}")
                
        elif opcao == '7':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            if existe_aresta(grafo, origem, destino):
                print(f"Sim, existe aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta direta de {origem} para {destino}.")
                
        elif opcao == '8':
            v = input("Digite o nome do vértice: ")
            listar_vizinhos(grafo, v)
            
        elif opcao == '9':
            entrada = input("Digite os vértices do percurso separados por espaço (ex: A B C): ")
            caminho = entrada.split()
            if percurso_valido(grafo, caminho):
                print("O percurso é VÁLIDO.")
            else:
                print("O percurso é INVÁLIDO.")
                
        elif opcao == '0':
            print("Encerrando...")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()