def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        
        for linha in matriz:
            linha.append(0)
            
        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        idx = vertices.index(vertice)
        
        matriz.pop(idx)
        
        for linha in matriz:
            linha.pop(idx)
            
        vertices.remove(vertice)


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    return False


def vizinhos(matriz, vertices, vertice):
    lista_vizinhos = []
    if vertice in vertices:
        i = vertices.index(vertice)
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                lista_vizinhos.append(vertices[j])
    return lista_vizinhos


def grau_vertices(matriz, vertices):
    graus = {}
    for i, vertice in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[linha][i] for linha in range(len(matriz)))
        total = entrada + saida
        graus[vertice] = {"saida": saida, "entrada": entrada, "total": total}
        
    return graus


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True
        
    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k+1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
            
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice in vertices:
        lista = vizinhos(matriz, vertices, vertice)
        print(f"Vizinhos de {vertice}: {lista}")
    else:
        print(f"Erro: O vértice '{vertice}' não existe no grafo.")


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("O grafo está vazio.")
        return

    print("\n--- Matriz de Adjacência ---")
    print("    " + " ".join(vertices))
    
    for i, vertice in enumerate(vertices):
        linha_str = " ".join(str(val) for val in matriz[i])
        print(f"{vertice} | {linha_str}")
    print("----------------------------\n")


def main():
    matriz, vertices = criar_grafo()
    
    while True:
        print("\n=== MENU DO GRAFO (MATRIZ) ===")
        print("1 - Mostrar a Matriz (Exibir Grafo)")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Calcular Graus dos Vértices")
        print("7 - Verificar Aresta")
        print("8 - Listar Vizinhos de um Vértice")
        print("9 - Verificar Percurso")
        print("0 - Sair")
        print("==============================")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            exibir_grafo(matriz, vertices)
            
        elif opcao == '2':
            v = input("Digite o nome do vértice a ser inserido: ").strip()
            inserir_vertice(matriz, vertices, v)
            print(f"Vértice '{v}' inserido!")
            
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("A aresta é não direcionada? (s/n): ").strip().lower()
            eh_nao_direcionado = (nd == 's')
            inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=eh_nao_direcionado)
            print(f"Aresta inserida entre {origem} e {destino}!")
            
        elif opcao == '4':
            v = input("Digite o nome do vértice a ser removido: ").strip()
            remover_vertice(matriz, vertices, v)
            print(f"Vértice '{v}' (e as suas conexões) removido(s)!")
            
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("A aresta era não direcionada? (s/n): ").strip().lower()
            eh_nao_direcionado = (nd == 's')
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado=eh_nao_direcionado)
            print("Aresta removida (se existia).")
            
        elif opcao == '6':
            graus = grau_vertices(matriz, vertices)
            if not graus:
                print("Grafo vazio.")
            else:
                for v, g in graus.items():
                    print(f"Vértice '{v}': Entrada = {g['entrada']}, Saída = {g['saida']}, Total = {g['total']}")
                    
        elif opcao == '7':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            if existe_aresta(matriz, vertices, origem, destino):
                print(f"Sim, EXISTE uma aresta de '{origem}' para '{destino}'.")
            else:
                print(f"Não, NÃO EXISTE uma aresta de '{origem}' para '{destino}'.")
                
        elif opcao == '8':
            v = input("Digite o nome do vértice para ver os vizinhos: ").strip()
            listar_vizinhos(matriz, vertices, v)
            
        elif opcao == '9':
            caminho_str = input("Digite os vértices do caminho separados por espaço (ex: A B C D): ")
            caminho = caminho_str.split()
            if percurso_valido(matriz, vertices, caminho):
                print(f"O percurso {caminho} é VÁLIDO.")
            else:
                print(f"O percurso {caminho} é INVÁLIDO (faltam conexões ou vértices).")
                
        elif opcao == '0':
            print("A encerrar o programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()