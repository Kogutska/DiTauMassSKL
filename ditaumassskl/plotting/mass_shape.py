import ROOT
import matplotlib.patches as patches

# build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height


from . import *
__all__ = ['plot_mass',
           'compare_mass',
           'plot_size_dependency'
           ]

def plot_mass(predict_mass, true_mass = 100, category=None, label=None,prefix=''):
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
    cat=''
    if category is not None:
        cat =category.name
    if label is None:
        label=''
    plt.text(0.2, 0.85,label+cat, 
             fontsize=20,
             horizontalalignment='center',
             verticalalignment='center',
             transform=ax.transAxes)

    for format in [".png", ".eps", ".pdf"]:
        outfig="./plots/"+prefix+"_mass_shape_"+str(true_mass)+"_"+category.name+format
        fig.savefig(outfig)
        log.info("created %s"%outfig)
    fig.clear()

def compare_mass (sig, bkg, estimator='BRT', category=None, label=None, prefix=''):
    
    mean1 = np.mean(sig)
    std1 = np.std(sig)
    
    bins = np.linspace(0, 250, 50)    
    fig = plt.figure()
    ax = fig.gca()
    plt.hist(sig,bins=bins,
             color='b', alpha=0.5,
             histtype='stepfilled',
             normed=1,
             edgecolor='r',
             facecolor = 'none',
             hatch='/',
             label=estimator +'-H125:%0.2f + %0.2f'%(mean1, std1)
             )
    # p = mlab.normpdf(bins, mean1, std1)
    # plt.plot(bins, p, 'y--', linewidth=2)

    mean2 = np.mean(bkg)
    std2 = np.std(bkg)
    # p2 = mlab.normpdf(bins, mean2, std2)
    # plt.plot(bins, p2, 'g--', linewidth=2)

    plt.hist(bkg,bins=bins,
             color='b', alpha=0.5,
             histtype='stepfilled',
             normed=1,
             edgecolor='b',
             facecolor = 'none',
             #facecolor = 'red',
             hatch='\\',
             label= estimator+'-Z90: %0.2f + %0.2f'%(mean2, std2)
             )
    cat=''
    if category is not None:
        cat =category.name
    if label is None:
        label=''
    plt.text(0.2, 0.9,label+cat, 
             fontsize=14,
             horizontalalignment='center',
             verticalalignment='center',
             transform=ax.transAxes)

    plt.xlabel(estimator + " Mass")
    plt.ylabel("Fraction of events")
    plt.legend(loc='best')
    for format in [".png", ".eps", ".pdf"]:
        outfig = "./plots/"+prefix+"_Z90H125_"+ estimator+"_mass_%s%s"%(cat, format)
        fig.savefig(outfig)
        log.info("created %s"%outfig)
    fig.clear()
    
def plot_size_dependency(nevents,roc_area, label=None):
    """
    plot the area under roc curve versus input sample size per mass point.
    Parameters
    -----------
    nevents: list of sample size per mass point
    roc_area: lit of correspondingarea under roc curve
    
    """
    evts=np.array(nevents)
    area = np.array(roc_area)
    fig = plt.figure()
    ax=plt.gca()
    plt.plot(evts,area,'--bs', label=r'$H\rightarrow \tau_{h}\tau_{h}H125/Z90$' +'separation efficiency')

    plt.legend(loc='best')
    plt.grid()
    #plt.xlim(0.80,1.0)
    plt.ylim(0.86,.90)
    plt.ylabel("Area Under ROC Curve")
    plt.xlabel("Sample Size per Mass Point (k)")
    plt.legend(loc="best")
    outfig = "./plots/area_under_roc_curve_vs_sample_size_hh.eps"
    fig.savefig(outfig, dpi=1200)
    log.info("created %s"%outfig)
