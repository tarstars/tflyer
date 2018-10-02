#include "field_util.h"

#include "life_field.h"

LifeField createFromString(const std::string& s) {
  int w;
  int n = s.size();
  for (w = 0; w < n && s[w] != '\n'; ++w) {
  }
  int h = n / w;

  LifeField field(h, w);
  for (int p = 0; p < h; ++p) {
    for (int q = 0; q < w; ++q) {
      int val = 0;
      if (s[p * (w + 1) + q] == '*') {
	val = 1;
      }
      field.Set(p, q, val);
    }
  }
  return field;
}

std::string toString(const LifeField& lf) {
  int h = lf.Height();
  int w = lf.Width();

  std::string s(h * (w + 1), ' ');
  int ind = 0;
  for (int p = 0; p < h; ++p) {
    for (int q = 0; q < w; ++q) {
      if (lf.Get(p, q)) {
	s[ind] = '*';
      }
      ++ind;
    }
    s[ind] = '\n';
    ++ind;
  }
  return s;
}
