
from . import *
__all__ =['cal_roc', 
          'area_under_roc',
          'plot_roc_curve',
          'compare_brts']

def cal_roc(y_bkg, y_sig, bins=None):
    """ to get the false positive rate and true positive rate.
    Parameters:
    ----------
    y_bkg : numpy array type, bkg di-tau mass estimation.
    y_sig : numpy array type, sig di-tau mass estimation

    Returns:
    --------
    a tuple of rejection efficiency and acceptance efficiency for different cuts on mass.

    """
    if (bins is None):
        bins = np.linspace(50,200,30)
    frac_bkg, bin_bkg, _bkg = plt.hist(y_bkg, bins=bins, normed=1)
    frac_sig, bin_sig, _sig = plt.hist(y_sig, bins=bins, normed=1)
    plt.close()

    # calculate the area under hist sequentially
    bkg = np.zeros(len(bins))
    sig = np.zeros(len(bins))
    bkg[0]=1.
    sig[0]=1.

    c = 1
    step = bins[1]-bins[0]
    while c <len(bins)-1:
        bkg[c] = bkg[c-1]- step*frac_bkg[c]
        sig[c] = sig[c-1]- step*frac_sig[c]
        c +=1
    rej = 1. - bkg
    acc = sig

    return rej, acc

def area_under_roc (roc):
    """ to calculate area under roc curve.

    Parameters
    ----------
    roc:tuple of np arrays; false positive rate and true positive rate of classification as function of the cut on the target.

    Returns
    -------
    area: float; area under roc curve
    """
    area = trapz(roc[1], roc[0])
    return area

def plot_roc_curve(brt,mmc=None,mosaic=None,label=None, category= None, prefix=''):
    area_brt = area_under_roc(brt)
    if mmc is not None:
        area_mmc  = area_under_roc(mmc)
    if mosaic is not None:
        area_mosaic  = area_under_roc(mosaic)
        
    fig = plt.figure()
    ax = plt.gca()
    plt.plot(brt[0], brt[1], label="AUC BRT= %0.4f"%area_brt, color='blue', marker = 'o')
    if mmc is not None:
        plt.plot(mmc[0], mmc[1], label="AUC MMC= %0.4f"%area_mmc, color ='red', marker = 'o')
    if mosaic is not None:
        plt.plot(mosaic[0], mosaic[1], label="AUC Mosaic= %0.4f"%area_mosaic, color ='magenta', marker = 'o')
    
    plt.legend(loc='best')
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.ylabel("Z90 Rejection")
    plt.xlabel("H125 Acceptance")
    cat=''
    if category is not None:
        cat =category.name.upper()
    if label is None:
        label=''
    plt.text(0.2, 0.85,label+"("+cat+")", 
             fontsize=15,
             horizontalalignment='center',
             verticalalignment='center',
             transform=ax.transAxes)
    plt.legend(loc='lower left')
    for ext in [".png", ".pdf", ".eps"]:
        outfig = "./plots/"+prefix+"_roc_curve_%s%s"%(cat, ext)
        fig.savefig(outfig,)# dpi=1200
        log.info("created %s"%outfig)
    
    return 


def compare_brts(boosts,category=None,outprefix=None, outsuffix=None, label=None):
    """
    Parametres
    ----------
    bossts: dictionary of predicted signal versus background efficiens for different meta regressors
    category: Category object. see ../categories.
    outprefix: str, to add to the output(trained model name).
    outsuffix: str, to append to the plot output name (testing parameters)
    """
    colors=['blue','red','green','cyan','magenta','yellow','black','white']
    fig = plt.figure()
    ax = plt.gca()
    if len(colors) < len(boosts.keys()):
        colors = colors*(len(boost.keys()))
    i=0
    for name, brt in boosts.items():
        area_brt = area_under_roc(brt)
        plt.plot(brt[0], brt[1], label="AUC %s: %0.4f"%(name,area_brt), color=colors[i], marker = 's', linestyle='--')
        i+=1
       
    plt.legend(loc='best')
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.ylabel("Z90 Rejection")
    plt.xlabel("H125 Acceptance")
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
    outfig = "./plots/"+"roc_curve_comparing_boosts_%s.eps"%cat
    fig.savefig(outfig, dpi=1200)
    log.info("created %s"%outfig)
