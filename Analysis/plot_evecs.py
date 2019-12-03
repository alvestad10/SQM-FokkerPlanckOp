import os

import matplotlib.pyplot as plt
import pandas as pd

from analysis_settings import ROOT_DATA_MODEL

def param_txt(k,n):
    """
    The sigma parameter text
    """
    return "_sig_cos("+ str(k) + "pi_" + str(n) +")_isin("+ str(k) + "pi_"+ str(n) +")"
    #return "_sig_" + str(1) + "_i" + str(5)

filename = "EVecs/Evecs"
filename = filename + '_H'

# This can be changed specific to the test
filename += param_txt(8,25)
filename += "_N_" + str(200)
filename += "_on_" + str(-20) + "-" + str(20)


filename_periodic  = filename + '__PERIODIC'
filename_sbp = filename + '__SBP'

try:
    data_periodic = pd.read_csv(os.path.join(ROOT_DATA_MODEL,filename_periodic), header=None, sep=",")
    #data_periodic = data_periodic*(-1)
    nr_columns = len(data_periodic.columns)
    data_periodic[5].plot(label="PERIODIC")
except:
    print("No data from periodic")
try:
    data_sbp = pd.read_csv(os.path.join(ROOT_DATA_MODEL,filename_sbp), header=None, sep=",")
    #data_sbp = data_sbp*(-1)
    nr_columns = len(data_sbp.columns)
    data_sbp[8].plot(label="SBP")
except:
    print("No data for sbp")

plt.legend()
plt.show()
