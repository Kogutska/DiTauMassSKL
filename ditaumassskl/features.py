
## reco level training; goal is to predict Higgs mass.
branches = ['ditau_dr',
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
            'parent_m'
            ]
## last one is the target
features= branches[:-1]
target = ["parent_m"]

estimators = ['ditau_mmc_mlnu3p_m',
              'ditau_mosaic_mH',
              ]
