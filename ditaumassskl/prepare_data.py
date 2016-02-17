from root_numpy import root2array
import numpy as np
import pandas as pd
from . import log

class Sample():
    def __init__(self,
                 ntuples_path='./ntuples/',
                 tree_name = 'NOMINAL',
                 masses= None,
                 level= 'reco',
                 mode = 'gg',
                 suffix = 'test'):
        
        self.npath= ntuples_path
        self.tree_name = tree_name
        self.masses = masses
        self.mode = mode
        self.level = level
        self.suffix = suffix

    def get_files (self):
        fpaths =[]
        if self.mode in ['vbf', 'gg']:
            assert isinstance(self.masses, list)
            for m in self.masses:
                fname = self.level + '_' + self.mode +'_'+ str(m) + '_'+ self.suffix + '.root'
                fpath = self.npath + fname
                fpaths.append(fpath)
    
        if self.mode == "mix":
            for self.mode in ['vbf', 'gg']:
                for m in self.masses:
                    fname = self.level + '_' + self.mode +'_'+ str(m) + '_'+ self.suffix + '.root'
                    fpath = self.npath + fname
                    fpaths.append(fpath)
        return fpaths
    
    def get_dframe(self, fpaths, branches=None, cuts = None):
        train_df = []
        for s in fpaths:
            log.info("Opening %s" % s)
        ## transfer TTree to NumPy array
            train_array= root2array(s,
                                    branches = branches,
                                    selection=cuts,
                                    treename=self.tree_name)

        ## create pandas DataFrame object to manipluate data in an easy way
            df = pd.DataFrame(np.hstack((train_array.reshape(train_array.shape[0], -1))),
                              index = ["Evt%i" % i for i in range(train_array.shape[0])])
            train_df.append(df)
        data = pd.concat(train_df, ignore_index=True)
        return data

    ## draw sample distribution curve
    def draw_sample_dist (self, fpaths):
        dists= []
        for s in fpaths:
            f = ROOT.TFile(s)
            tree = f.Get(self.tree_name)
            dists.append(0.001*tree.GetEntries())
            
        mass_dists = ROOT.TGraph(len(dists))
        canvas = ROOT.TCanvas()
        canvas.SetFillStyle(18)
        i = 0
        for m , n in zip(self.masses, dists):
            mass_dists.SetPoint (i, m , n)
            i += 1
            mass_dists.Draw("ALP")
            mass_dists.GetXaxis().SetTitle("Mass (%s_%s ) " % (level,self.mode))
            mass_dists.GetYaxis().SetTitle("# of events(/k)")
            mass_dists.GetXaxis().SetLimits(40, 220)
            mass_dists.GetYaxis().SetLimits(0, 20)
                
            mass_dists.SetMarkerColor(2)
            mass_dists.SetLineColor(4)
            mass_dists.SetLineWidth(3)
            mass_dists.SetMarkerStyle(20)
            canvas.SaveAs("./plots/input_samples_distribution_%s_%s.png"% (level,self.mode))
            canvas.Clear()
