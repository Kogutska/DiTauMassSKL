import math
def get_label(variable):
    label = variable['root']
    if 'units' in variable.keys():
        label += ' [{0}]'.format(variable['units'])
    return label

#### compatible with the 8 TeV RECO and TRUTH samples
VARIABLES_TRUTH = {
    'resonance_m': {
        'name': 'resonance_m',
        'root': 'm_{H}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },

    'mass_vis_tau1_tau2' : {
        'name': 'mass_vis_tau1_tau2',
        'root': 'visible m_{#tau #tau}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },


    'mass_collinear_tau1_tau2' : {
        'name': 'mass_collinear_tau1_tau2',
        'root': 'm_{coll}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },


    'tau1_pt': {
        'name': 'tau1_pt',
        'root': '#tau1_{p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'tau2_pt': {
        'name': 'tau2_pt',
        'root': '#tau2_{ p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'pt_diff_tau1_tau2': {

       'name': 'pt_diff_tau1_tau2',
        'root': '#Delta P_{T} (#tau1, #tau2)',
        'type': 'f',
        'bins': 20,
        'range': (0., 1.2)
        },

    'tau1_eta': {
        'name': 'tau1_eta',
        'root': '#eta_{#tau_{1}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },

    'tau2_eta': {
        'name': 'tau2_eta',
        'root': ' #eta_{ #tau_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },
 
    # 'dEta_jet1_jet2': {
    #     'name': 'dEta_jet1_jet2',
    #     'root': 'd#eta_{jj}',
    #     'type': 'f',
    #     'bins': 10,
    #     'range': (0, 10)
    #     },
 
   'dEta_jets': {
        'name': 'dEta_jets',
        'root': 'd#eta_{jj}',
        'type': 'f',
        'bins': 10,
        'range': (0, 10)
        },
 
    
    'dPhi_tau1_MET': {
        'name': 'dPhi_tau1_MET', 
        'root': '#Delta #phi(#tau1, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau2_MET': {
        'name': 'dPhi_tau2_MET', 
        'root': '#Delta #phi(#tau2, MET)',
        'type': 'f',
        'units' : 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_tau1_tau2': {
        'name': 'dPhi_tau1_tau2', 
        'root': '#Delta #phi (#tau1, #tau2)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dPhi_min_tau_MET': {
        'name': 'dPhi_min_tau_MET', 
        'root': '#Delta #phi (#tau1 #tau2, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'dR_tau1_tau2': {
        'name': 'dR_tau1_tau2',
        'root': '#Delta R(#tau, #tau)',
        'type': 'f',
        'bins': 20,
        'range': (0, 4)
        },
 
    'eta_product_jets': {
        'name': 'eta_product_jets', 
        'root': '#eta_{jet_{1}} #times #eta_{jet_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-20. , 20. )
        },

    'cos_theta_tau1_tau2': {
        'name': 'cos_theta_tau1_tau2',
        'root': 'cos(#theta_{#tau1 #tau2})',
        'type':'f',
        'bins' : 20,
        'range' : (-1.2 , 1.2)
        },

    'mass_jet1_jet2': {
        'name': 'mass_jet1_jet2', 
        'root': 'm_{jj}',
        'type': 'f',
        'units': 'GeV',
        'scale' : 1.,
        'bins': 30,
        'range': (0. , 2000. )
        },


    'mass_tau1_tau2_jet1': {
        'name': 'mass_tau1_tau2_jet1' ,
        'root': 'm_{#tau #tau j}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1., 
        'bins': 30,
        'range': (0. , 1200.)
        },

     
    'MET_et': {    
        'name': 'MET_et' ,
        'root': 'E_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1., 
        'bins': 30,
        'range': (0. , 200.)
        },
    


    'tau_pt_ratio': {
        'name': 'tau_pt_ratio' ,
        'root': 'P^{ #tau 1}_{T} / P^{#tau 2}_{T} ',
        'type': 'f',
        'bins': 20,
        'range': (0. , 30)
        },

    
    'sum_pt_tau1_tau2': {
       'name': 'sum_pt_tau1_tau2' ,
        'root': 'P^{#tau1 #tau2}_{T}',
        'type': 'f',
       'units' : 'GeV',
       'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'sum_pt_tau1_tau2_met': {
        'name': 'sum_pt_tau1_tau2_met' ,
        'root': 'P^{#tau1#tau2 MET}_{T}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 40,
        'range': (0. , 400.)
        },


    # 'tau1_eta_centrality': {
    #    'name': 'tau1_eta_centrality' ,
    #     'root': '#tau 1 #eta -Centrality',
    #     'type': 'f',
    #     'bins':20,  
    #     'range': (0. , 1.5)
    #     },

    # 'tau2_eta_centrality': {
    #     'name': 'tau2_eta_centrality' ,
    #     'root': '#tau 2 #eta -Centrality',
    #     'type': 'f',
    #     'bins':20,  
    #     'range': (0. , 1.5)
    #     },


    'transverse_mass_tau1_met': {
        'name': 'transverse_mass_tau1_met' ,
        'root': 'm_{T}(#tau1 MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'transverse_mass_tau2_met': {
        'name': 'transverse_mass_tau2_met' ,
        'root': 'm_{T}(#tau_{2} MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },



    'transverse_mass_tau1_tau2': {
        'name': 'transverse_mass_tau1_tau2' ,
        'root': 'm^{T}_{#tau_{1} #tau_{2}}',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'vector_sum_pt_tau1_tau2': {
        'name': 'vector_sum_pt_tau1_tau2',
        'root' : '#vec{P}_{T}(#tau1 #tau2)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 40,
        'range': (0. , 500.)
        },
        

    'vector_sum_pt_tau1_tau2_met': {
        'name': 'vector_sum_pt_tau1_tau2_met', 
        'root': '#vec{P}_{T}(#tau1 #tau2 MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 40,
        'range': (0. , 700.)
        },

    # 'sum_pt_full': {
    #     'name': 'sum_pt_full', 
    #     'root': '#P^{Full}_{T}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 30,
    #     'range': (0. , 1200.)
    #     },


    # 'vector_sum_pt_full': {
    #     'name': 'vector_sum_pt_full', 
    #     'root': '#vec{P}^{Full}_{T}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 30,
    #     'range': (0. , 1200.)
    #     },



##### RELATIVE kinematics of jets and taus

    # 'mass_ratio_jets_taus': {
    #     'name': 'mass_ratio_jets_taus', 
    #     'root': 'm_{jj}/m_{#tau#tau}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },

    # 'sum_pt_ratio_jets_taus': {
    #     'name': 'sum_pt_ratio_jets_taus', 
    #     'root': 'P^{jj}_{T}/P^{#tau#tau}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },


    # 'vector_sum_pt_ratio_jets_taus': {
    #     'name': 'vector_sum_pt_ratio_jets_taus', 
    #     'root': '#vec{P}^{jj}_{T}/#vec{P}^{#tau#tau}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },


    # 'dR_ratio_jets_taus': {
    #     'name': 'dR_ratio_jets_taus', 
    #     'root': 'dR_{jj} / dR_{#tau#tau}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 10.)
    #     },
    # 'sum_pt_ratio_full_tausMET': {
    #     'name': 'sum_pt_ratio_full_tausMET', 
    #     'root': 'P^{Full}_{T} / P^{#tau#tau MET}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 10.)
    #     },





}



VARIABLES = {
    'parent_m': {
        'name': 'parent_m',
        'root': 'm_{H}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },

    'ditau_vis_mass' : {
        'name': 'ditau_vis_mass',
        'root': 'm^{vis}_{#tau #tau}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },


    # 'ditau_coll_approx_m' : {
    #     'name': 'ditau_coll_approx_m',
    #     'root': 'm_{coll}',
    #     'type': 'f',
    #     'units': 'GeV',
    #     'scale': 0.001,
    #     'bins': 30,
    #     'range': (0, 1000)
    #     },


    'ditau_tau0_pt': {
        'name': 'ditau_tau0_pt',
        'root': '#tau1_{p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'ditau_tau1_pt': {
        'name': 'ditau_tau1_pt',
        'root': '#tau2_{ p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'ditau_dpt': {

       'name': 'ditau_dpt',
        'root': '#Delta P_{T} (#tau1, #tau2)',
        'type': 'f',
        'bins': 20,
        'range': (-200, 200)
        },

    'ditau_tau0_eta': {
        'name': 'ditau_tau0_eta',
        'root': '#eta_{#tau_{1}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },

    'ditau_tau1_eta': {
        'name': 'ditau_tau1_eta',
        'root': ' #eta_{ #tau_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)

        },

    'ditau_tau0_phi': {
        'name': 'ditau_tau0_phi',
        'root': '#phi_{#tau_{1}}',
        'type': 'f',
        'bins': 20,
        'range': (-3., 3.)
        },

    'ditau_tau1_phi': {
        'name': 'ditau_tau1_phi',
        'root': ' #phi_{ #tau_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },
    
    'met_phi': {    
        'name': 'met_phi', 
        'root': 'MET_phi',
        'type': 'f',
        'bins': 20,
        'range': (-3. , 3.)
        },

 
    #### ditau variables

    # "ditau_met_sum_cos_dphi":{
    #     'name': 'ditau_met_sum_cos_dphi', 
    #     'root': 'Sum cos(#Delta #phi)',
    #     'type': 'f',
    #     'units': 'rad',
    #     'bins': 20,
    #     'range': (-3. , 3.)
    #             },
     
    # "ditau_cosalpha":{
    #     'name': 'ditau_cosalpha', 
    #     'root': 'cos(#alpha)',
    #     'type': 'f',
    #     'bins': 20,
    #     'range': (-1. , 1.)
    #     },
    

    # 'ditau_met_centrality': {    
    #     'name': 'ditau_met_centrality', 
    #     'root': 'MET_phi_centrality',
    #     'type': 'f',
    #     'bins': 20,
    #     'range': (-3. , 3.)
    #     },



    'ditau_met_lep0_cos_dphi': {
        'name': 'ditau_met_lep0_cos_dphi', 
        'root': '#Delta #phi(#tau1, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'ditau_met_lep1_cos_dphi': {
        'name': 'ditau_met_lep1_cos_dphi', 
        'root': '#Delta #phi(#tau2, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },


    'ditau_dphi': {
        'name': 'ditau_dphi', 
        'root': '#Delta #phi (#tau1, #tau2)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'ditau_met_min_dphi': {
        'name': 'ditau_met_min_dphi', 
        'root': '#Delta #phi (#tau1 #tau2, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'ditau_dr': {
        'name': 'ditau_dr',
        'root': '#Delta R(#tau, #tau)',
        'type': 'f',
        'bins': 20,
        'range': (0, 4)
        },
 

    # 'ditau_cos_dtheta': {
    #     'name': 'ditau_cos_dtheta',
    #     'root': 'cos(#theta_{#tau1 #tau2})',
    #     'type':'f',
    #     'bins' : 20,
    #     'range' : (-1.2 , 1.2)
    #     },

     
    'met_et': {    
        'name': 'met_et' ,
        'root': 'E_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1., 
        'bins': 30,
        'range': (0. , 200.)
        },


    # 'tau_pt_ratio': {
    #     'name': 'tau_pt_ratio' ,
    #     'root': 'P^{ #tau 1}_{T} / P^{#tau 2}_{T} ',
    #     'type': 'f',
    #     'bins': 20,
    #     'range': (0. , 30)
    #     },
 
    
    'ditau_scal_sum_pt': {
       'name': 'ditau_scal_sum_pt' ,
        'root': 'P^{#tau1 #tau2}_{T}',
        'type': 'f',
       'units' : 'GeV',
       'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'ditau_vect_sum_pt': {
        'name': 'ditau_vect_sum_pt',
        'root' : '#vec{P}_{T}(#tau1 #tau2)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 40,
        'range': (0. , 500.)
        },
        

    'ditau_mt_lep0_met': {
        'name': 'ditau_mt_lep0_met' ,
        'root': 'm_{T}(#tau1 MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'ditau_mt_lep1_met': {
        'name': 'ditau_mt_lep1_met' ,
        'root': 'm_{T}(#tau_{2} MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    # 'ditau_mt': {
    #     'name': 'ditau_mt' ,
    #     'root': 'm^{T}_{#tau_{1} #tau_{2}}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 30,
    #     'range': (0. , 300.)
    #     },


    
    #### dijet variables 
     
   # 'dijet_deta': {
   #      'name': 'dijet_deta',
   #      'root': 'd#eta_{jj}',
   #      'type': 'f',
   #      'bins': 10,
   #      'range': (0, 10)
    #      },
 
   #  'dijet_etaXeta': {
   #      'name': 'dijet_etaXeta', 
   #      'root': '#eta_{jet_{1}} #times #eta_{jet_{2}}',
   #      'type': 'f',
   #      'bins': 20,
   #      'range': (-20. , 20. )
   #      },


   #      'dijet_m': {
   #      'name': 'dijet_m', 
   #      'root': 'm_{jj}',
   #      'type': 'f',
   #      'units': 'GeV',
   #      'scale' : 1.,
   #      'bins': 30,
   #      'range': (0. , 2000. )
   #      },




    # 'vector_sum_pt_tau1_tau2_met': {
    #     'name': 'vector_sum_pt_tau1_tau2_met', 
    #     'root': '#vec{P}_{T}(#tau1 #tau2 MET)',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 40,
    #     'range': (0. , 700.)
    #     },



    # 'sum_pt_tau1_tau2_met': {
    #     'name': 'sum_pt_tau1_tau2_met' ,
    #     'root': 'P^{#tau1#tau2 MET}_{T}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 40,
    #     'range': (0. , 400.)
    #     },


    # 'tau1_eta_centrality': {
    #    'name': 'tau1_eta_centrality' ,
    #     'root': '#tau 1 #eta -Centrality',
    #     'type': 'f',
    #     'bins':20,  
    #     'range': (0. , 1.5)
    #     },

    # 'tau2_eta_centrality': {
    #     'name': 'tau2_eta_centrality' ,
    #     'root': '#tau 2 #eta -Centrality',
    #     'type': 'f',
    #     'bins':20,  
    #     'range': (0. , 1.5)
    #     },


    # 'sum_pt_full': {
    #     'name': 'sum_pt_full', 
    #     'root': '#P^{Full}_{T}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 30,
    #     'range': (0. , 1200.)
    #     },


    # 'vector_sum_pt_full': {
    #     'name': 'vector_sum_pt_full', 
    #     'root': '#vec{P}^{Full}_{T}',
    #     'type': 'f',
    #     'units' : 'GeV',
    #     'scale': 1.,
    #     'bins': 30,
    #     'range': (0. , 1200.)
    #     },



##### RELATIVE kinematics of jets and taus

    # 'mass_ratio_jets_taus': {
    #     'name': 'mass_ratio_jets_taus', 
    #     'root': 'm_{jj}/m_{#tau#tau}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },

    # 'sum_pt_ratio_jets_taus': {
    #     'name': 'sum_pt_ratio_jets_taus', 
    #     'root': 'P^{jj}_{T}/P^{#tau#tau}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },


    # 'vector_sum_pt_ratio_jets_taus': {
    #     'name': 'vector_sum_pt_ratio_jets_taus', 
    #     'root': '#vec{P}^{jj}_{T}/#vec{P}^{#tau#tau}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 30.)
    #     },


    # 'dR_ratio_jets_taus': {
    #     'name': 'dR_ratio_jets_taus', 
    #     'root': 'dR_{jj} / dR_{#tau#tau}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 10.)
    #     },
    # 'sum_pt_ratio_full_tausMET': {
    #     'name': 'sum_pt_ratio_full_tausMET', 
    #     'root': 'P^{Full}_{T} / P^{#tau#tau MET}_{T}',
    #     'type': 'f',
    #     'units' : '',
    #     'bins': 40,
    #     'range': (0. , 10.)
    #     },




    }


VARIABLES_Truth = {
    'parent_m': {
        'name': 'parent_m',
        'root': 'm_{H}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },

    'true_ditau_vis_mass' : {
        'name': 'true_ditau_vis_mass',
        'root': 'm_{#tau #tau}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (50, 200)
        },


    'true_ditau_coll_approx_m' : {
        'name': 'true_ditau_coll_approx_m',
        'root': 'm_{coll}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0, 1000)
        },


    'ditau_tau0_pt': {
        'name': 'ditau_tau0_pt',
        'root': '#tau1_{p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'ditau_tau1_pt': {
        'name': 'ditau_tau1_pt',
        'root': '#tau2_{ p_{T}}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1.,
        'bins': 20,
        'range': (20, 120)
        },

    'true_ditau_dpt': {

       'name': 'true_ditau_dpt',
        'root': '#Delta P_{T} (#tau1, #tau2)',
        'type': 'f',
        'bins': 20,
        'range': (0., 1.2)
        },

    'ditau_tau0_eta': {
        'name': 'ditau_tau0_eta',
        'root': '#eta_{#tau_{1}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },

    'ditau_tau1_eta': {
        'name': 'ditau_tau1_eta',
        'root': ' #eta_{ #tau_{2}}',
        'type': 'f',
        'bins': 20,
        'range': (-2.5, 2.5)
        },
 
    #### ditau variables
    'ditau_met_lep0_cos_dphi': {
        'name': 'ditau_met_lep0_cos_dphi', 
        'root': '#cos(#Delta #phi(#tau1, MET))',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'ditau_met_lep1_cos_dphi': {
        'name': 'ditau_met_lep1_cos_dphi', 
        'root': '#cos(#Delta #phi(#tau2, MET))',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },


    'true_ditau_vis': {
        'name': 'true_ditau_vis', 
        'root': '#Delta #phi (#tau1, #tau2)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'ditau_met_min_dphi': {
        'name': 'ditau_met_min_dphi', 
        'root': '#Delta #phi (#tau1 #tau2, MET)',
        'type': 'f',
        'units': 'rad',
        'bins': 20,
        'range': (0. , 4.5)
        },

    'true_ditau_vis_dr': {
        'name': 'ditau_dr',
        'root': '#Delta R(#tau, #tau)',
        'type': 'f',
        'bins': 20,
        'range': (0, 4)
        },
 

    # 'ditau_cos_dtheta': {
    #     'name': 'ditau_cos_dtheta',
    #     'root': 'cos(#theta_{#tau1 #tau2})',
    #     'type':'f',
    #     'bins' : 20,
    #     'range' : (-1.2 , 1.2)
    #     },

     
    'met_et': {    
        'name': 'met_et' ,
        'root': 'E_{T}',
        'type': 'f',
        'units': 'GeV',
        'scale': 1., 
        'bins': 30,
        'range': (0. , 200.)
        },

    'true+ditau_met_centrality': {    
        'name': 'ditau_met_centrality', 
        'root': 'MET_phi_centrality',
        'type': 'f',
        'bins': 20,
        'range': (-3. , 3.)
        },

    # 'tau_pt_ratio': {
    #     'name': 'tau_pt_ratio' ,
    #     'root': 'P^{ #tau 1}_{T} / P^{#tau 2}_{T} ',
    #     'type': 'f',
    #     'bins': 20,
    #     'range': (0. , 30)
    #     },

    
    'ditau_scal_sum_pt': {
       'name': 'ditau_scal_sum_pt' ,
        'root': 'P^{#tau1 #tau2}_{T}',
        'type': 'f',
       'units' : 'GeV',
       'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'ditau_vect_sum_pt': {
        'name': 'ditau_vect_sum_pt',
        'root' : '#vec{P}_{T}(#tau1 #tau2)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 40,
        'range': (0. , 500.)
        },
        

    'ditau_mt_lep0_met': {
        'name': 'ditau_mt_lep0_met' ,
        'root': 'm_{T}(#tau1 MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },

    'ditau_mt_lep1_met': {
        'name': 'ditau_mt_lep1_met' ,
        'root': 'm_{T}(#tau_{2} MET)',
        'type': 'f',
        'units' : 'GeV',
        'scale': 1.,
        'bins': 30,
        'range': (0. , 300.)
        },
}
