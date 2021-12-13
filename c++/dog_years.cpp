#include <iostream>

int main() {
  
  //dog age in human years
  int dog_age = 6;
  int early_years, later_years, human_years;
  
  //the first 2 years of a dog's life equate to about 21 human years
  early_years = 21; 
  
  //each following year is about 4 human years
  later_years = (dog_age - 2) * 4;

  //human years, then, is a combination of both of these
  human_years = early_years + later_years;

  std::cout << "My name is Tink!  Ruff ruff, I am " << human_years << " years old in human years.\n";

}
