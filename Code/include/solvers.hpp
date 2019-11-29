#include <iostream>

enum Solver { EIGEN, PETSC };

std::string modelname_short(Solver m) {
    switch(m)
    {
        case EIGEN   : return "EIGEN";     break;
        case PETSC  : return "PETSC";   break;
        default    : return "No matching solver name";
    }
}