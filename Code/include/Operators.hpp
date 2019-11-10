#include "../lib/eigen-git-mirror/Eigen/Dense"
#include "typedefs.hpp"


/* DerivativesS */


/*
* Summation by parts operator from:
* http://oddjob.utias.utoronto.ca/dwz/Miscellaneous/SBP_SAT_review.pdf
*/
complex_M D1_42(int N) {
    double h11 = 17.0/48.0; double h22 = 59.0/48.0;
    double h33 = 43.0/48.0; double h44 = 49.0/48.0;

    double q11 = -1.0/2.0;  double q12 = 59.0/96.0;
    double q13 = -1.0/12.0; double q14 = -1.0/32.0;
    double q23 = 59.0/96.0; double q24 = 0.0;
    double q34 = 59.0/96.0;
    
    // Write test: N must be larger than 8

    //setting up H and D1
    complex_M H = complex_M::Zero(N,N);
    
    // Optimize this!
    for (int i = 0; i<N; i++) {
        H(i,i) = 1.0;
    }
    H(0,0) = h11; H(N-1,N-1) = h11;
    H(1,1) = h22; H(N-2,N-2) = h22;
    H(2,2) = h33; H(N-3,N-3) = h33;
    H(3,3) = h44; H(N-4,N-4) = h44;
    
    complex_M Q = complex_M::Zero(N,N);
    Q(0,0) = q11;  Q(0,1) = q12; Q(0,2) = q13; Q(0,3) = q14;
    Q(1,0) = -q12;               Q(1,2) = q23; Q(1,3) = q24;
    Q(2,0) = -q13; Q(2,1) = -q23;              Q(2,3) = q34; Q(2,4) = -1.0/12.0;
    Q(3,0) = -q14; Q(3,1) = -q24; Q(3,2) = -q34;             Q(3,4) = 2.0/3.0; Q(3,5) = -1.0/12.0;

    //internal nodes
    for (int i = 4; i<N-5; i++) {
        Q(i,i-2) = 1.0/12.0; Q(i,i-1) = -2.0/3.0;
        Q(i,i+1) = 2.0/3.0; Q(i,i+2) = -1.0/12.0;
    }

    //bottom portion of the matrix
    for (int i = 0; i<7; i++) {
        for (int j=0; j<7; j++) {
            Q(N-i-1,N-j-1) = -Q(i,j);
        }
    }

    return H.inverse()*Q;

}

complex_M D2_42(int N) {

    complex_M D1 = D1_42(N);

    return D1*D1;    

}


/******************************************
********** FOKKER-PLANCK OPERATORS ******** 
*******************************************/


/*******************************************
***** LARGE MASS ANHARMONIC OSCILLATOR *****
********************************************

NAME: LM_AHO
ACTION: 1/2 m omega^2 x^2 + 1/4 \lambda x^4

*/

/*
    Non Derivative part of the Fokker-Planck Operator
*/
complex_d Q_LM_AHO(complex_d sig, complex_d lmb, complex_d x) {
    return -0.25*sig*sig*x*x + (3.0/2.0)*lmb*x*x - 0.5*sig*lmb*x*x*x*x - 0.25*lmb*lmb*x*x*x*x*x*x + 0.5*sig;
}

complex_M Q_LM_AHO_Matrix(complex_d sig, complex_d lmb, int N, double a, double x_min) {
    complex_M M = complex_M::Zero(N,N);
    for (int i = 0; i<N; i++) {
        M(i,i) = Q_LM_AHO(sig,lmb,x_min + a*i);
    }
    return M;
}

complex_M LM_AHO_Matrix(complex_d K, complex_d sig, complex_d lmb, int N, double a, double x_min) {
    complex_M Q = Q_LM_AHO_Matrix(sig,lmb,N,a,x_min);
    complex_M D2 =(1.0/(a*a))*D2_42(N);
    Eigen::MatrixXcd H = K*(D2 + Q);
    return H;
}


/*******************************************
***** LARGE MASS HARMONIC OSCILLATOR *****
********************************************

NAME: LM_HO
ACTION: 1/2 m omega^2 x^2 

*/

/*
    Non Derivative part of the Fokker-Planck Operator
*/
complex_M Q_LM_HO_Matrix(complex_d sig, int N, double a, double x_min) {
    complex_M M = complex_M::Zero(N,N);
    for (int i = 0; i<N; i++) {
        M(i,i) = Q_LM_AHO(sig,0.0,x_min + a*i);
    }
    return M;
}

complex_M LM_HO_Matrix(complex_d K, complex_d sig, int N, double a, double x_min) {
    complex_M Q = Q_LM_HO_Matrix(sig,N,a,x_min);
    complex_M D2 = (1.0/(a*a))*D2_42(N);
    complex_M H = K*(D2 + Q);
    return H;
}







/*******************************************
***** OTHER OUTDATED FUNCTIONS *****
********************************************

NAME: LM_HO
ACTION: 1/2 m omega^2 x^2 

*/

/*
    Non Derivative part of the Fokker-Planck Operator
*/

complex_M B_Matrix(complex_d sig, int N, double a, double x_min) {
    complex_M D1 = D1_42(N);
    complex_M B = complex_M::Zero(N,N);

    for (int i = 0; i<N; i++) {
        B(i,i) = sig*(x_min + a*i);
    }

    return B*D1;
}


complex_M E_Matrix(complex_d sig, int N, double a, double x_min) {
    complex_M E = complex_M::Zero(N,N);

    for (int i = 0; i<N; i++) {
        E(i,i) = 0.5*sig - 0.25*sig*sig*(x_min + a*i)*(x_min + a*i);
    }

    return E;
}