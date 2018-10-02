#include "field_util.h"
#include "life_field.h"

#include <iostream>
#include <unistd.h>

int main() {
  std::string description =
    "                            \n"
    "     *                      \n"
    "      *                     \n"
    "    ***                     \n"
    "                            \n"
    "                            \n"
    "                            \n";

  LifeField current = createFromString(description);
  std::cout << current.Width() << " " << current.Height() << std::endl;

  for (int meter = 0; meter < 1000; ++meter) {
    std::cout << "\x1B[2J";
    std::cout << toString(current) << std::endl;
    usleep(50000);
    current.Next();
  }
  std::cout << toString(current) << std::endl;
  return 0;
}
