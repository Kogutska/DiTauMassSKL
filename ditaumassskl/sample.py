
## global imports
import random
import ROOT
from root_numpy import root2array
import numpy as np
import pandas as pd
import tables
import os

## local imports
from ditaumassskl.features import branches
from ditaumassskl.log import *

## root_numpy library makes it easy to read your data stored
## in a ROOT TTree. Each call to root2array will create a 2D array which contains
## one row per event, and one column representing each branch you want to use

## filters: should be a ROOT.TCut object
## apply truth-matching
selection = "(ditau_tau1_matched_isHadTau==1) && (ditau_tau0_matched_isHadTau==1)"

class Sample():

    def __init__(self, fname, ntuples_path = " ", tree_name= "NOMINAL"):
        self.ntuples_path = ntuples_path
        self.fpath = os.path.join(ntuples_path, fname)
        self.tree_name = tree_name
        
    def get_dframe(self, cuts = None):
        logger.info("Opening %s" % self.fpath)
        ## transfer TTree to NumPy array
        train_array= root2array(self.fpath,
                                branches = branches,
                                selection=cuts,
                                treename=self.tree_name)
        ## create pandas DataFrame object to manipluate data in an easy way
        df = pd.DataFrame(np.hstack((train_array.reshape(train_array.shape[0], -1))),
                          index = ["Evt%i" % i for i in range(train_array.shape[0])])
        
        return df
                          
