
from. import *
__all__ =['cal_roc', 
          'area_under_roc',
          'plot_roc_curve']

def cal_roc(y_bkg, y_sig):
    """ to get the false positive rate and true positive rate.
    Parameters:
    ----------
    y_bkg : numpy array type, bkg di-tau mass estimation.
    y_sig : numpy array type, sig di-tau mass estimation

    Returns:
    --------
    a tuple of rejection efficiency and acceptance efficiency for different cuts on mass.

    """

    bins = np.linspace(50,200,50)
    frac_bkg, bin_bkg, _bkg = plt.hist(y_bkg, bins=bins, normed=1)
    frac_sig, bin_sig, _sig = plt.hist(y_sig, bins=bins, normed=1)
    plt.close()
    ## calculate the area under hist sequentially
    bkg = np.zeros(len(bins))
    sig = np.zeros(len(bins))
    bkg[0]=1.
    sig[0]=1.

    c= 1
    step=bins[1]-bins[0]
    while c <len(bins)-1:
        bkg[c] = bkg[c-1]- step*frac_bkg[c]
        sig[c] = sig[c-1]- step*frac_sig[c]
        c +=1
    rej = 1.-bkg
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

def plot_roc_curve(brt, mmc, category= 'gg', prefix=''):
    area_brt = area_under_roc(brt)
    area_mmc  = area_under_roc(mmc)

    fig = plt.figure()
    plt.plot(brt[0], brt[1], label="AUC BRT= %0.4f"%area_brt, color='blue', marker = 'o')
    plt.plot(mmc[0], mmc[1], label="AUC MMC= %0.4f"%area_mmc, color ='red', marker = 'o')
    plt.legend(loc='best')
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.ylabel("Z90 Rejection")
    plt.xlabel("H125 Acceptance")
    plt.legend(loc="best")
    outfig = "./plots/"+prefix+"roc_curve_%s.eps"%category
    fig.savefig(outfig)
    log.info("created %s"%outfig)


