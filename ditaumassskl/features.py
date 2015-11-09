
## reco level training; goal is to predict Higgs mass.
features = ['ditau_dr',
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

target = ["parent_m"]
