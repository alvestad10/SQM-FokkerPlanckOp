import os

import matplotlib.pyplot as plt
import pandas as pd

from analysis_settings import MODEL,\
                              ROOT_DATA_MODEL,\
                              ROOT_FIGURES_MODEL,\
                              COLUMNS,\

from analysis_settings import V_MIN,\
                              V_MAX,\
                              V_MIN_MAX,\
                              N

###########################################
#####
#       PARENT TESTS CLASS            
#####
###########################################


class Test_parent:
    """
    All functions and data related to the specific test is
    stored in this class. Look into one of the child classes
    to finc specific usage
    """
    def __init__(self,NN,KK,h,f,periodic,v_min_max):
        self.N = NN # Number of points in x direction
        self.K = KK # The kernel
        
        self.H = h # If the modified Fokker-Planck operator should be used
        self.F = f # If the Fokker-Planck should be used
        
        self.PERIODIC = periodic # Periodic boundary condition
        self.V_MIN_MAX = v_min_max # Add min and max in colume when searching for filename

        self.filenames = [] # TO BE USED LATER

    def construct_filename(self):
        """
        Construct the filename for the specifi set of eigenvalues
        """

        filename = "EVal"
        if self.F:
            filename += '_F'
        elif self.H:
            filename = filename + '_H'

        # This can be changed specific to the test
        filename += self.param_txt()

        # This should be removed when all eigenvalues files contain N
        if self.N != None:
            filename += "_N_" + str(self.N)

        # Checking if the kernel is added to data filname
        if self.K != "1":
            filename += "_K_" + K

        if self.V_MIN_MAX:
            filename += "_on_" + str(V_MIN) + "-" + str(V_MAX)
        
        if self.PERIODIC:
            filename += self.periodic()

        self.filename = filename

    def periodic(self):
        return "__PERIODIC"

    def param_txt(self):
        return ""

    def read_file(self):
        """
        Reading the file corresponding to the filname
        MOST run get filename first
        """
        self.data = pd.read_csv(os.path.join(ROOT_DATA_MODEL,self.filename),
                             header=None,
                             names=COLUMNS).sort_values(by=[Re_Im], ascending = False)\
                                           .reset_index(drop=True)[LEVAL:LEVAL + NEVALS]\
                                           .reset_index()


    def add_to_all_ev(self):
        """
        Add data to all_ev, which contains all the relevant eigenvalues
        """
        # Creating the all_ev variabel if it do not exist
        try:
            self.all_ev = pd.concat([self.all_ev,self.data])
        except:
            self.all_ev = self.data


    def convert_eigen_sgn(self):
        """
        Conver to positive sign eigenvalues
        """
        self.all_ev.Re = self.all_ev.Re*(-1)
        self.all_ev.Im = self.all_ev.Im*(-1)

    def plot(self):
        print("Plot is not implemented")
    
    def save(self):
        print("Save is not implemented")



###########################################
#####
#       VARY N            
#####
###########################################


class Test_vary_N(Test_parent):
    """
    This test is for varying the N (number of poits in x direction).

    @input
    KK: Kernel used
    h: If modified FP used
    f: If FP used
    R: Real value of sigma
    I: Imaginary value of sigma
    B: Boundary condition (SBP, PERIODIC)
    v_min_max: if V_min_max is used

    """
    def __init__(self,KK, h,f,periodic, R, I, B, v_min_max):
        Test_parent.__init__(self,0,KK,h,f,periodic,v_min_max)
        self.R = R
        self.I = I
        self.B = B

    def loop(self, i_min, i_max, i_step):
        for i in range(i_min, i_max, i_step):
            
            # Old vary_N files do not include H or V_min_max
            if (i==800):
                self.H = True
                self.V_MIN_MAX = True

            # Setting N for this loop
            self.N = i

            self.construct_filename()
            # Testing in case the file does not exist
            try:
                self.read_file()
            except:
                continue
            # Adding N and B to the dataframe
            self.add_to_data()
            self.add_to_all_ev()

        self.convert_eigen_sgn()

    def periodic(self):
        return "__" + self.B

    def param_txt(self):
        """
        The sigma parameter text
        """
        return "_sig_" + str(self.R) + "_i" + str(self.I)


    def add_to_data(self):
        """
        Adding N and B to the data dataframe
        """
        self.data['N'] = self.N
        self.data['B'] = self.B

    
    def merge(self, test2):
        """
        Merging to tests to be able to plot them side by side
        """
        self.all_ev = pd.concat([self.all_ev,test2.all_ev])
        self.all_ev['I+B'] = self.all_ev['index'].map(str) + "_" +self.all_ev.B
    

    def plot(self):
        """
        Plotting the all_ev eigenvalues
        (must run plt.show() after this) 
        """
        if NEVALS == 1:
            sns.lineplot(data=self.all_ev, x="N", y="Re", hue="B")
            plt.title("Lowest eigenvalue for given N")
            if LEVAL > 0:
                plt.ylim([-0.01,40])
            plt.legend()
        else:
            sns.lineplot(data=self.all_ev, x="N", y="Re", hue="I+B")
            plt.title("The eigenvalues for varying N")
            plt.ylim([-0.01,40])
            plt.legend()



###########################################
#####
#       Vary sigma IM            
#####
###########################################


class Test_sig_im(Test_parent):
    """
    This test is for varying the imagenary part of sigma parameter in the potential.

    @input
    NN: Number of points in x direction
    KK: Kernel used
    h: If modified FP used
    f: If FP used
    R: Real value of sigma
    I: Imaginary value of sigma
    B: Boundary condition (SBP, PERIODIC)
    v_min_max: if V_min_max is used

    """
    def __init__(self,NN,KK, h,f,periodic, R, I, v_min_max):
        Test_parent.__init__(self,NN,KK,h,f,periodic,v_min_max)
        self.update_R_I(R,I)

    def update_R_I(self, R, I):
        self.R = R
        self.I = I

    def param_txt(self):
        return "_sig_" + str(self.R) + "_i" + str(self.I)
    
    def add_to_data(self):
        self.data['N'] = self.N

    def plot(self):
        sns.scatterplot(data=self.all_ev, x="Re", y="Im", hue="index")
        plt.title("Varying Complex part of sigma")



###########################################
#####
#       VARY SIG ON UNIT CIRCLE           
#####
###########################################

class Test_sig_unit_circle(Test_parent):
    
    def init_new(self, k, n):
        self.k = k
        self.n = n

    def param_txt(self):
        return "_sig_cos("+ str(self.k) + "pi_" + str(self.n) +")_isin("+ str(self.k) + "pi_"+ str(self.n) +")"

    def add_to_data(self):
        self.data['N'] = self.k/(48)
    
    def plot(self):
        sns.lineplot(data=self.all_ev, x="N", y="Re", hue="index")
        plt.title("Vary sigma on unit circle")