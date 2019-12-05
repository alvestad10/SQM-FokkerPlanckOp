import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from analysis_settings import ROOT_DATA_MODEL,\
                              ROOT_FIGURES_MODEL

V = 100
N = 500
EVECNR = 0

def filename_parameters():
    fname = '_H'

    # This can be changed specific to the test
    fname += param_txt(13,25)
    fname += "_N_" + str(N)
    fname += "_on_" + str(-V) + "-" + str(V)

    return fname


def param_txt(k,n):
    """
    The sigma parameter text
    """
    return "_sig_cos("+ str(k) + "pi_" + str(n) +")_isin("+ str(k) + "pi_"+ str(n) +")"
    #return "_sig_" + str(1) + "_i" + str(0)


fname = "EVecs/Evecs"

fname += filename_parameters()

fname_periodic  = fname + '__PERIODIC'
fname_sbp = fname + '__SBP'
print(fname_periodic)
try:
    
    data_periodic = pd.read_csv(os.path.join(ROOT_DATA_MODEL,fname_periodic), header=None, sep=",")
    
    # Normalize
    data_periodic = data_periodic / data_periodic.abs().max()
    
    #data_periodic = data_periodic*(-1)
    nr_columns = len(data_periodic.columns)
    
    # Adding xaxis
    data_periodic['x'] = np.linspace(-V,V,N)
    
    # Plot
    sns.lineplot(data=data_periodic, x='x', y=EVECNR, label="PERIODIC")

except FileNotFoundError:
    print("No data from periodic")

try:
    data_sbp = pd.read_csv(os.path.join(ROOT_DATA_MODEL,fname_sbp), header=None, sep=",")

    # Normalixing
    data_sbp = data_sbp / data_sbp.abs().max()
    #data_sbp = data_sbp*(-1)
    
    nr_columns = len(data_sbp.columns)
    
    # Adding xaxis
    data_sbp['x'] = np.linspace(-V,V,N)
    
    # Plot
    #sns.lineplot(data=data_sbp, x='x', y=EVECNR+10, label="SBP")
except FileNotFoundError:
    print("No data for sbp")

plt.xlabel('x')
plt.ylabel('FP Proabability distribution')
plt.xlim([-25,25])
if True:
    fig_filename = "EVec/Evec"
    fig_filename += filename_parameters()
    fig_filename += "_EVecNr_" + str(EVECNR)
    fig_filename += "_PERIODIC"
    fig_filename += "_ZOOMED"
    #fig_filename += "_PERIODIC_VS_SBP"
    print("Saving file as: " + fig_filename)
    plt.savefig(os.path.join(ROOT_FIGURES_MODEL, fig_filename))

plt.legend()
plt.show()
