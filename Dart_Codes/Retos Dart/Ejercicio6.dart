import 'dart:math';
void main() {
  // Generar el tamaño aleatorio del arreglo entre 10 y 30
  final random = Random();
  final size = random.nextInt(21) + 10;

  // Crear el arreglo con valores aleatorios entre 0 y 10
  List<int> array = List.generate(size, (_) => random.nextInt(11));

  // Ordenar el arreglo de forma ascendente
  array.sort();

  print('Arreglo ordenado de forma ascendente:');
  print(array);

  // Mezclar el arreglo de forma aleatoria
  for (var i = 0; i < array.length; i++) {
    final randomIndex = random.nextInt(array.length);
    final temp = array[i];
    array[i] = array[randomIndex];
    array[randomIndex] = temp;
  }

  print('Arreglo mezclado de forma aleatoria:');
  print(array);
}
