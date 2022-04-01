/**
 * @file tree.cc
 * @author Saúl Sosa
 * @brief  Programa que crea un árbol de asteriscos
 * @version 0.1
 * @date 2022-04-01
 *
 *
 */

#include <iostream>

int main() {
  int tamano_arbol;
  int asterix = 1;
  int spaces = 1;

  std::cout << "Tamño del árbol?\n";
  std::cin >> tamano_arbol;
  for (int i = tamano_arbol; i > 0; i--) {
    //Colocar espacios  
    for (int j = 0; j < tamano_arbol - spaces; j++) {
      std::cout << " ";
    }
    //Colocar asteriscos
    for (int j = 0; j < asterix; j++) {
      std::cout << "*";
    }
    //Los asteriscos se van añadiendo de 2 en dos
    asterix += 2;
    //En cada iteración los espacios son uno menos
    spaces++;
    std::cout << std::endl;
  }
  return 0;
}