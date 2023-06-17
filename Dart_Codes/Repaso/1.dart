void main() {
  List<int> numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10];

  List<int> numerosNegativos = numeros.where((numero) => numero < 0).toList();

  print(numerosNegativos); // Imprime: [-2, -4, -6, -8, -10]
}
import 'dart:math';

void main() {
  Random random = Random();
  
  int numeroAleatorioNegativo = -random.nextInt(100); // Genera un número aleatorio negativo entre 0 y -99
  
  print(numeroAleatorioNegativo);
}

void main() {
  List<int> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  // Agregar elementos en las posiciones 8 y 7
  lista.insert(8, 11);
  lista.insert(7, 12);

  print(lista); // Imprime: [1, 2, 3, 4, 5, 6, 7, 12, 8, 11, 9, 10]

  // Quitar elementos de las posiciones 8 y 7
  lista.removeAt(8);
  lista.removeAt(7);

  print(lista); // Imprime: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

import 'dart:io';

void main() {
  List<int> lista = [];

  // Solicitar al usuario que ingrese los elementos de la lista
  for (int i = 0; i < 5; i++) {
    stdout.write('Ingrese el elemento ${i + 1}: ');
    int elemento = int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }

  print(lista); // Imprime la lista ingresada por el usuario
}
import 'dart:math';

void main() {
  List<int> lista = [5, 2, 8, 1, 9, 3, 7, 4, 6];

  // Ordenar la lista de manera descendente
  lista.sort((a, b) => b.compareTo(a));

  print('Lista ordenada de manera descendente: $lista');

  // Ordenar la lista de manera aleatoria
  Random random = Random();
  lista.shuffle(random);

  print('Lista ordenada de manera aleatoria: $lista');
}
