import sys

def procesar_caso(data):
    if not data:
        return
    
    n = int(data[0])
    d = int(data[1])
    flags = []
    index = 2
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        flags.append((x, y))
    
    total_nodes = 2 * n
    graph = [[] for _ in range(total_nodes)]
    
    for i in range(n):
        for j in range(i + 1, n):
            for a in [0, 1]:
                for b in [0, 1]:
                    pos_i = flags[i][a]
                    pos_j = flags[j][b]
                    if abs(pos_i - pos_j) < d:
                        node_i_a = 2 * i + a
                        node_j_b = 2 * j + b
                        node_i_not_a = 2 * i + (1 - a)
                        node_j_not_b = 2 * j + (1 - b)
                        graph[node_i_a].append(node_j_not_b)
                        graph[node_j_b].append(node_i_not_a)
    
    visited = [False] * total_nodes
    order = []
    next_index = [0] * total_nodes
    stack = []
    for i in range(total_nodes):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            while stack:
                node = stack[-1]
                if next_index[node] < len(graph[node]):
                    neighbor = graph[node][next_index[node]]
                    next_index[node] += 1
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                else:
                    stack.pop()
                    order.append(node)
    
    rev_graph = [[] for _ in range(total_nodes)]
    for u in range(total_nodes):
        for v in graph[u]:
            rev_graph[v].append(u)
    
    visited2 = [False] * total_nodes
    comp = [-1] * total_nodes
    current_comp = 0
    next_index2 = [0] * total_nodes
    order.reverse()
    for node in order:
        if not visited2[node]:
            stack2 = [node]
            visited2[node] = True
            comp[node] = current_comp
            while stack2:
                cur = stack2[-1]
                if next_index2[cur] < len(rev_graph[cur]):
                    neighbor = rev_graph[cur][next_index2[cur]]
                    next_index2[cur] += 1
                    if not visited2[neighbor]:
                        visited2[neighbor] = True
                        comp[neighbor] = current_comp
                        stack2.append(neighbor)
                else:
                    stack2.pop()
            current_comp += 1
    
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("No")
            return
    
    print("Yes")
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            print(flags[i][0])
        else:
            print(flags[i][1])

def main():
    if sys.stdin.isatty():
        # Modo de prueba local: ejecutar casos de prueba predefinidos
        test_cases = [
            ["3", "2", "1", "4", "2", "5", "0", "6"],  
            ["3", "3", "1", "4", "2", "5", "0", "6"],  
        ]
        for tokens in test_cases:
            print(f"--- Caso de prueba: {tokens} ---")
            procesar_caso(tokens)
            print()
    else:
        data = sys.stdin.read().split()
        procesar_caso(data)

if __name__ == "__main__":
    main()