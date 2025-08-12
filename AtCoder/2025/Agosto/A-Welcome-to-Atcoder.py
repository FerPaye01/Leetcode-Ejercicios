#!/usr/bin/env python3  # Shebang: seleccionar intérprete Python disponible en el sistema
# -*- coding: utf-8 -*-  # Codificación del archivo para compatibilidad con textos

import sys  # Importar módulo para manejar entrada/salida y detectar TTY

def procesar_caso(tokens):  # Función principal que procesa los tokens de entrada
    if not tokens:  # Verificar que existan tokens; si no, salir sin producir salida
        return  # Salida temprana cuando no hay datos

    a = int(tokens[0])  # Parsear primer entero 'a' desde el primer token
    b = int(tokens[1])  # Parsear segundo entero 'b' desde el segundo token
    c = int(tokens[2])  # Parsear tercer entero 'c' desde el tercer token

    raw_s = tokens[3]  # Tomar el token correspondiente a la cadena 's' en crudo
    s = raw_s.decode() if isinstance(raw_s, bytes) else raw_s  # Normalizar 's' a str si viene como bytes

    suma = a + b + c  # Calcular suma de a, b y c de forma entera
    print(f"{suma} {s}")  # Imprimir resultado en una sola línea separado por espacio de medio ancho

def main():  # Punto de entrada del programa
    if sys.stdin.isatty():  # Modo interactivo / prueba local cuando la entrada es TTY
        # Casos de prueba (emulan ejemplos y casos habituales) para verificación rápida
        casos_prueba = [
            ["1", "2", "3", "test"],          # Ejemplo: 1, 2 3, "test" -> 6 test
            ["72", "128", "256", "myonmyon"], # Ejemplo: 72, 128 256, "myonmyon" -> 456 myonmyon
        ]
        for tokens in casos_prueba:  # Iterar casos y mostrar resultado de cada uno
            print(f"--- Caso de prueba: {tokens} ---")  # Encabezado claro por caso
            procesar_caso(tokens)  # Procesar caso de prueba
            print()  # Separador visual entre casos
    else:  # Modo concurso / ejecución normal: leer desde stdin de forma eficiente
        datos = sys.stdin.buffer.read().split()  # Leer todo en bytes y tokenizar por espacios/nuevas líneas
        procesar_caso(datos)  # Procesar tokens leídos desde la entrada estándar

if __name__ == "__main__":  # Guardar ejecución cuando se importe como módulo
    main()  # Ejecutar la función principal
