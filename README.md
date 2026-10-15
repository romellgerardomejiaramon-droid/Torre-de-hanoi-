# Torre de Hanoi en Python

 Introduccion

Este programa fue realizado en Python para resolver el problema de la Torre de Hanoi. El programa permite probar diferentes cantidades de discos y observar cuantos movimientos se necesitan para resolverlo.

Se realizaron pruebas con **5, 10, 30 y 64 discos**, tomando en cuenta el numero de movimientos y el tiempo de ejecucion.

 Funcionamiento del programa

El programa comienza probando las cantidades de discos indicadas. Para cada cantidad, la funcion torre_hanoi() se encarga de realizar los movimientos de los discos entre las torres.

Para 5 y 10 discos, el programa muestra todos los movimientos realizados. Para 30 y 64 discos, solamente muestra los primeros 30 movimientos, ya que realizar y mostrar todos los movimientos tomaria demasiado tiempo.

El programa tambien calcula el total de movimientos que se necesitan y mide cuanto tiempo tarda en realizar la prueba. La funcion convertir_tiempo() ayuda a mostrar el tiempo en segundos, minutos, horas, dias o años.

Al final se muestran los resultados de cada prueba.

  Metodos utilizados

El programa tiene 3 metodos o funciones, y cada uno sirve para realizar una parte diferente del programa.

 1. torre_hanoi()

Esta funcion es la encargada de mover los discos de una torre a otra. Al principio puede parecer complicado saber en que orden se deben mover, pero la funcion va organizando los movimientos poco a poco hasta llegar al resultado. Para hacerlo utiliza tres torres: una de donde salen los discos, otra que sirve de apoyo y una donde deben quedar al final.

Tambien guarda los movimientos que se van realizando para despues mostrarlos en la pantalla. Cuando se utilizan 30 o 64 discos, el programa solo muestra los primeros 30 movimientos, porque mostrar todos seria demasiado tardado.

 2. convertir_tiempo()

Esta funcion sirve para que sea mas facil entender el tiempo que tarda el programa. Como el tiempo se mide primero en segundos, esta funcion lo convierte a minutos, horas, dias o anos cuando es necesario.

Asi, en lugar de ver una cantidad muy grande de segundos, podemos entender mejor cuanto tiempo podria tardar el programa en completar todos los movimientos.

 3. main()

Esta es la funcion principal, porque desde aqui se organizan las pruebas del programa. Primero se indican las cantidades de discos que se van a probar: 5, 10, 30 y 64.

Despues, el programa calcula cuantos movimientos se necesitan y utiliza la funcion torre_hanoi() para obtener los movimientos que se mostraran. Tambien mide el tiempo que tarda cada prueba y presenta los resultados en la pantalla.

Al final, muestra el tiempo total de las pruebas y permite comparar lo que sucede cuando se aumenta la cantidad de discos.

En general, al revisar estas tres funciones, entendi que cada una tiene una tarea diferente y que juntas permiten resolver el problema, mostrar los movimientos y conocer el tiempo que puede tomar.

 Resultados de las pruebas

| Cantidad de discos | Total de movimientos | Movimientos mostrados |
|---:|---:|---:|
| 5 | 31 | 31 |
| 10 | 1,023 | 1,023 |
| 30 | 1,073,741,823 | 30 |
| 64 | 18,446,744,073,709,551,615 | 30 |

El total de movimientos se obtiene con la formula:

2 ** discos - 1

En los casos de 30 y 64 discos solamente se muestran los primeros 30 movimientos para evitar que el programa tenga que realizar y mostrar una cantidad demasiado grande de movimientos.

 Conclusiones

Con este programa aprendi como funciona la Torre de Hanoi y como se pueden mover los discos siguiendo un orden. Tambien aprendi a utilizar funciones en Python y a medir el tiempo que tarda el programa en ejecutarse.

Al probar diferentes cantidades de discos, pude observar que los movimientos aumentan demasiado conforme se agregan mas discos. Por ejemplo, con 5 discos son 31 movimientos, mientras que con 64 discos son mas de 18 trillones de movimientos.

Esto me permitio entender que un problema puede ser sencillo con pocos datos, pero al aumentar la cantidad de datos puede necesitar mucho mas tiempo para completarse.
