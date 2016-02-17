import rootpy
import logging
log = logging.getLogger('DiTauMass')

## package-wise variables
MASSES= range(60,205, 5)
NTUPLE_PATH = "/home/warehouse/sbahrase/SAMPLES/nTuples/MC15/HTauTau/"
DEFAULT_STUDENT = "reco"
DEFAULT_TREE = "NOMINAL"

# setup the argument parser
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--test_mode', type=str, default='VBF', choices=['VBF', 'gg', 'mix', 'Z'])
parser.add_argument('--test_level', type = str , default = 'reco', choices = ['truth', 'reco'])
parser.add_argument('--train_level', type = str , default = 'truth', choices = ['truth', 'reco'])
parser.add_argument('--train_id', type = str , default = '0000',)

parser.add_argument('--channel', type = str , default = 'hh', choices = ['hh','lh', 'll'])
parser.add_argument('--train_mode', type=str, default='VBF', choices=['VBF', 'gg', 'mix', 'Z'])
#parser.add_argument('files', nargs='+', default=None)

from datetime import date
date = date.today()
date = date.strftime("%m%d%Y")

import os
import ROOT
ROOT.gROOT.SetBatch(True)

ATLAS_LABEL = os.getenv('ATLAS_LABEL', 'Internal').strip()
