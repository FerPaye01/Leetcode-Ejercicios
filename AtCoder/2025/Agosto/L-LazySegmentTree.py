import sys

def procesar_caso(tokens):
    if not tokens:
        return
    it = iter(tokens)
    n = int(next(it))  # Longitud del arreglo
    q = int(next(it))  # Número de consultas
    A = [int(next(it)) for _ in range(n)]  # Arreglo binario inicial

    size = 4 * n + 5  # Tamaño máximo del árbol de segmentos
    cnt0 = [0] * size  # Número de ceros por nodo
    cnt1 = [0] * size  # Número de unos por nodo
    inv_seg = [0] * size  # Número de inversiones por nodo
    lazy = [0] * size  # Marcador lazy de flip pendiente

    def aplicar_voltear(node):
        # Intercambia ceros y unos en el nodo y recalcula inversiones
        lazy[node] ^= 1
        cnt0[node], cnt1[node] = cnt1[node], cnt0[node]
        inv_seg[node] = cnt0[node] * cnt1[node] - inv_seg[node]

    def push(node):
        # Propaga la operación pendiente a los hijos
        if lazy[node]:
            aplicar_voltear(node * 2)
            aplicar_voltear(node * 2 + 1)
            lazy[node] = 0

    def pull(node):
        # Combina resultados de los hijos para actualizar el nodo
        left = node * 2
        right = node * 2 + 1
        cnt0[node] = cnt0[left] + cnt0[right]
        cnt1[node] = cnt1[left] + cnt1[right]
        inv_seg[node] = inv_seg[left] + inv_seg[right] + cnt1[left] * cnt0[right]

    def construir(node, l, r):
        # Construye el árbol de segmentos desde el arreglo inicial
        if l == r:
            if A[l - 1] == 0:
                cnt0[node] = 1
                cnt1[node] = 0
            else:
                cnt0[node] = 0
                cnt1[node] = 1
            inv_seg[node] = 0
            lazy[node] = 0
            return
        mid = (l + r) // 2
        construir(node * 2, l, mid)
        construir(node * 2 + 1, mid + 1, r)
        pull(node)

    def actualizar(node, l, r, ql, qr):
        # Aplica flip al rango [ql, qr] en O(log N)
        if ql <= l and r <= qr:
            aplicar_voltear(node)
            return
        if r < ql or qr < l:
            return
        push(node)
        mid = (l + r) // 2
        if ql <= mid:
            actualizar(node * 2, l, mid, ql, qr)
        if qr > mid:
            actualizar(node * 2 + 1, mid + 1, r, ql, qr)
        pull(node)

    def consultar(node, l, r, ql, qr):
        # Consulta inversiones y cuenta de 0/1 en rango [ql, qr]
        if ql <= l and r <= qr:
            return (cnt0[node], cnt1[node], inv_seg[node])
        if r < ql or qr < l:
            return (0, 0, 0)
        push(node)
        mid = (l + r) // 2
        if qr <= mid:
            return consultar(node * 2, l, mid, ql, qr)
        if ql > mid:
            return consultar(node * 2 + 1, mid + 1, r, ql, qr)
        left_res = consultar(node * 2, l, mid, ql, qr)
        right_res = consultar(node * 2 + 1, mid + 1, r, ql, qr)
        c0 = left_res[0] + right_res[0]
        c1 = left_res[1] + right_res[1]
        inv = left_res[2] + right_res[2] + left_res[1] * right_res[0]
        return (c0, c1, inv)

    construir(1, 1, n)  # Inicializa el árbol

    out_lines = []
    for _ in range(q):
        t = int(next(it))  # Tipo de operación
        lq = int(next(it))  # Límite izquierdo
        rq = int(next(it))  # Límite derecho
        if t == 1:
            actualizar(1, 1, n, lq, rq)  # Flip
        else:
            res = consultar(1, 1, n, lq, rq)  # Consulta
            out_lines.append(str(res[2]))  # Solo se imprime el número de inversiones

    sys.stdout.write("\n".join(out_lines))

def main():
    if sys.stdin.isatty():
        # Pruebas locales con el ejemplo y caso adicional
        tests = [
            "5 5\n0 1 0 0 1\n2 1 5\n1 3 4\n2 1 4\n1 1 3\n2 1 2\n",
            "3 4\n1 0 1\n2 1 3\n1 2 2\n2 1 3\n2 2 2\n"
        ]
        for t in tests:
            print("=== Test ===")
            procesar_caso(t.split())
            print()
    else:
        data = sys.stdin.read().split()
        procesar_caso(data)

if __name__ == "__main__":
    main()
