import 'dart:io';

void main() {
  // Solicitando una cadena de texto por teclado
  print('Ingrese su nombre: ');
  String nombre = stdin.readLineSync()!;
  print('Hola, $nombre!');

  // Solicitando un número por teclado
  print('Ingrese su edad: ');
  int edad = int.parse(stdin.readLineSync()!);
  print('Su edad es $edad años.');
}
