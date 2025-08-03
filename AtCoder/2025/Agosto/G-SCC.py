import sys

def procesar_entrada_scc(data):
    if not data:
        print(0)
        return
    
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        graph[a].append(b)
        rev_graph[b].append(a)

    visited1 = [False] * n
    next_index = [0] * n
    stack_dfs = []
    order_stack = []

    for i in range(n):
        if not visited1[i]:
            visited1[i] = True
            stack_dfs.append(i)
            while stack_dfs:
                u = stack_dfs[-1]
                if next_index[u] < len(graph[u]):
                    v = graph[u][next_index[u]]
                    next_index[u] += 1
                    if not visited1[v]:
                        visited1[v] = True
                        stack_dfs.append(v)
                else:
                    stack_dfs.pop()
                    order_stack.append(u)

    visited2 = [False] * n
    scc_list = []

    for node in reversed(order_stack):
        if not visited2[node]:
            comp = []
            stack_rev = [node]
            visited2[node] = True
            while stack_rev:
                u = stack_rev.pop()
                comp.append(u)
                for v in rev_graph[u]:
                    if not visited2[v]:
                        visited2[v] = True
                        stack_rev.append(v)
            comp.reverse()
            scc_list.append(comp)

    print(len(scc_list))
    for comp in scc_list:
        line = [str(len(comp))] + [str(x) for x in comp]
        print(" ".join(line))

def main():
    if sys.stdin.isatty():
        test_cases = [
            "6 7\n1 4\n5 2\n3 0\n5 5\n4 1\n0 3\n4 2"#,
            #"2 1\n0 1",
            #"0 0",
            #"1 0",
            #"2 2\n0 1\n1 0",
            #"3 3\n0 1\n1 2\n2 0"
        ]
        for tc in test_cases:
            print(f"--- Caso de prueba ---")
            print("Entrada:")
            print(tc)
            print("Salida:")
            data = tc.split()
            procesar_entrada_scc(data)
            print()
    else:
        data = sys.stdin.read().split()
        procesar_entrada_scc(data)

if __name__ == "__main__":
    main()