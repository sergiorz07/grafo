def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    
    arestas.append([origem, destino])
    
    if nao_direcionado:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
        
    if nao_direcionado:
        if [destino, origem] in arestas:
            arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        
    arestas[:] = [aresta for aresta in arestas if aresta[0] != vertice and aresta[1] != vertice]


def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    lista_vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            lista_vizinhos.append(destino)
    return lista_vizinhos


def grau_vertices(vertices, arestas):
    graus = {v: {'entrada': 0, 'saida': 0, 'total': 0} for v in vertices}
    
    for origem, destino in arestas:
        graus[origem]['saida'] += 1
        graus[destino]['entrada'] += 1
        
    for v in vertices:
        graus[v]['total'] = graus[v]['entrada'] + graus[v]['saida']
        
    return graus


def percurso_valido(arestas, caminho):
    if len(caminho) < 2:
        return True
        
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]
        if not existe_aresta(arestas, u, v):
            return False
            
    return True


def listar_vizinhos(vertices, arestas, vertice):
    if vertice in vertices:
        lista = vizinhos(vertices, arestas, vertice)
        print(f"Vizinhos de {vertice}: {lista}")
    else:
        print(f"Erro: O vértice '{vertice}' não existe no grafo.")


def exibir_grafo(vertices, arestas):
    if not vertices:
        print("O grafo está vazio.")
        return
        
    print("\n--- Lista de Arestas ---")
    print(f"Vértices: {vertices}")
    print("Arestas:")
    if not arestas:
        print("  (nenhuma aresta)")
    for origem, destino in arestas:
        print(f"  {origem} -> {destino}")
    print("------------------------\n")


def main():
    vertices, arestas = criar_grafo()
    
    while True:
        print("\n=== MENU DO GRAFO (LISTA DE ARESTAS) ===")
        print("1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Calcular Graus dos Vértices")
        print("7 - Verificar Aresta")
        print("8 - Listar Vizinhos de um Vértice")
        print("9 - Verificar Percurso")
        print("0 - Sair")
        print("========================================")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            exibir_grafo(vertices, arestas)
            
        elif opcao == '2':
            v = input("Digite o nome do vértice a ser inserido: ").strip()
            inserir_vertice(vertices, v)
            print(f"Vértice '{v}' inserido!")
            
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("A aresta é não direcionada? (s/n): ").strip().lower()
            eh_nao_direcionado = (nd == 's')
            inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=eh_nao_direcionado)
            print(f"Aresta inserida entre {origem} e {destino}!")
            
        elif opcao == '4':
            v = input("Digite o nome do vértice a ser removido: ").strip()
            remover_vertice(vertices, arestas, v)
            print(f"Vértice '{v}' (e suas conexões) removido(s)!")
            
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("A aresta era não direcionada? (s/n): ").strip().lower()
            eh_nao_direcionado = (nd == 's')
            remover_aresta(arestas, origem, destino, nao_direcionado=eh_nao_direcionado)
            print("Aresta removida (se existia).")
            
        elif opcao == '6':
            graus = grau_vertices(vertices, arestas)
            if not graus:
                print("Grafo vazio.")
            else:
                for v, g in graus.items():
                    print(f"Vértice '{v}': Entrada = {g['entrada']}, Saída = {g['saida']}, Total = {g['total']}")
                    
        elif opcao == '7':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            if existe_aresta(arestas, origem, destino):
                print(f"Sim, EXISTE uma aresta de '{origem}' para '{destino}'.")
            else:
                print(f"Não, NÃO EXISTE uma aresta de '{origem}' para '{destino}'.")
                
        elif opcao == '8':
            v = input("Digite o nome do vértice para ver os vizinhos: ").strip()
            listar_vizinhos(vertices, arestas, v)
            
        elif opcao == '9':
            caminho_str = input("Digite os vértices do caminho separados por espaço (ex: A B C D): ")
            caminho = caminho_str.split()
            if percurso_valido(arestas, caminho):
                print(f"O percurso {caminho} é VÁLIDO.")
            else:
                print(f"O percurso {caminho} é INVÁLIDO (faltam conexões).")
                
        elif opcao == '0':
            print("Encerrando o programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()