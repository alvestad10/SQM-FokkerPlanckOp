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
Model MODEL = LM_AHO;


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
    int N = 500;
    double a = (x_max-x_min) / (double)N;
    int n_min = 0;
    int n_max = 48;
    //double a = (x_max-x_min) / (double)N;
    /*
    * MODEL INDEPENDENT PARAMETERS
    */
    /*
    complex_d sig(cos(n*M_PI/nn), sin(n*M_PI/nn));*/
    complex_d lmb(2.0,0);

    for (int n=n_min;n<n_max;n++){
        // Loop parameters
        //complex_d sig(1.0,0.0);
        complex_d sig(cos(n*M_PI/(n_max/2.0)), sin(n*M_PI/(n_max/2.0)));
        complex_d K = 1;//std::conj(sig);
        

        /* CONSTRUCT MATRICES */
        complex_M H;
        switch(MODEL) {
            case LM_HO   : H = F_LM_HO_Matrix(K,sig,N,a,x_min);     break;
            case LM_AHO  : H = F_LM_AHO_Matrix(K,sig,lmb,N,a,x_min);   break;
            default      : assert(false);
        }

        // If needed, print out the Fokker-Planck operator
        //std::cout << "H:" << std::endl << H << std::endl;

        // Compute the eigenvalue system
        Eigen::ComplexEigenSolver<complex_M> ces;
        ces.compute(H);

        // If needed, print out the eigenvalues
        //std::cout << "The eigenvalues of H are:" << std::endl << ces.eigenvalues() << std::endl;
        
        // Save eigenvalues
        /*
        *   TODO: This sould be a function to save in a systematci order
        *         i.e., save with config file or womthing where the specifics
        *         if the run is saved. For instance include x_min, x_max, a, N,
        *         sigma and D2_XX for the LM_HO case.
        */
        std::string filename = "../Data/" + modelname_short(MODEL) 
                                + "/EVal_F_sig_" 
                                + "cos("+ std::to_string(n) +"pi_"+ std::to_string(n_max/2) +")" //std::to_string((int)sig.real()) 
                                + "_i" + "sin("+ std::to_string(n) +"pi_"+ std::to_string(n_max/2) +")" //std::to_string((int)sig.imag())
                                + "_N_" + std::to_string((int)N);
                                //+ "_K_sig*";
        
        
        std::cout << filename << std::endl;
        save_eigenvalues(ces.eigenvalues(), filename);
    }
    return 0;
}