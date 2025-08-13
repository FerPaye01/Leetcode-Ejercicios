"""
Problem Statement
AtCoDeer the deer found two positive integers, a and b. Determine whether 
the product of a and b is even or odd.

Constraints
- 1 ≤ a, b ≤ 10000
- a and b are integers.

Input
Input is given from Standard Input in the following format:
a  b

Output
If the product is odd, print Odd; if it is even, print Even.

Sample Input 1
3 4

Sample Output 1
Even

As 3 × 4 = 12 is even, print Even.

Sample Input 2
1 21

Sample Output 2
Odd

As 1 × 21 = 21 is odd, print Odd.
"""
import sys
def procesar_dato(tokens):
    if len(tokens)<2:
        return
    entero_a = int(tokens[0])
    entero_b = int(tokens[1])
    if entero_a % 2 == 0 or entero_b % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
def main():
    if sys.stdin.isatty():
        casos_prueba =[
            ["3", "4"]
        ]
        for tokens in casos_prueba:
            print(f"---Caso de prueba : {tokens} ---")
            procesar_dato(tokens)
            print()
    else: 
        data = sys.stdin.read().split()
        procesar_dato(data)
if __name__ == "__main__":
    main()

