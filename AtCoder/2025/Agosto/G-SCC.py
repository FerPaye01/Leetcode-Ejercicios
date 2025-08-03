import sys
from array import array
from typing import List
from typing import Union
# Constantes del problema
MOD = 998244353
PRIMITIVE_ROOT = 3
def ntt(a: Union[array, list], roots: List[int]):
    n = len(a)
    
    # 1. Reordenamiento bit-reversal (in-place)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    # 2. Pasos de mariposa (Butterfly)
    # El truco es que `roots` ya contiene las bases `w_len` pre-calculadas.
    log_n = n.bit_length() - 1
    for i in range(log_n):
        len_block = 1 << (i + 1)
        half = 1 << i
        w_len = roots[i] # Acceso O(1) a la raíz pre-calculada
        
        for j in range(0, n, len_block):
            w = 1
            for k in range(j, j + half):
                # Las operaciones se realizan sobre enteros nativos del array
                u = a[k]
                v = (w * a[k + half]) % MOD
                a[k] = u + v
                if a[k] >= MOD:
                    a[k] -= MOD
                
                a[k + half] = u - v
                if a[k + half] < 0:
                    a[k + half] += MOD
                
                w = (w * w_len) % MOD

def main():
    data = sys.stdin.buffer.read().split()
    
    n_val = int(data[0])
    m_val = int(data[1])
    
    # --- Configuración de NTT ---
    final_len = n_val + m_val - 1
    log_size = (final_len - 1).bit_length()
    size = 1 << log_size
    
    # --- 1. Pre-cálculo de Raíces (Optimización Clave) ---
    roots = [0] * log_size
    inv_roots = [0] * log_size
    
    # Calculamos las raíces para cada nivel de la mariposa
    for i in range(log_size):
        angle = (MOD - 1) >> (i + 1)
        roots[i] = pow(PRIMITIVE_ROOT, angle, MOD)
        inv_roots[i] = pow(roots[i], MOD - 2, MOD)

    # --- 2. Preparación de Arrays (Tipo de dato `array.array`) ---
    # 'L' para unsigned long, que se ajusta a los valores del problema
    # Esto es mucho más eficiente en memoria y velocidad que una lista de Python
    a = array('q', map(int, data[2 : 2 + n_val]))  # 'q' es signed long long (64-bit con signo)
    a.extend([0] * (size - n_val))
    b = array('q', map(int, data[2 + n_val : 2 + n_val + m_val]))
    b.extend([0] * (size - m_val))

    ntt(a, roots)
    ntt(b, roots)

    c = array('q', (x * y % MOD for x, y in zip(a, b)))

    ntt(c, inv_roots)


    size_inv = pow(size, MOD - 2, MOD)
    for i in range(final_len):
        c[i] = (c[i] * size_inv) % MOD
        
    sys.stdout.write(" ".join(map(str, c[:final_len])) + "\n")


if __name__ == "__main__":
    main()