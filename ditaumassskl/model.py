from ROOT import TLorentzVector

from rootpy.tree import TreeModel, FloatCol, IntCol, BoolCol, CharCol
from rootpy.vector import LorentzRotation, LorentzVector, Vector3, Vector2
from rootpy.extern.hep import pdg
from rootpy import log
import math



ignore_warning = log['/ROOT.TVector3.PseudoRapidity'].ignore(
    '.*transvers momentum.*')


from mass import collinearmass

class EventModel(TreeModel):
    runnumber = IntCol()
    evtnumber = IntCol()
    weight = FloatCol()
    hadhad = IntCol() # 1 or 0
    lephad = IntCol() # 1 or 0
    leplep = IntCol() # 1 or 0
    
class FourMomentum(TreeModel):
    pt = FloatCol()
    et = FloatCol()
    eta = FloatCol(default=-1111)
    phi = FloatCol(default=-1111)
    m = FloatCol()

    @classmethod
    def set(cls, this, other):
        if isinstance(other, TLorentzVector):
        this.pt = other.Pt()
        this.p = other.P()
        this.et = other.Et()
        this.e = other.E()
        this.m = other.M()
        with ignore_warning:
            this.phi = other.Phi()
            this.eta = other.Eta()

class Met(FourMomentum):
    met_et=FloatCol()
    met_etx=FloatCol()
    met_ety=FloatCol()
    met_phi=FloatCol()
    met_sumet=FloatCol()
    @classmethod
    def set(cls, this,other):
        this.met_et=other.true_met_et
        this.met_etx=other.true_met_etx
        this.met_ety=other.true_met_ety
        this.met_phi=other.true_met_phi
        this.met_sumet=other.true_met_sumet
        
    
class Tau(FourMomentum + FourMomentum.prefix('full_')):

     true_tau_0_decay_mode = 6
     true_tau_0_n_charged = 1
     true_tau_0_n_charged_pion = 0
     true_tau_0_n_neutral = 0
     true_tau_0_n_neutral_pion = 0
     
    
    @classmethod
    def set_full(cls, this, other):
        if isinstance(other, TLorentzVector):
            vect = other
        else:
            vect = other.fourvect
        this.full_pt = vect.Pt()
        this.full_p = vect.P()
        this.full_et = vect.Et()
        this.full_e = vect.E()
        this.full_m = vect.M()
        with ignore_warning:
            this.full_phi = vect.Phi()
            this.full_eta = vect.Eta()

class TrueTauBlock(TrueTau.prefix('tau1_') + TrueTau.prefix('tau2_') + TrueMet.prefix('MET_')):
    

    dR_tau1_tau2 = FloatCol()
    dEta_tau1_tau2 = FloatCol()
    dPhi_tau1_tau2 = FloatCol()    


    dPhi_tau1_tau2_MET= FloatCol()
    dPhi_tau1_MET= FloatCol()
    dPhi_tau2_MET= FloatCol()
    dPhi_min_tau_MET = FloatCol()

    vector_sum_pt_tau1_tau2= FloatCol()
    sum_pt_tau1_tau2= FloatCol()
    vector_sum_pt_tau1_tau2_met = FloatCol()
    sum_pt_tau1_tau2_met= FloatCol()

    transverse_mass_tau1_tau2 = FloatCol() 
    transverse_mass_tau1_met = FloatCol() 
    transverse_mass_tau2_met = FloatCol() 
    mass_tau1_tau2_jet1 =FloatCol(default = -9999)
    mass_vis_tau1_tau2 = FloatCol() 
    mass_collinear_tau1_tau2 = FloatCol()

    theta_tau1_tau2 = FloatCol()
    cos_theta_tau1_tau2 = FloatCol()
    
    tau_pt_ratio = FloatCol() 
    met_phi_centrality = FloatCol() 
    pt_diff_tau1_tau2 = FloatCol() 

    # tau1, tau2, met, jet1, jet2 variables
    sum_pt = FloatCol() 
    sum_pt_full = FloatCol()
    vector_sum_pt  = FloatCol() 
    vector_sum_pt_full = FloatCol()

    true_resonance_pt = FloatCol()
    resonance_pt = FloatCol()

    @classmethod 
    def set(cls, tree, tau1, tau2, jet1=None, jet2=None):


        TrueTau.set_full(tree.tau1, tau1.fourvect)
        TrueTau.set_full(tree.tau2, tau2.fourvect)

        TrueTau.set(tree.tau1, tau1.decay.fourvect_vis)
        TrueTau.set(tree.tau2, tau2.decay.fourvect_vis)


        tree.tau1.index = tau1.index
        tree.tau1.charge = tau1.charge
        tree.tau1.flavor = 'l' if tau1.decay.leptonic else 'h'
        if tree.tau1.flavor == 'l':
            tree.tau1.pdgId = pdg.mu if tau1.decay.leptonic_muon else pdg.e
        else:
            tree.tau1.nProng = tau1.decay.nprong
            tree.tau1.nPi0s = tau1.decay.nneutrals
        
        tree.tau2.index = tau2.index
        tree.tau2.charge = tau2.charge
        tree.tau2.charge = tau2.charge
        tree.tau2.flavor = 'l' if tau2.decay.leptonic else 'h'
        if tree.tau2.flavor == 'l':
            tree.tau2.pdgId = pdg.mu if tau2.decay.leptonic_muon else pdg.e
        else:
            tree.tau2.nProng = tau2.decay.nprong
            tree.tau2.nPi0s = tau2.decay.nneutrals
            

        MET = tau1.decay.fourvect_missing + tau2.decay.fourvect_missing
        TrueMet.set(tree.met, tau1.decay.fourvect_missing, tau2.decay.fourvect_missing)

        vis_tau1 = tau1.decay.fourvect_vis
        vis_tau2 = tau2.decay.fourvect_vis
        tree.dR_tau1_tau2 = vis_tau1.DeltaR(vis_tau2)
        tree.dEta_tau1_tau2 = abs(vis_tau1.Eta() - vis_tau2.Eta())
        tree.dPhi_tau1_tau2 = abs(vis_tau1.DeltaPhi(vis_tau2))
        
        vis_taus = vis_tau1 + vis_tau2

        tree.dPhi_tau1_tau2_MET = abs(vis_taus.DeltaPhi(MET))
        tree.dPhi_tau1_MET = abs(vis_tau1.DeltaPhi(MET))
        tree.dPhi_tau2_MET = abs(vis_tau2.DeltaPhi(MET))
        tree.dPhi_min_tau_MET = min(tree.dPhi_tau1_MET, tree.dPhi_tau2_MET)
        
        tree.vector_sum_pt_tau1_tau2_met = (vis_taus + MET).Pt()
        tree.sum_pt_tau1_tau2_met = vis_tau1.Pt() + vis_tau2.Pt() + MET.Pt()
        tree.vector_sum_pt_tau1_tau2 = vis_taus.Pt()
        tree.sum_pt_tau1_tau2 = vis_tau1.Pt() + vis_tau2.Pt() 
        tree.pt_diff_tau1_tau2 = math.sqrt(pow(vis_tau1.Pt() * math.cos(vis_tau1.Phi()) - vis_tau2.Pt() * math.cos(vis_tau2.Phi()), 2) +
                                          pow (vis_tau1.Pt() * math.sin(vis_tau1.Phi()) - vis_tau2.Pt() * math.sin(vis_tau2.Phi()), 2)) / tree.sum_pt_tau1_tau2

        tree.transverse_mass_tau1_tau2 = vis_taus.Mt() 
        tree.transverse_mass_tau1_met = (vis_tau1 + MET).Mt()
        tree.transverse_mass_tau2_met = (vis_tau2 + MET).Mt()
        
        tree.theta_tau1_tau2 = abs(tau1.fourvect.Angle(tau2.fourvect))
        tree.cos_theta_tau1_tau2 = math.cos(tree.theta_tau1_tau2)
      tree.tau1.collinear_momentum_fraction = x1
        tree.tau2.collinear_momentum_fraction = x2

        tree.met_phi_centrality = eventshapes.phi_centrality(
            tau1.fourvect, tau2.fourvect, Vector2(MET.X(), MET.Y()))

        if vis_tau2.Pt() != 0:
            tree.tau_pt_ratio = vis_tau1.Pt() / vis_tau2.Pt()
        else:
            tree.tau_pt_ratio = 0

        tree.sum_pt = vis_tau1.Pt() + vis_tau2.Pt() + MET.Pt()
 )
            tree.sum_pt = vis_tau1.Pt() + vis_tau2.Pt() + jet1.pt + jet2.pt + MET.Pt()
            tree.vector_sum_pt = (vis_tau1 + vis_tau2 + jet1.fourvect + jet2.fourvect + MET).Pt()




            ##########################
            # Jet and sum pt variables
            ##########################



                # determine boost of system
                # determine jet CoM frame
            beta = (jet1.fourvect + jet2.fourvect).BoostVector()
            tree.jet_beta.copy_from(beta)
            
            jet1.fourvect_boosted.copy_from(jet1.fourvect)
            jet2.fourvect_boosted.copy_from(jet2.fourvect)
            jet1.fourvect_boosted.Boost(beta * -1)
            jet2.fourvect_boosted.Boost(beta * -1)
            
   boosted tau centrality
            tau1.centrality_boosted = eventshapes.eta_centrality(
                tau1.fourvect_boosted.ssmethod 
    def set(cls, tree, jet1, jet2):
        if jet1 is not None:
            tree.jet1.index = jet1.index
            FourMomentum.set(tree.jet1, jet1)
        if jet2 is not None:
            tree.jet2.index = jet2.index
            FourMomentum.set(tree.jet2, jet2)
            
            tree.dEta_jet1_jet2 = abs(jet1.eta - jet2.eta)
            tree.eta_product_jets = jet1.eta * jet2.eta
            tree.eta_product_jets_boosted = (jet1.fourvect_boosted.Eta() * jet2.fourvect_boosted.Eta())

            tree.mass_j
