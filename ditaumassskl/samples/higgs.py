import numpy as np
import pandas as pd
import tables
import os
import ROOT
from root_numpy import root2array
from rootpy.tree import Cut
from rootpy.io import root_open
from rootpy.plotting import Hist
from rootpy import asrootpy

from .sample import Sample
from .. import NTUPLE_PATH, DEFAULT_STUDENT
from .. import log; log = log[__name__]

class Signal(Sample):
    pass

class Higgs(Signal):
    MASSES = range(60, 205, 5)
    MODES = ['gg', 'vbf', 'Z']
    LEVELS = ['truth', 'reco']
    def __init__(self, e_com=13,
                 ntuple_path='',
                 mode=None, modes=None,
                 mass=None, masses=None,
                 level = None, levels = None,
                 channel=None,
                 label=None,
                 **kwargs):
        """
        Parameters
        ----------
        * e_com: LHC center-of-mass energy (13 or 8)
        * mass: Mass of the Higgs boson
        * mode: production mode (vbf/gg)
        """
        self.ntuple_path=ntuple_path
        self.mode=mode
        self.masses=masses
        self.level=level
        self.channel=channel
        if levels is None:
            if level is not None:
                assert level in Higgs.LEVELS
                levels = [level]
            else:
                levels = Higgs.LEVELS

        else:
            assert len(levels) > 0
            for level in levels:
                assert level in Higgs.LEVELS
            assert len(set(levels)) == len(levels)


        if masses is None:
            if mass is not None:
                assert mass in Higgs.MASSES
                masses = [mass]
            else:
                # default to 125
                masses = [125]
        else:
            assert len(masses) > 0
            for mass in masses:
                assert mass in Higgs.MASSES
            assert len(set(masses)) == len(masses)

        if modes is None:
            if mode is not None:
                assert mode in Higgs.MODES
                modes = [mode]
            else:
                # default to all modes
                modes = Higgs.MODES
        else:
            assert len(modes) > 0
            for mode in modes:
                assert mode in Higgs.MODES
            assert len(set(modes)) == len(modes)
            
        name = 'Higgs'
        str_level=''
        if len(levels) == 1:
            str_level = levels[0]
            name += '_%s' % str_level

        
        str_mode = ''
        if len(modes) == 1:
            str_mode = modes[0]
            name += '_%s' % str_mode

        str_mass = ''
        if len(masses) == 1:
            str_mass = '%d' % masses[0]
            name += '_%s' % str_mass

        if label is None:
            label = '%s-%s#font[52]{H}(%s)#rightarrow#tau#tau' % (
                str_level, str_mode, str_mass)

        super(Higgs, self).__init__(ntuple_path=ntuple_path,
                                    name=name, label=label, **kwargs)
        self._sub_samples = []
        self._scales      = []
        self._files       = [] 
        for level in levels:
            for mode in modes:
                for mass in masses:                    
                    self._sub_samples.append(Signal(
                            student='%s_%s_%s_' % (level, mode, mass),
                            level = level,
                            name='%s_Higgs_%s_%s' % (level, mode, mass), 
                            label='%s_Higgs_%s_%s' % (level, mode, mass)))
                    # Add all sample with a scale of 1
                    self._scales.append(1)
                    fname='%s_%s_%s_%s.root'%(level,mode,mass,self.suffix)
                    self._files.append(os.path.join(self.ntuple_path,fname))
    @property
    def components(self):
        return self._sub_samples
    @property
    def files(self):
        return self._files
    @property
    def scales(self):
        return self._scales
    
    @property
    def events(self):
        events={}
        for f in self.files:
            inf=ROOT.TFile.Open(f, "READ")
            tree= inf.Get(self.tree_name)
            entries=tree.GetEntries()
            events[f]=entries
        return events

    def get_dframe(self,cuts = None, nevents=None,branches= []):
        log.info("Transferring roots to numpy arrays")
        assert isinstance (branches,list)
        dfs = []
        for f in self.files:
            log.debug('Opening %s'%f)
            array = root2array(f,
                               branches=branches,
                               selection=cuts,
                               treename=self.tree_name)
            df = pd.DataFrame(array.flatten(),#np.hstack((array.reshape(array.shape[0], -1))),
                              index = ["Evt%i" % i for i in range(array.shape[0])])
            if nevents is not None:
                df = df.sample(n=nevents, random_state=1, replace=True)
            dfs.append(df)
        dframe = pd.concat(dfs)
        
        return dframe

    def set_scales(self, scales):
        """
        """
        if isinstance(scales, (float, int)):
            for i in xrange(self._sub_samples):
                self._scales.append(scales)
        else:
            if len(scales) != len(self._sub_samples):
                log.error('Passed list should be of size {0}'.format(len(self._sub_samples)))
                raise RuntimeError('Wrong lenght !')
            else:
                for scale in scales:
                    self._scales.append(scale)
        
        log.info('Set samples scales: {0}'.format(self._scales))
 
    def draw_helper(self, *args, **kwargs):
        hist_array = []
        for s in self._sub_samples:
            h = s.fill_hists(*args)
            
            hist_array.append(h)

        if len(self._scales) != len(hist_array):
            log.error('The scales are not set properly')
            raise RuntimeError('scales need to be set before calling draw_helper')
        hsum = hist_array[0].Clone()
        hsum.reset()
        hsum.title = self.label
        for h, scale in zip(hist_array, self._scales):
            hsum += scale * h
        return hsum

        # draw sample distribution curve
    def plot_event_dist (self):
        mass_dist_plot = ROOT.TGraph(len(self._files))
        canvas = ROOT.TCanvas()
        canvas.SetFillStyle(18)
        i = 0
        for f, evts in self.events.items():
            log.debug('Opening %s'%f)
            d,fname = os.path.split(f)
            fn = fname.split('_')
            mass=int(fn[2])
            mass_dist_plot.SetPoint (i, mass , evts/1000.)
            i += 1

        mass_dist_plot.Draw("AP")
        mass_dist_plot.GetXaxis().SetTitle("Mass GeV (%s ) " % self.mode)
        mass_dist_plot.GetYaxis().SetTitle("#events(k)")
        mass_dist_plot.GetXaxis().SetLimits(40, 220)
        mass_dist_plot.GetYaxis().SetLimits(0, 40)

        mass_dist_plot.SetMarkerColor(2)
        mass_dist_plot.SetLineColor(4)
        mass_dist_plot.SetLineWidth(2)
        mass_dist_plot.SetMarkerStyle(20)

        canvas.SaveAs("./plots/input_samples_distribution_%s_%s.png"%( 
                self.mode, self.channel))
        canvas.Clear()

