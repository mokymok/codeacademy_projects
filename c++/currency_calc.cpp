#include <iostream>

int main() {
  
  double pesos, reais, soles;

  double dollars;
  
  std::cout << "Enter the number of Colombian Pesos: ";
  std::cin >> pesos;

  std::cout << "Enter the number of Brazilian Reais: ";
  std::cin >> reais;

  std::cout << "Enter the number of Peruvian Soles: ";
  std::cin >> soles;

  //rates as of 12.13.21
  double conv_rate_peso = 0.00026;
  double conv_rate_reais = 0.18;
  double conv_rate_soles = 0.25;

  dollars = (conv_rate_peso * pesos) + (conv_rate_reais * reais) + (conv_rate_soles * soles);

  std::cout << "US Dollars = $" << dollars << "\n";
}
