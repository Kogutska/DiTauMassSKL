from . import *
import numpy as np
__all__= ['plot_calib_curve',
          ]

def plot_calib_curve (masses, predictors, 
                      pnames=["BRT", "MMC"], 
                      mode='gg', prefix= '',
                      category=None,
                      label=None
                      ):
    """
    evaluate predictors over some range.
    Parameters
    -----------
    masses: list, mass range that you want to evaluate estimators.
    predictors: dict, predictor[MODE][MASS][TYPE]= [PREDICTIONS])
    
    Return
    ------
    None
    """
    colors = ["blue", "red", "green"] 
    fig = plt.figure()
    ax = plt.gca()
    plt.plot(masses, masses, color='black', linewidth=2, marker='o')
    counter = 0
    for pname in pnames:
        means = []  
        stds  = []
        for mass in masses:
            means.append(np.mean(predictors[mode][mass][pname]))
            stds.append(np.std(predictors[mode][mass][pname]))
            
        plt.errorbar([mass+2 for mass in masses], #< offset by 2
                     means,
                     yerr=stds,
                     label=pname,
                     color=colors[counter],
                     marker = 'o',
                     linestyle=':',
                     linewidth = 2)
        counter += 1

    plt.legend(loc='best')
    plt.grid()
    plt.xlim(max(0, masses[0]-50), masses[-1]+50)
    plt.ylim(max(0, masses[0]-50), masses[-1]+50)
    plt.ylabel("reco mass")
    plt.xlabel("true mass")
    plt.legend(loc="best")
    
    cat=''
    if category:
        cat =category.name.upper()
    if label is None:
        label=''
    plt.text(0.2, 0.85,label+"("+cat+")", 
             fontsize=15,
             horizontalalignment='center',
             verticalalignment='center',
             transform=ax.transAxes)

    for ext in [".png", ".eps", ".pdf"]:
        outfig = "./plots/"+prefix+"_calibration_curve_%s%s"%(cat, ext)
        fig.savefig(outfig)
        log.info("created %s"%outfig)
    
