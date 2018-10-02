#include "life_field.h"

LifeField::LifeField(int h, int w): h(h), w(w), field(h, w), buffer(h, w) {}

void
LifeField::Set(int p, int q, char v) {
  if (v == 0) {
    field[p][q] = 0;
  } else {
    field[p][q] = 1;
  }
}

char
LifeField::Get(int p, int q) const {
  return field[((p%h)+h)%h][((q%w)+w)%w];
}

int
LifeField::Height() const {
  return h;
}

int
LifeField::Width() const {
  return w;
}

void
LifeField::Next() {
  // Naive implementation of rules
  for (int p = 0; p < h; ++p) {
    for (int q = 0; q < w; ++q) {
      int neighs = 0;
      for (int dp = -1; dp < 2; ++dp) {
	for (int dq = -1; dq < 2; ++dq) {
	  if ((dp != 0) || (dq != 0)) {
	    neighs += Get(p + dp, q + dq);
	  }
	}
      }
      buffer[p][q] = neighs;
    }
  }

  for (int p = 0; p < h; ++p) {
    for (int q = 0; q < w; ++q) {
      char newVal = 0;
      if (((field[p][q] == 1) && (buffer[p][q] == 2)) ||
	  (buffer[p][q] == 3)) {
	newVal = 1;
      }
      field[p][q] = newVal;
    }
  }
}
