import rootpy
import logging

#__all__=['parser']
log = logging.getLogger('DiTauMass')
log.setLevel(logging.INFO)
MMC_VERSION = 'mlm'
MMC_MASS = 'ditau_mmc_%s_m' % MMC_VERSION
MMC_PT = 'tau_tau_mmc_%s_pt' % MMC_VERSION

## package-wise variables
MASSES= range(60,205, 5)
NTUPLE_PATH='/home/sbahrase/WorkDesk/SAMPLES/nTUPLEs/hh_skim_brt/v1/train_brt'
DEFAULT_STUDENT = "reco"
DEFAULT_TREE = "NOMINAL"
# setup the argument parser
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-tem','--test_mode',  type=str,default='gg',choices=['gg', 'vbf', 'Z'])
parser.add_argument('-tel','--test_level', type=str,default = 'reco', choices = ['truth', 'reco'])
parser.add_argument('-tl','--train_level', type=str,default = 'reco', choices = ['truth', 'reco'])
parser.add_argument('-id','--train_id',    type=str,default = '0000',)
parser.add_argument('-c','--channel',      type=str,default = 'hh', choices = ['hh','lh', 'll'])
parser.add_argument('-tc','--train_channel',type=str,default = 'hh', choices = ['hh','lh', 'll'])
parser.add_argument('-tm','--train_mode',nargs='+',default='gg',)#choices=['gg', 'vbf', 'Z'])
parser.add_argument('-mreg', '--meta_reg', type=str,default='grb', 
                    choices=['ada','bag', 'ext','grb','rf'])
parser.add_argument('-breg', "--base_reg", type=str,default='dt', choices=['dt', 'ext'])

# regressors list
base_regs={}
base_regs['dt']='DecisionTreeRegressor'
base_regs['ext']='ExtraTreeRegressor'
meta_regs={}
meta_regs['ada']='AdaBoostRegressor'
meta_regs['bag']='BaggingRegressor'
meta_regs['ext']='ExtraTreesRegressor'
meta_regs['grb']='GradientBoostingRegressor'
meta_regs['rf']='RandomForestRegressor'


from datetime import date
date = date.today()
date = date.strftime("%m%d%Y")

import os
import ROOT
ROOT.gROOT.SetBatch(True)
ATLAS_LABEL = os.getenv('ATLAS_LABEL', 'Internal').strip()

from sklearn.preprocessing import StandardScaler
##--------------------------------------------------------------
## scale data
def scale_data(data_matrix):
    """
    ## Multi-layer Perceptron is sensitive to feature scaling, so it is
    ## highly recommended to scale your data. For example, scale each
    ## attribute on the input vector X to [0, 1] or [-1, +1], or
    ## standardize it to have mean 0 and variance 1. Note that you must
    ## apply the same scaling to the test set for meaningful results.
    """
    scaler = StandardScaler()  
    # Don't cheat - fit only on training data
    scaler.fit(data_matrix)  
    X_train = scaler.transform(data_matrix)  
    
    return X_train


