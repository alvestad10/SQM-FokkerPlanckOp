#include <iostream>

enum Model { LM_HO,
             LM_AHO};

std::string modelname_short(Model m) {
    switch(m)
    {
        case LM_HO   : return "LM_HO";     break;
        case LM_AHO  : return "LM_AHO";   break;
        default    : return "No matching model name";
    }
}

std::string modelname_long(Model m) {
    switch(m)
    {
        case LM_HO   : return "Large-Mass Harmonic Oscillator";     break;
        case LM_AHO  : return "Large-Mass Anharmonic oscillator";   break;
        default    : return "No matching model name";
    }
}