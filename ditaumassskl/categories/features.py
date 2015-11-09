
# BE CAREFUL, THE ORDER
# MATTERS -- TMVA YOU SUCK :-(


## HADHAD ORDER !!



FEATURES_TRUTH = [
   # 'resonance_m',
    'dR_tau1_tau2',
   # 'MET_et',
    'sum_pt_tau1_tau2_met',
    'transverse_mass_tau1_met',
    'transverse_mass_tau2_met',
    #'pt_diff_tau1_tau2',

    'mass_vis_tau1_tau2',
    'sum_pt_tau1_tau2', 
   # 'dPhi_tau1_tau2',
    'transverse_mass_tau1_tau2',
    
    'tau1_pt',  
    
    #'cos_theta_tau1_tau2',
    
    'tau2_pt',
    #'tau1_eta',
    #'tau2_eta',
    
    #'dPhi_tau1_MET',
    #'dPhi_tau2_MET',
    #'dPhi_min_tau_MET',
    
    #'vector_sum_pt_tau1_tau2',
    #'vector_sum_pt_tau1_tau2_met',
    #'mass_collinear_tau1_tau2',
    

    ]



#### for 13 TeV truth 
FEATURES_Tr = [
   # 'parent_m',
    'ditau_dr',
    'met_et',
    'ditau_scal_sum_pt',
    'ditau_vect_sum_pt',
    'ditau_mt_lep0_met',
    'ditau_mt_lep1_met',
    'ditau_dpt',
    'ditau_vis_mass',
    'ditau_dphi',
    'ditau_tau0_pt',  
    'ditau_tau1_pt',
    'ditau_met_min_dphi',
    'ditau_met_lep0_cos_dphi',
    'ditau_met_lep1_cos_dphi',
    
    ]


#### reco variables
FEATURES = [
    #'parent_m',
    'ditau_dr',
    'met_et',
    'ditau_scal_sum_pt',
    'ditau_vect_sum_pt',
    'ditau_mt_lep0_met',
    'ditau_mt_lep1_met',
    'ditau_dpt',
    'ditau_vis_mass',
    'ditau_dphi',
    'ditau_tau0_pt',  
    'ditau_tau1_pt',
    'ditau_met_min_dphi',
    'ditau_met_lep0_cos_dphi',
    'ditau_met_lep1_cos_dphi',
    # "ditau_met_sum_cos_dphi",
    # "ditau_cosalpha",
    # "ditau_met_centrality",
    # "ditau_coll_approx_m"
    ]


#### killing BRT :p
# FEATURES = [
#     'ditau_tau0_pt',
#     'ditau_tau0_phi',
#     'ditau_tau0_pt',
#     'ditau_tau1_phi',
#     'ditau_tau0_eta',
#     'ditau_tau1_eta',    
#     'met_et',
#     'met_phi',
   
# ]


### LEPHAD ORDER



# FEATURES = [
    
#     'dR_tau1_tau2',
#     'MET_et',
#     'sum_pt_tau1_tau2_met',
#     'transverse_mass_tau1_met',
#     'transverse_mass_tau2_met',
#     'pt_diff_tau1_tau2',
#     'mass_vis_tau1_tau2',
#     'sum_pt_tau1_tau2', 
#     'dPhi_tau1_tau2',
#     'dPhi_tau1_tau2_MET',
#     'dPhi_tau1_MET',
#     'transverse_mass_tau1_tau2',
#     'tau1_pt',   
#     'cos_theta_tau1_tau2',
#     'tau2_pt',

#     ]
#     'tau1_eta',
#     'tau2_eta',
#     'dPhi_tau2_MET',
#     'vector_sum_pt_tau1_tau2',
#     'vector_sum_pt_tau1_tau2_met',
#     'mass_collinear_tau1_tau2',
    
#     ]




### not very useful taus kinematics



#### ##### RELATIVE kinematics of jets and taus

# 'mass_ratio_jets_taus',
# 'sum_pt_ratio_jets_taus',
# 'vector_sum_pt_ratio_jets_taus',
# 'sum_pt_ratio_full_tausMET',
# 'dR_ratio_jets_taus',



# ####  NOT USEFUl FOR BRT  TRAINING , very low correlation with resonance mass ###

# 'dEta_jets',
# 'eta_product_jets',
# 'mass_jet1_jet2',
# 'mass_tau1_tau2_jet1',
# 'met_phi_centrality',
# 'tau1_eta_centrality',
# 'sum_pt_full',
# 'vector_sum_pt_full',
    
features_vbf = FEATURES
features_boosted = FEATURES
