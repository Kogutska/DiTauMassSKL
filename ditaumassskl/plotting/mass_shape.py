
from . import *
__all__ = ['plot_mass',
           'compare_mass',
           ]

def plot_mass(predict_mass, true_mass = 100, category=None, prefix=''):
    """ to plot the mass line-shape.    
    Parameters
    ----------
    mass: numpy array; Regression Tree Model predicted mass
    category: TCuts-Derived object; To specify the testing filters mode.

    Returns
    -------
    None; Saves plots on the disk.

    """
    mean = np.mean(predict_mass)
    std = np.std(predict_mass)
    bins = np.linspace(0, 250, 50)
    
    fig = plt.figure()
    ax = fig.gca()
    plt.hist(predict_mass,bins=bins,
             color='b', alpha=0.5,
             histtype='stepfilled',
             normed=1,
             facecolor = 'blue',
             label='BRT:%0.2f + %0.2f'%(mean, std)
             )                  
    p = mlab.normpdf(bins, mean, std)
    plt.plot(bins, p, 'r--', linewidth=2)
    
    plt.xlabel("BRT mass")
    plt.ylabel("Fraction of events")
    plt.legend(loc='best')
    #ax.set_xticks(np.arange(0.,220.,11))
    #plt.grid()
    outfig="./plots/"+prefix+"_mass_shape_"+str(true_mass)+"_"+category+".eps"
    fig.savefig(outfig)
    log.info("created %s"%outfig)
    fig.clear()

def compare_mass (sig, bkg, estimator='BRT', category='gg', prefix=''):
    
    mean1 = np.mean(sig)
    std1 = np.std(sig)
    bins = np.linspace(0, 250, 50)    
    fig = plt.figure()
    ax = fig.gca()
    plt.hist(sig,bins=bins,
             color='b', alpha=0.5,
             histtype='stepfilled',
             normed=1,
             facecolor = 'blue',
             label=estimator +'-H125:%0.2f + %0.2f'%(mean1, std1)
             )
    p = mlab.normpdf(bins, mean1, std1)
    plt.plot(bins, p, 'r', linewidth=1.5)
    
    mean2 = np.mean(bkg)
    std2 = np.std(bkg)
    plt.hist(bkg,bins=bins,
             color='b', alpha=0.5,
             histtype='stepfilled',
             normed=1,
             facecolor = 'red',
             label= estimator+'-Z90: %0.2f + %0.2f'%(mean2, std2)
             )
    p2 = mlab.normpdf(bins, mean2, std2)
    plt.plot(bins, p2, 'g', linewidth=1.5)

    plt.xlabel(estimator + " Mass")
    plt.ylabel("Fraction of events")
    plt.legend(loc='best')
    outfig = "./plots/"+prefix+"_Z90H125_"+ estimator+"_mass.eps"
    fig.savefig(outfig)
    log.info("created %s"%outfig)
    fig.clear()
    
