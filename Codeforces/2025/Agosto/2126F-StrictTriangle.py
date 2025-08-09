"""import sys
from heapq import heappush, heappop

def main():
    datos = list(map(int, sys.stdin.read().split()))
    it = iter(datos)
    t = next(it)
    SALIDAS = []
    INF = 10**30

    for _ in range(t):
        nodos = next(it); aristas = next(it); k = next(it)

        # listas de adyacencia separadas para l (ladrón) y r (policía)
        adj_l = [[] for _ in range(nodos + 1)]
        adj_r = [[] for _ in range(nodos + 1)]
        # leer aristas
        for _a in range(aristas):
            u = next(it); v = next(it); li = next(it); ri = next(it)
            adj_l[u].append((v, li)); adj_l[v].append((u, li))
            adj_r[u].append((v, ri)); adj_r[v].append((u, ri))

        # Dijkstra clásico desde k con pesos r -> dR[u]
        def dijkstra(adj, inicio):
            dist = [INF] * (nodos + 1)
            dist[inicio] = 0
            pq = [(0, inicio)]
            while pq:
                d, u = heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))
            return dist

        dR = dijkstra(adj_r, k)

        # Dijkstra modificado (estado: nodo con temporizador t)
        # t_u = mejor (mínimo) temporizador alcanzable para u
        t_mejor = [INF] * (nodos + 1)
        procesado = [False] * (nodos + 1)

        # inicio
        t_mejor[1] = -dR[1]
        pq = [(t_mejor[1], 1)]
        exito = False

        while pq:
            t_act, u = heappop(pq)
            if t_act != t_mejor[u]:
                continue
            # si los policías ya pueden llegar (o ya llegaron), no sirve esta situación
            if dR[u] <= t_act:
                continue
            if procesado[u]:
                continue
            procesado[u] = True
            if u == nodos:
                exito = True
                break
            # transitar por aristas (usa l)
            for v, li in adj_l[u]:
                t_sig = t_act + li
                if t_sig < -dR[v]:
                    t_sig = -dR[v]
                if t_sig < t_mejor[v]:
                    t_mejor[v] = t_sig
                    heappush(pq, (t_sig, v))

        SALIDAS.append("YES" if exito else "NO")

    sys.stdout.write("\n".join(SALIDAS))

if __name__ == "__main__":
    main()
"""


import sys
from heapq import heappush, heappop

def resolver_caso(nodos, aristas, k, lista_aristas):
    INF = 10**30

    # listas de adyacencia separadas para l (ladrón) y r (policía)
    adj_l = [[] for _ in range(nodos + 1)]
    adj_r = [[] for _ in range(nodos + 1)]
    for u, v, li, ri in lista_aristas:
        adj_l[u].append((v, li)); adj_l[v].append((u, li))
        adj_r[u].append((v, ri)); adj_r[v].append((u, ri))

    # Dijkstra clásico desde k con pesos r -> dR[u]
    def dijkstra(adj, inicio):
        dist = [INF] * (nodos + 1)
        dist[inicio] = 0
        pq = [(0, inicio)]
        while pq:
            d, u = heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        return dist

    dR = dijkstra(adj_r, k)

    # Dijkstra modificada para "temporizador"
    t_mejor = [INF] * (nodos + 1)
    procesado = [False] * (nodos + 1)

    t_mejor[1] = -dR[1]
    pq = [(t_mejor[1], 1)]
    while pq:
        t_act, u = heappop(pq)
        if t_act != t_mejor[u]:
            continue
        if dR[u] <= t_act:
            continue
        if procesado[u]:
            continue
        procesado[u] = True
        if u == nodos:
            return "YES"
        for v, li in adj_l[u]:
            t_sig = max(t_act + li, -dR[v])
            if t_sig < t_mejor[v]:
                t_mejor[v] = t_sig
                heappush(pq, (t_sig, v))
    return "NO"


def main():
    # === Definición de test cases ===
    test_cases = [
        # Cada caso: [n, m, k, (u,v,l,r)...]
        [4, 4, 2,
         (1, 2, 10, 20),
         (2, 3, 10, 30),
         (1, 3, 49, 90),
         (4, 3, 1, 1000)],

        [4, 4, 2,
         (1, 2, 10, 20),
         (2, 3, 10, 30),
         (1, 3, 50, 90),
         (4, 3, 1, 1000)]
        # Puedes añadir más casos del enunciado aquí
    ]

    # === Construcción de datos como si fuera stdin ===
    data = [str(len(test_cases))]
    for caso in test_cases:
        n = caso[0]; m = caso[1]; k = caso[2]
        data.extend([str(n), str(m), str(k)])
        for u, v, l, r in caso[3:]:
            data.extend([str(u), str(v), str(l), str(r)])

    # === Procesamiento ===
    t = int(data[0])
    index = 1
    resultados = []
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); k = int(data[index+2])
        index += 3
        aristas = []
        for _a in range(m):
            u = int(data[index]); v = int(data[index+1])
            l = int(data[index+2]); r = int(data[index+3])
            index += 4
            aristas.append((u, v, l, r))
        resultados.append(resolver_caso(n, m, k, aristas))

    # === Salida caso por caso ===
    print("\n".join(resultados))


if __name__ == "__main__":
    main()
