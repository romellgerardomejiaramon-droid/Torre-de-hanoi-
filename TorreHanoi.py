
import time

def torre_hanoi(discos, origen, auxiliar, destino, movimientos, limite):
    if len(movimientos) >= limite:
        return

    if discos == 1:
        movimientos.append((1, origen, destino))
        return

    torre_hanoi(discos - 1, origen, destino, auxiliar, movimientos, limite)

    if len(movimientos) < limite:
        movimientos.append((discos, origen, destino))

    torre_hanoi(discos - 1, auxiliar, origen, destino, movimientos, limite)

def convertir_tiempo(segundos):
    if segundos < 60:
        return str(round(segundos, 4)) + " segundos"
    elif segundos < 3600:
        return str(round(segundos / 60, 2)) + " minutos"
    elif segundos < 86400:
        return str(round(segundos / 3600, 2)) + " horas"
    elif segundos < 31536000:
        return str(round(segundos / 86400, 2)) + " dias"
    else:
        return str(round(segundos / 31536000, 2)) + " años"

def main():
    cantidades = [5, 10, 30, 64]
    tiempo_total = 0
    tiempo_por_movimiento = 0

    for discos in cantidades:
        print("\nTORRE DE HANOI:", discos, "DISCOS")

        inicio = time.perf_counter()

        total = 2 ** discos - 1
        movimientos = []

        if discos <= 10:
            limite = total
        else:
            limite = 30

        torre_hanoi(discos, "A", "B", "C", movimientos, limite)

        for numero, (disco, origen, destino) in enumerate(movimientos, 1):
            print(numero, "- Mover disco", disco, "de", origen, "a", destino)

        fin = time.perf_counter()
        tiempo = fin - inicio
        tiempo_total += tiempo

        print("Total de movimientos:", total)
        print("Movimientos mostrados:", len(movimientos))
        print("Tiempo de ejecucion:", tiempo, "segundos")

        if discos == 10 and len(movimientos) > 0:
            tiempo_por_movimiento = tiempo / len(movimientos)

        if tiempo_por_movimiento > 0:
            tiempo_estimado = total * tiempo_por_movimiento
            print("Tiempo aproximado para completar todo:", convertir_tiempo(tiempo_estimado))
        else:
            print("Tiempo aproximado: no disponible")

    print("\nTIEMPO TOTAL DE LAS PRUEBAS:", tiempo_total, "segundos")

main()
