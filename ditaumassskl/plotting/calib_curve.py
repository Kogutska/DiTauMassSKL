from . import *
__all__= ['plot_calib_curve',
          ]

def plot_calib_curve (samples,
                      brt_model = '',
                      branches= [],
                      features = [],
                      cuts= None,
                      category='gg',
                      prefix= ''):
    
    files = samples.get_files()
    brt = {'means': [], 'rms' : [], 'res': []}
    mmc = {'means': [], 'rms' : [], 'res': []}

    ## read regressor from disk
    with open (brt_model, 'rb') as m:
        regressor = pickle.load(m)
        m.close()
    print files
    for f in files:
        log.info("opening %s"%f)
        df = samples.get_dframe([f],branches=branches,cuts=cuts)

        brt_in = df.reindex(columns=features)
        brt_mass = regressor.predict(brt_in)
        mmc_mass = df.reindex(columns=['ditau_mmc_mlnu3p_m']).ix[:,0]

        brt_mean = np.mean(brt_mass)
        brt_rms  = np.std(brt_mass)
        mmc_mean = np.mean(mmc_mass)
        mmc_rms  = np.std(mmc_mass)

        brt['means'].append(brt_mean)
        mmc['means'].append(mmc_mean)
        brt['rms'].append(brt_rms)
        mmc['rms'].append(mmc_rms)
        #del df_h, brt_in, brt_in

    true_mass = range(100, 155, 5)
    x = [60, 180]
    y = [60, 180]

    fig = plt.figure()
    plt.plot(x,y, color='black', linewidth=2, marker='o')
    plt.errorbar([x+1 for x in true_mass],
                 brt['means'],
                 yerr=brt['rms'],
                 label="BRT",
                 color='blue',
                 marker = 'o',
                 linestyle=':',
                 linewidth = 2)
    plt.errorbar(true_mass,
                 mmc['means'],
                 yerr=mmc['rms'],
                 label="MMC",
                 color='red',
                 marker = 'o',
                 linestyle=':',
                 linewidth=2)
    
    plt.legend(loc='best')
    #plt.grid()
    plt.xlim(50,200)
    plt.ylim(50, 200)
    plt.ylabel("reco mass")
    plt.xlabel("true mass")
    plt.legend(loc="best")
    outfig = "./plots/"+prefix+"_calibration_curve_%s.eps"%category
    fig.savefig(outfig)
    log.info("created %s"%outfig)
