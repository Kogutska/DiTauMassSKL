from .. import MMC_MASS


# Neural Net feats
HH_FEATURES_NN = [
    "ditau_tau0_pt",
    "ditau_tau0_eta",
    "ditau_tau0_phi",
    "ditau_tau0_m",

    "ditau_tau1_pt",
    "ditau_tau1_eta",
    "ditau_tau1_phi",
    "ditau_tau1_m",

    "met_et",
    "met_etx",
    "met_ety",
    
    ]


# # reco level training; goal is to predict Higgs mass.
HH_FEATURES= ['ditau_dr',
              'met_et',
              'ditau_scal_sum_pt',
              'ditau_vect_sum_pt',
              'ditau_mt_lep0_met',
              'ditau_mt_lep1_met',
              'ditau_vis_mass',
              'ditau_dphi',
              'ditau_tau0_pt',
              'ditau_tau1_pt',
              'ditau_met_min_dphi',
              'ditau_met_lep0_cos_dphi',
              'ditau_met_lep1_cos_dphi',
              'ditau_dpt',
              
               
              # # # low correlation features
              # "ditau_tau0_eta",
              # "ditau_tau0_phi",
              # "ditau_tau0_m",
              
              # "ditau_tau1_eta",
              # "ditau_tau1_phi",
              # "ditau_tau1_m",
              
              # "met_etx",
              # "met_ety",
              # 'met_sumet',

              # 'ditau_coll_approx_m',
              # # 'ditau_coll_approx_x0', 
              # # 'ditau_coll_approx_x1',

              # "ditau_tau0_n_tracks",
              # "ditau_tau1_n_tracks",
              # "ditau_tau0_jet_bdt_score",
              
              # # NOT IN NTUPS
              #'ditau_ptx',
              #'ditau_pty',
              
              
              #"dijet_vis_mass",
              #"dijet_deta",
              
              # "ditau_tau0_jet_bdt_score_trans",
              # 'ditau_pt_diff',
              # 'ditau_pt_ratio',
              # 'ditau_mt',
              # 'ditau_cos_theta',

              # "ditau_mmc_mlm_m",
              ]

HH_CUT_BRANCHES = [
    "ditau_tau0_jet_bdt_medium", 
    "ditau_tau1_jet_bdt_medium",
    "ditau_tau0_matched_isHadTau",
    "ditau_tau1_matched_isHadTau",
    "jet_1_pt",
    "jet_0_pt",
    ]

TARGET = ["parent_m"]
HH_MASS_PREDICTORS = [
    "ditau_mmc_mlm_m",
    #'ditau_mmc_mlnu3p_m',
    #'ditau_mosaic_mH_m6',
    ]
HH_BRACNHES = list(
    set(HH_FEATURES + HH_CUT_BRANCHES + TARGET + HH_MASS_PREDICTORS)
    )

##------------------------------------------------------------------------
## lephad channel features
LH_FEATURES= ['lephad_dr',
              'met_reco_et',
              'lephad_scal_sum_pt',
              'lephad_vect_sum_pt',
              'lephad_mt_lep0_met',
              'lephad_mt_lep1_met',
              'lephad_vis_mass',
              'lephad_dphi',
              'lep_0_pt',
              'tau_0_pt',
              'lephad_met_min_dphi',
              'lephad_met_lep0_cos_dphi',
              'lephad_met_lep1_cos_dphi',
              'lephad_dpt',
              ]

LH_MASS_PREDICTORS = ["lephad_mmc_mlm_m"]
LH_CUT_BRACNHES = [
    "is_oneselectedlep",
    "is_oneselectedtau",
    "met_reco_et",
    "lep_0_q",
    "tau_0_q",
    "tau_0_jet_bdt_score",
    "tau_0_jet_bdt_medium",
    "tau_0_eta",
    "n_bjets",
    "lephad_mt_lep0_met",
    "ditau_matched",
    "is_boosted_mva",
    "is_vbf_mva",
    ]

LH_BRANCHES = list(
    set(LH_FEATURES + LH_CUT_BRACNHES + TARGET + LH_MASS_PREDICTORS)
    )

##------------------------------------------------------------------------
## TRUTH MC15 feats
HH_FEATURES_TRUTH= ['true_ditau_vis_dr',
                    'true_met_et',
                    'true_ditau_vis_scal_sum_pt',
                    'true_ditau_vis_vect_sum_pt',
                    'true_ditau_vis_dpt',
                    'true_ditau_vis_mass',
                    'true_ditau_vis_dphi',
                    'true_tau_0_pt_vis',
                    'true_tau_1_pt_vis',                    
                    # 'true_ditau_vis_mt_lep0_met',
                    # 'true_ditau_vis_mt_lep1_met',
                    # 'true_ditau_vis_met_min_dphi',
                    # 'true_ditau_vis_met_lep0_cos_dphi',
                    # 'true_ditau_vis_met_lep1_cos_dphi',
                    'parent_m'
                    ]

HH_FEATURES_DITAU_TRUTH_MATCHED = [
    'ditau_matched_vis_dr',
    'true_met_et',
    'ditau_matched_vis_scal_sum_pt',
    'ditau_matched_vis_vect_sum_pt',
    # 'ditau_matched_vis_mt_lep0_met',
    # 'ditau_matched_vis_mt_lep1_met',
    'ditau_matched_vis_mass',
    'ditau_ditau_matched_vect_sum_pt_dphi',
    'ditau_matched_tau0_pt',
    'ditau_matched_tau1_pt',
    'ditau_met_min_dphi',
    'ditau_met_lep0_cos_dphi', #<! not availbale
    'ditau_met_lep1_cos_dphi', #<! not available
    'ditau_matched_dpt',

    # low correlation features
    # 'met_sumet',
    # 'ditau_mt',
    # 'ditau_pt_diff',
    # 'ditau_cos_theta',
    # 'ditau_coll_approx_m',
    # 'ditau_coll_approx_x0', 
    # 'ditau_coll_approx_x1',
    #'ditau_pt_ratio',
    ]

# # RECO TRUTH feats:
RECO_TRUTH_FEATURES = {
    'ditau_dr':
        ["ditau_dr", "ditau_matched_vis_dr"],
    'met_et':
        ['met_et', 'true_met_et'],
    'ditau_scal_sum_pt':
        ['ditau_scal_sum_pt', 'ditau_matched_vis_scal_sum_pt'],
    'ditau_vect_sum_pt':
        ['ditau_vect_sum_pt', 'ditau_matched_vis_vect_sum_pt'],
    # 'ditau_mt_lep0_met':
    #     ['ditau_mt_lep0_met', 'ditau_mt_lep0_met']
    # 'ditau_mt_lep1_met':
    #     ['ditau_mt_lep1_met', 'ditau_mt_lep1_met'],
    'ditau_vis_mass':
        ['ditau_vis_mass', 'ditau_matched_vis_mass'],
    'ditau_dphi':
        ['ditau_dphi', 'ditau_matched_vis_dphi'],
    'ditau_tau0_pt':
        ['ditau_tau0_pt', 'ditau_tau0_matched_pt'],
    'ditau_tau1_pt':
        ['ditau_tau1_pt', 'ditau_tau1_matched_pt'],
    # 'ditau_met_min_dphi':
    #     ['ditau_met_min_dphi', 'ditau_met_min_dphi'],
    # 'ditau_met_lep0_cos_dphi':
    #     ['ditau_met_lep0_cos_dphi', 'ditau_met_lep0_cos_dphi'],
    # 'ditau_met_lep1_cos_dphi':
    #     ['ditau_met_lep1_cos_dphi', 'ditau_met_lep1_cos_dphi'],
    # 'ditau_dpt':
    #     ['ditau_dpt', 'ditau_matched_vis_dpt'],
    }

##------------------------------------------------------------------------
## MC12 features 
FEATS_HH_TRUTH = (
    'dR_tau1_tau2',
    'MET_et',
    'sum_pt_tau1_tau2_met',
    'transverse_mass_tau1_met',
    'transverse_mass_tau2_met',
    'pt_diff_tau1_tau2',
    'mass_vis_tau1_tau2',
    'sum_pt_tau1_tau2', 
    'dPhi_tau1_tau2',
    'transverse_mass_tau1_tau2',
    'tau1_pt',  
    'mass_collinear_tau1_tau2',
    'cos_theta_tau1_tau2',
    'tau2_pt',
    'tau1_eta',
    'tau2_eta',
    'dPhi_tau1_MET',
    'dPhi_tau2_MET',
    'dPhi_tau1_tau2_MET',
    'vector_sum_pt_tau1_tau2',
    'vector_sum_pt_tau1_tau2_met')

TARGET_HH_TRUTH = ['resonance_m', 'resonance_et']
