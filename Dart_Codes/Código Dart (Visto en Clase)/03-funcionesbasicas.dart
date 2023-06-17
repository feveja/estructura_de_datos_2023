main() {
  var op1 = operacion(20, 10, suma);
  var op2 = operacion(20, 10, resta);
  print(op1);
  print(op2);
}

int operacion(int a, int b, Function func) {
  return func(a, b);
}

int suma(int a, int b) {
  return a + b;
}

int resta(int a, int b) {
  return a - b;
}
