# Torre de Hanoi en Python

 Introduccion

Este programa fue realizado en Python para resolver el problema de la Torre de Hanoi. El programa permite probar diferentes cantidades de discos y observar cuantos movimientos se necesitan para resolverlo.

Se realizaron pruebas con **5, 10, 30 y 64 discos**, tomando en cuenta el numero de movimientos y el tiempo de ejecucion.

 Funcionamiento del programa

El programa comienza probando las cantidades de discos indicadas. Para cada cantidad, la funcion `torre_hanoi()` se encarga de realizar los movimientos de los discos entre las torres.

Para 5 y 10 discos, el programa muestra todos los movimientos realizados. Para 30 y 64 discos, solamente muestra los primeros 30 movimientos, ya que realizar y mostrar todos los movimientos tomaria demasiado tiempo.

El programa tambien calcula el total de movimientos que se necesitan y mide cuanto tiempo tarda en realizar la prueba. La funcion `convertir_tiempo()` ayuda a mostrar el tiempo en segundos, minutos, horas, dias o anos.

Al final se muestran los resultados de cada prueba.

 Metodos utilizados

El programa tiene **3 metodos**:

- **torre_hanoi():** Se encarga de hacer los movimientos de los discos entre las torres.
- **convertir_tiempo():** Sirve para convertir el tiempo de segundos a minutos, horas, dias o años.
- **main():** Es donde se ejecuta el programa. Aqui se prueban las cantidades de 5, 10, 30 y 64 discos y se muestran los resultados.

En total, el programa utiliza **3 metodos**.

 Resultados de las pruebas

| Cantidad de discos | Total de movimientos | Movimientos mostrados |
|---:|---:|---:|
| 5 | 31 | 31 |
| 10 | 1,023 | 1,023 |
| 30 | 1,073,741,823 | 30 |
| 64 | 18,446,744,073,709,551,615 | 30 |

El total de movimientos se obtiene con la formula:

`2 ** discos - 1`

En los casos de 30 y 64 discos solamente se muestran los primeros 30 movimientos para evitar que el programa tenga que realizar y mostrar una cantidad demasiado grande de movimientos.

 Conclusiones

Con este programa aprendi como funciona la Torre de Hanoi y como se pueden mover los discos siguiendo un orden. Tambien aprendi a utilizar funciones en Python y a medir el tiempo que tarda el programa en ejecutarse.

Al probar diferentes cantidades de discos, pude observar que los movimientos aumentan demasiado conforme se agregan mas discos. Por ejemplo, con 5 discos son 31 movimientos, mientras que con 64 discos son mas de 18 trillones de movimientos.

Esto me permitio entender que un problema puede ser sencillo con pocos datos, pero al aumentar la cantidad de datos puede necesitar mucho mas tiempo para completarse.
