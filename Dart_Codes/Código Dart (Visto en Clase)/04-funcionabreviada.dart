main() {
  var op1 = operacion(10, 20, suma);
  var op2 = operacion(10, 20, resta);
  print(op1);
  print(op2);
}

int operacion(int a, int b, Function func) => func(a, b);
int suma(int a, int b) => a + b;
int resta(int a, int b) => a - b;
