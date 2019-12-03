#include "typedefs.hpp"

/* TEST ENUM */
enum Test { SIG_UNIT_CIRCLE, VARY_N };

std::string param_filename_txt(Test TEST, complex_d sig, int n, int n_max) {
    switch(TEST)
    {
        case SIG_UNIT_CIRCLE:
            return "_sig_cos("+ std::to_string(n) +"pi_"+ std::to_string(n_max/2) +")"
                                + "_i" + "sin("+ std::to_string(n) +"pi_"+ std::to_string(n_max/2) +")";
            break;
        case VARY_N:
            return "_sig_" + std::to_string((int)sig.real()) 
                    + "_i" + std::to_string((int)sig.imag());
            break;
        default : return "No matching operator name";
    }
}
