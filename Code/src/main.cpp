#include <iostream>
#include <fstream>
#include <assert.h>

#include "typedefs.hpp"
#include "models.hpp"
#include "Operators.hpp"
#include "../lib/eigen-git-mirror/Eigen/Dense"


/****************
*** CONSTANTS ***
*****************/
Model MODEL = LM_HO;


/*********************
*** HELP FUNCTIONS ***
**********************/

/*
Save eigenvalues to a file
*/
void save_eigenvalues(Eigen::VectorXcd ev, std::string filename) {
    std::ofstream outFile(filename);
    for (const complex_d &e : ev) {
        outFile << std::to_string(e.real()) << "," 
                << std::to_string(e.imag()) << "\n";
    }
}


int main() {

    /*
    * MODEL INDEPENDENT PARAMETERS
    */
    double x_min = -100.0;
    double x_max = 100.0;
    int N = 100;
    double a = (x_max-x_min) / (double)N;

    /*
    * MODEL INDEPENDENT PARAMETERS
    */
    /*
    complex_d sig(cos(n*M_PI/nn), sin(n*M_PI/nn));*/
    complex_d lmb(2.0,0);

    for (int n=0;n<40;n++){
        
        // Loop parameters
        complex_d sig(1.0,n);
        complex_d K = 1;
        
        /* CONSTRUCT MATRICES */
        complex_M H;
        switch(MODEL) {
            case LM_HO   : H = LM_HO_Matrix(K,sig,N,a,x_min);     break;
            case LM_AHO  : H = LM_AHO_Matrix(K,sig,lmb,N,a,x_min);   break;
            default      : assert(false);
        }

        // Compute the eigenvalue system
        Eigen::ComplexEigenSolver<Eigen::MatrixXcd> ces;
        ces.compute(H);

        // If needed, print out the eigenvalues
        //std::cout << "The eigenvalues of A are:" << std::endl << ces.eigenvalues() << std::endl;
        
        // Save eigenvalues
        /*
        *   TODO: This sould be a function to save in a systematci order
        *         i.e., save with config file or womthing where the specifics
        *         if the run is saved. For instance include x_min, x_max, a, N,
        *         sigma and D2_XX for the LM_HO case.
        */
        std::string filename = "../Data/" + modelname_short(MODEL) 
                                + "/EVal_sig_" 
                                + std::to_string((int)sig.real()) 
                                + "_i" + std::to_string((int)n);
        save_eigenvalues(ces.eigenvalues(), filename);
    }
    return 0;
}