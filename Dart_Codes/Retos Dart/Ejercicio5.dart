import 'dart:io';

void main() {
  // Pedir al usuario una lista de números enteros separados por espacios
  print('Introduce una lista de números enteros separados por espacios:');
  String Motomomami = stdin.readLineSync()!;

  // Convertir la entrada de usuario en una lista de enteros
  //Map Devuelve un iterable y al colocalrle el .tolist() lo pasara a lista
  List<int> numeros = Motomomami.split(' ').map(int.parse).toList();

  // Calcular la suma de los números en la lista
  int suma = 0;
  for (int numero in numeros) {
    suma += numero;
  }

  // Mostrar la suma de los números
  print('La suma de los números es: $suma');
}
