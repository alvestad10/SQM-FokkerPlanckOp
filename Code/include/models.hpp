#include <iostream>

enum Model { LM_HO,
             LM_AHO,
             HO_SK};

std::string modelname_short(Model m) {
    switch(m)
    {
        case LM_HO   : return "LM_HO";     break;
        case LM_AHO  : return "LM_AHO";   break;
        case HO_SK  : return "HO_SK";   break;
        default    : return "No matching model name";
    }
}

std::string modelname_long(Model m) {
    switch(m)
    {
        case LM_HO   : return "Large-Mass Harmonic Oscillator";     break;
        case LM_AHO  : return "Large-Mass Anharmonic oscillator";   break;
        case HO_SK  : return "Harmonic oscillator on Schwinger-Keldysh contour";   break;
        default    : return "No matching model name";
    }
}