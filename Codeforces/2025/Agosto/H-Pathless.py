import sys

def main():
    # ---> Para stdin: descomenta abajo y comenta hasta "# comentario"
    # data = sys.stdin.read().split()
    test_cases = [
        (3, 2, [0, 1, 2]),
        (3, 3, [0, 1, 2]),
        (3, 6, [0, 1, 2]),
        (3, 4, [0, 1, 2]),
        (3, 10, [0, 1, 2]),
        (5, 1000, [2, 0, 1, 1, 2])
    ]
    data = [str(len(test_cases))]
    for n, s, a in test_cases:
        data.append(str(n))
        data.append(str(s))
        data.extend(map(str, a))
    # comentario
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        s = int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n

        c0 = a.count(0)
        c1 = a.count(1)
        c2 = a.count(2)
        total_sum = c1 + 2 * c2

        if s < total_sum:
            a_sorted = sorted(a)
            output_lines.append(" ".join(map(str, a_sorted)))
        elif s - total_sum == 1:
            arr = [0] * c0 + [2] * c2 + [1] * c1
            output_lines.append(" ".join(map(str, arr)))
        else:
            output_lines.append("-1")
    
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()