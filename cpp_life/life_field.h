#pragma once

#include "matrix.h"

class LifeField {
 public:
  LifeField(int h, int w);
  void Set(int p, int q, char v);
  char Get(int p, int q) const;
  int  Height() const;
  int  Width() const;
  void Next();
 private:
  int h, w;
  Matrix field, buffer;
};
