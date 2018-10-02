#pragma once

#include <string>

class LifeField;

LifeField createFromString(const std::string& s);
std::string toString(const LifeField& lf);
