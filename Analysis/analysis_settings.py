"""
 Defining all constants related to analysing the results
 from the Fokker-Planck operator simulations in Code
"""
import os
import socket

#-----------------------------------------#
#----------- MODEL to be used ------------#
MODEL = 'LM_AHO' 
#-----------------------------------------#
#-----------------------------------------#



#-----------------------------------------#
#              PATHS                      #
#-----------------------------------------#

# GET HOSTNAME FOR THIS COMPUTER
HOSTNAME = socket.gethostname()
if HOSTNAME == "D12691":
    ROOT_DIR = "/home/daniel/Developer/Stochastic/SQM-FokkerPlanckOp"

# DATA DIRECTORY
ROOT_DATA = os.path.join(ROOT_DIR,'Data')
ROOT_DATA_MODEL = os.path.join(ROOT_DATA,MODEL)

# FIGURE DIRECTORY
ROOT_FIGURES = os.path.join(ROOT_DIR,'Figures')
ROOT_FIGURES_MODEL = os.path.join(ROOT_FIGURES, MODEL)


#-----------------------------------------#
#           TESTS                         #
#-----------------------------------------#
from enum import Enum, unique

@unique
class Test(Enum):
    SIG_UNIT_CIRCLE = 1
    SIG_IM = 2
    VARY_N = 3

    def describe(self):
        return self.name, self.value
    
    def __str__(self):
        return 'my custom str! {0}'.format(self.value)
        





#-----------------------------------------#
#           DATA PARAMETERS               #
#-----------------------------------------#
COLUMNS = ["Re","Im"]

# Lattice parameters
N = 250
V_MIN = -100
V_MAX = 100
V_MIN_MAX = False


#--------------------------------------------------#
#              PLOT PARAMETERS                     #
#--------------------------------------------------#
LINESTYLES = ("solid", "dashed")

BLACK = 'black'
GREEN = '#20A387'
YELLOW = '#FDE725'
PURPLE = '#440154'
BLUE = '#39568C'

COLORS = [GREEN,
          PURPLE,
          BLUE,
          YELLOW,
          BLACK]




