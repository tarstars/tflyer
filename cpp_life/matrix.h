#pragma once

#include <vector> // bad idea, only to shorten this example.
                  // in real life needs to be placed into .cpp
                  // using PIMPL

class Matrix {
  typedef std::vector<char> storage_type;
 public:
 Matrix(int h, int w):h(h), w(w), dat(h*w) {}
  storage_type::iterator operator[](int ind) {return dat.begin() + w * ind;}
  storage_type::const_iterator operator[](int ind) const {return dat.begin() + w * ind;}
 private:
  int h, w;
  storage_type dat; // char can be template parameter of Matrix
};
  
  
