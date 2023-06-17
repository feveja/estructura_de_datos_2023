//Ejercicio 7
import 'dart:io';

void main() {
  print("Cantidad de elementos de la lista");
  int n = int.parse(stdin.readLineSync()!);
  List<int> lista = [];
  for (int i = 0; i < n; i++) {
    print("Ingrese el elemento");
    //el signo de exclamacion evalua si es distinto de lo que esta en la terminal,
    //es decir que si no se ingresa nada (esta en blanco), la linea no sera leida.
    int elemento = int.parse(stdin.readLineSync()!);
    if (elemento < 0) {
      print("Los valores deben ser mayores que 0");
      //regresa la iteracion
      i = i - 1;
    } else {
      lista.add(elemento);
    }
  }
  print("La lista es $lista");
  lista.sort();
  print("Orden ascendente $lista");
  // lista.reversed representa un iterable de los elementos de la lista en orden inverso,
  // Aun no es una lista, luego el metodo .toList() lo
  lista = lista.reversed.toList();
  print("Orden descendente $lista");
  int menor = lista[lista.length - 1];
  int mayor = lista[0];
  print("Elemento mayor $mayor");
  print("Elemento menor $menor");
}
