import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print("Resolviendo un sistema de ecuaciones lineales....")

    A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
    b = np.array([4, 1, 1])

    try:
        x = np.linalg.solve(A, b)
        print("Solucion del Sistema:")
        for i, valor in enumerate(x, start=1):
            print(f"x{i} = {valor:.4f}")
        return x
    except np.linalg.LinalgError:
        print("El sistema no tiene solucion o tiene soluciones infinitas")
        return None
    
def graficar_soluciones(soluciones):
    if soluciones is not None:
        print("Generando trafico de las soluciones")

        etiquetas = [f"x{i}" for i in range(1, len(soluciones) + 1)]
        plt.bar(etiquetas, soluciones, color=['blue', 'green', 'red'])
        plt.title("Soluciones del Sistema de Ecuaciones")
        plt.xlabel("Variables")
        plt.ylabel("Valores")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.savefig("soluciones.png")
        plt.close()
        print("Grafico guardado en 'soluciones.png'")
    else:
        print("No se pudo generar el grafico deseado")

def guardar_resulatados_csv(soluciones):
    if soluciones is not None:
        print("Guardando soluciones en un archivo CSV")

        with open("resultados.csv", mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Variable", "Valor"])
            for i, valor in enumerate(soluciones, start=1):
                escritor.writerow([f"x{i}", f"{valor:.4f}"])
        print("Resultados guardados en un Archivo CSV")
    else:
        print("No se puedieron guardar los resultados")

def main():
    print("=== Sistema de Ecuaciones Lineales ===")

    soluciones = resolver_sistema()

    graficar_soluciones(soluciones)

    guardar_resulatados_csv(soluciones)

if __name__ == "__main__":
    main()