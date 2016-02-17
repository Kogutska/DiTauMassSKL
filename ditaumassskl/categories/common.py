
from rootpy.tree import Cut
from math import pi

from .base import Category
from . import MMC_MASS
from . import Coll_MASS

## hadhad specific
TAU1_MEDIUM = Cut('ditau_tau0_jet_bdt_tight==1')
TAU2_MEDIUM = Cut('ditau_tau1_jet_bdt_medium==1')
TAU1_TIGHT = Cut('ditau_tau0_jet_bdt_medium==1')
TAU2_TIGHT = Cut('ditau_tau1_jet_bdt_tight==1')
TAU1_TRUTH_MATCH = Cut('ditau_tau0_matched_isHadTau==1')
TAU2_TRUTH_MATCH = Cut('ditau_tau1_matched_isHadTau==1')

TRUTH_MATCH = TAU1_TRUTH_MATCH & TAU2_TRUTH_MATCH
ID_MEDIUM = TAU1_MEDIUM & TAU2_MEDIUM
ID_TIGHT = TAU1_TIGHT & TAU2_TIGHT
ID_MEDIUM_TIGHT = (TAU1_MEDIUM & TAU2_TIGHT) | (TAU1_TIGHT & TAU2_MEDIUM)

## lephad specific
TAU_MEDIUM = Cut('evtsel_tau_is_Medium')
TAU_Positive = Cut('tau1_q ==1')
TAU_Negative = Cut('tau1_q ==-1')
TAU_Positive = Cut('tau2_q ==1')
TAU_Negative = Cut('tau2_q ==-1')

LEP_Positive = Cut('evtsel_lep_charge ==1')
LEP_Negative = Cut('evtsel_lep_charge ==-1')

ISO_LEP = Cut('evtsel_is_isoLep')
MT = Cut('tarnsverse_mass_tau1_tau2 < 70000')
BJET = Cut('is_tau_b_jet ==0')


TAU_MEDIUM_LEP_ISO = TAU_MEDIUM  & ISO_LEP 
OS_TAU_LEP = (TAU_Positive & LEP_Negative) | (TAU_Negative & LEP_Positive)

## NO B jet with Pt > 30 GeV

# ID cuts for control region where both taus are medium but not tight
ID_MEDIUM_NOT_TIGHT = (TAU1_MEDIUM & -TAU1_TIGHT) & (TAU2_MEDIUM & -TAU2_TIGHT)

TAU_SAME_VERTEX = Cut('tau_same_vertex')
LEAD_TAU_35 = Cut('tau_0_pt > 35')
SUBLEAD_TAU_25 = Cut('tau_1_pt > 25')

LEAD_JET_50 = Cut('jet_0_pt > 50')
SUBLEAD_JET_30 = Cut('jet_1_pt > 30')
AT_LEAST_1JET = Cut('jet_0_pt > 30')

CUTS_2J = LEAD_JET_50 & SUBLEAD_JET_30
CUTS_1J = LEAD_JET_50 & (- SUBLEAD_JET_30)
CUTS_0J = (- LEAD_JET_50)

MET = Cut('met_et > 20')
DR_TAUS = Cut('0.8 < ditau_dr < 2.4')
DETA_TAUS = Cut('ditau_deta< 1.5')
DETA_TAUS_CR = Cut('ditau_deta> 1.5')

H_Pt = 100
RESONANCE_PT = Cut('parent_pt > %i'%H_Pt)


## LEPHAD specific cuts:
TAU_PT = Cut('tau1_pt > 20.')
LEP_PT = Cut('tau2_pt > 12.')
MT = Cut('transverse_mass_tau1_tau2 < 70')

DPHI_MIN_TAUS_MET = Cut ('ditau_met_min_dphi <%0.2f'% (pi / 4))
# use .format() to set centality value
MET_CENTRALITY = 'MET_bisecting || (dPhi_min_tau_MET < {0})'

## hadhad preselection cuts
PRESELECTION = (
    LEAD_TAU_35 & SUBLEAD_TAU_25
    & ID_MEDIUM_TIGHT
    & MET
    & Cut('%s > 0' % MMC_MASS)
    & Cut('%s > 0' % Coll_MASS)
    & DR_TAUS
    & DETA_TAUS
    & DPHI_MIN_TAUS_MET
    #& TAU_SAME_VERTEX
    )


## lephad preselection cuts
PRESELECTION_LH =(
    TAU_MEDIUM_LEP_ISO 
    & TAU_PT
    & LEP_PT
    & MT
    & OS_TAU_LEP
    & Cut('%s > 0' % MMC_MASS)
    & Cut('%s > 0' % Coll_MASS)
    )

CUTS_VBF_LH = (
    CUTS_2J
    & Cut('dEta_jets > 3.')
    & Cut('mass_vis_tau1_tau2 > 40')
    )


# VBF category cuts
CUTS_VBF = (
    CUTS_2J
    & DETA_TAUS
    )

CUTS_VBF_CR = (
    CUTS_2J
    & DETA_TAUS_CR
    )

# Boosted category cuts
CUTS_BOOSTED = (
    RESONANCE_PT
    & DETA_TAUS
    )

CUTS_BOOSTED_CR = (
    RESONANCE_PT
    & DETA_TAUS_CR
    )


class Category_Loose_Preselection(Category):
    name = 'loose_preselection'
    label = '#tau_{had}#tau_{had} Loose Preselection'
    common_cuts = (
        LEAD_TAU_35 & SUBLEAD_TAU_25
        & ID_MEDIUM)
    

class Category_Preselection_NO_MET_CENTRALITY(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = PRESELECTION


class Category_Preselection(Category):
    name = 'preselection'
    label = '#tau_{had}#tau_{had} Preselection'
    common_cuts = (
        PRESELECTION
        #& Cut(MET_CENTRALITY.format(pi / 4))
        )


class Category_Preselection_LH(Category):
    name = 'preselection'
    label = '#tau_{lep}#tau_{had} Preselection'
    common_cuts = PRESELECTION_LH


class Category_Preselection_DEta_Control(Category_Preselection):
    is_control = True
    name = 'preselection_deta_control'


class Category_1J_Inclusive(Category_Preselection):
    name = '1j_inclusive'
    label = '#tau_{had}#tau_{had} Inclusive 1-Jet'
    common_cuts = Category_Preselection.common_cuts
    cuts = AT_LEAST_1JET
    norm_category = Category_Preselection
