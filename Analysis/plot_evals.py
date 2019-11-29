
############################################
###             IMPORTS                 ####
############################################

###### SYSTEM IMPORTS ######
import os
import argparse

###### LIBRARY IMPORTS #######
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



################################################
###                 CONSTANTS               ####
################################################
###### SETTINGS #######
from analysis_settings import MODEL,\
                              ROOT_DATA_MODEL,\
                              ROOT_FIGURES_MODEL,\
                              COLUMNS,\
                              Test

from analysis_settings import V_MIN,\
                              V_MAX,\
                              V_MIN_MAX,\
                              N

# TODO: Find this from folder
i_min = 10
i_max = 6100
steps = 10

i_min = 0
i_max = 10
steps = 1


# CONSTANTS (Remove these)
#F = False
#H = False
#TEST = None
#K="1"
#NEVALS = 1
#LEVALS = 0
#Re_Im = "Re"

def construct_filenames():
    pass

def get_ranges_from_available_files():
    pass

def read_data():
    pass


# TESTING SPECIFIC FUNCTIONS
def sig_cos_sin_test():
    pass

def vary_sig_Im():
    pass

def vary_N():
    pass

def loop():

    # Constants that will change
    v_min_max = V_MIN_MAX
    HH=H

    for i in range(i_min,i_max,steps):
        
        if (i == 800):
            v_min_max = True
            HH = True
        
        if (i>800):
            if i%100 != 0: continue

        #if TEST == Test.VARY_N:
        #    N = i

        # Construct filename
        filename = "EVal"
        if F:
            filename += '_F'
        elif HH:
            filename += '_H'

        if TEST == Test.SIG_UNIT_CIRCLE:
            filename += "_sig_cos("+ str(i) + "pi_" + str(24) +")_isin("+ str(i) + "pi_"+ str(24) +")"
        elif TEST == Test.SIG_IM:
            filename += "_sig_" + str(1) + "_i" + str(i)
        elif TEST == Test.VARY_N:
            filename += "_sig_" + str(1) + "_i" + str(0)    
        
        if N != None:
            filename += "_N_" + str(N)

        if K != "1":
            filename += "_K_" + K
        
        if v_min_max:
            filename += "_on_" + str(V_MIN) + "-" + str(V_MAX)

        
        df = pd.read_csv(os.path.join(ROOT_DATA_MODEL,filename),
                        header=None,
                        names=COLUMNS).sort_values(by=['Re'], ascending = False)\
                                    .reset_index(drop=True)[LEVAL:LEVAL + NEVALS]\
                                    .reset_index()

        if TEST == Test.SIG_UNIT_CIRCLE:
            df['N'] = i/(48)
        elif TEST in (Test.SIG_IM, Test.VARY_N):
            df['N'] = N

        if (i==i_min):
            all_ev = df
        else:
            all_ev = pd.concat([all_ev,df])

    all_ev.Re = all_ev.Re*(-1)
    all_ev.Im = all_ev.Im*(-1)

    if TEST == Test.SIG_UNIT_CIRCLE:
        sns.lineplot(data=all_ev, x="N", y="Re", hue="index")
        plt.title("Vary sigma on unit circle")
    elif TEST == Test.SIG_IM:
        sns.scatterplot(data=all_ev, x="Re", y="Im", hue="index")
        plt.title("Varying Complex part of sigma")
    elif TEST == Test.VARY_N:
        if NEVALS == 1:
            sns.lineplot(data=all_ev, x="N", y="Re")
            plt.title("Lowest eigenvalue for given N")
        else:
            sns.lineplot(data=all_ev, x="N", y="Re", hue="index")
            plt.title("The eigenvalues for varying N")
            plt.ylim([-0.01,40])


    plot_filename = "EVal"
    if F:
        plot_filename += '_F'
    elif H:
        plot_filename += '_H'

    if TEST == Test.VARY_N:
        plot_filename += "_" + Re_Im

    if vary_N: 
        plot_filename += "_EvalNr_" + str(NEVALS) + "-" + str(LEVAL + NEVALS-1)

    if TEST == Test.SIG_UNIT_CIRCLE:
        plot_filename += "_sig_cos_isin_n_" + str(48)
    elif vary_sig_Im:
        plot_filename += "_sig_" + str(1) + "_i" + str(0) + "-" + str(20)
    elif TEST == Test.VARY_N:
        plot_filename += "_sig_" + str(1) + "_i" + str(0)

    if TEST == Test.SIG_UNIT_CIRCLE or vary_sig_Im:
        plot_filename += "_NEvals_" + str(NEVALS)
        plot_filename += "_N_" + str(N)
    elif TEST == Test.VARY_N:
        plot_filename += "_N_" + str(i_min) + "-" + str(i_max)

    plot_filename += "_K_" + K

    plot_filename += "_on_"+ str(V_MIN) +'-'+ str(V_MAX)

    #plt.ylim([-0.01,40])

    if SAVE:
        #plt.savefig(os.path.join(ROOT_FIGURES, 'EVal_sigma_1_i0-20_NEvals_8_on_-100_100'))
        plt.savefig(os.path.join(ROOT_FIGURES_MODEL, plot_filename))

    if SHOW:
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Tests:
    parser.add_argument("-vary_N",
                        help="plot the change in the numbers of discretized points N",
                        action="store_true")
    parser.add_argument("-vary_sig_Im",
                        help="plot the change in the imagenary part of the sigma parameter",
                        action="store_true")
    parser.add_argument("-sig_cos_sin",
                        help="plot the change in sigma over complex unit circle",
                        action="store_true")


    parser.add_argument("-nevals",
                        help="Number of eigenvalues to show in plot",
                        type=int,
                        default=1)
    parser.add_argument("-leval",
                        help="The lowest eigenvalue to show",
                        type=int,
                        default=0)
    parser.add_argument("--kernel", "-K",
                        help="What kernel to use (see convention on datafiles)",
                        default="1")
    parser.add_argument("-F", "--F",
                        help="Eigenvalues from Fokker-Planck operator",
                        action="store_true")
    parser.add_argument("-H", "--H",
                        help="Eigenvalues from MODIFIED Fokker-Planck operator",
                        action="store_true")
    parser.add_argument("--real","-Re",
                        help="Plot real axis",
                        action="store_true",)
    parser.add_argument("--imag","-Im",
                        help="Plot imaginary axis",
                        action="store_true")
    parser.add_argument("--noN","-noN",
                        help="If N is not specified in filename",
                        action="store_true",
                        default=False)

    parser.add_argument("-save",
                        help="Plot the figure",
                        action="store_true",
                        default=False)
    parser.add_argument("-show",
                        help="Show the figure",
                        action="store_true",
                        default=False)

    
    
                    
    args = parser.parse_args()

    # Figure specifics
    SAVE = args.save
    SHOW = args.show

    # Eigenvalues parameters
    NEVALS = args.nevals
    LEVAL = args.leval

    if args.noN:
        N=None

    # Other parameters
    K=args.kernel
    if args.F and not args.H:
        F=True
        H=False
    elif args.H and not args.F:
        F=False
        H=True
    else:
        F=False
        H=False
        #assert False, "Specify either F or H"

    if args.real and not args.imag:
        Re_Im = "Re"
    elif args.imag and not args.real:
        Re_Im = "Im"
    else:
        # Check if the test is relevant for this parameters
        assert not args.vary_N, "Must specify if the real or imagenary eigenvalues should be plotted"

    # Select which type of testing
    if args.sig_cos_sin:
        TEST = Test.SIG_UNIT_CIRCLE
    elif args.vary_sig_Im:
        TEST = Test.SIG_IM
    elif args.vary_N:
        TEST = Test.VARY_N
    else:
        assert False, "Must specify test, see test enum in analysis_settings.py"
    
    loop()