#! /usr/bin/env python2.6
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from  scipy.stats import mode
from scipy.optimize import curve_fit

from sklearn import metrics

def compare(y1, y2, m1= 90, m2 = 125, tag1 ='Z', tag2 = 'H',**kwargs):
    """" to plot the mass line-shapes of two samples.

    Parameters
    ---------
    y_1 : numpy array; BRT-predicted mass (bkg)
    y_2 : numpy array; BRT-predicted mass (sig) 
    
    Retruns: None (saves plots as .eps files)
    """
    bins = np.linspace(0, 200, 40)
    fig = plt.figure()
    ax = fig.gca()
    plt.hist(y1,bins=bins,
             color='r', alpha=0.5,
             histtype='step',#linestyles=('solid','dashed'),
             normed=1,
             label='BRT: %0.2f +%0.2f'%(mean1, std1))
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
     
    # plt.hist(y2,bins=bins,
    #          color='b', alpha=0.5,
    #          histtype='step', #normed=1,
    #          label='BRT-Mcut: %0.2f +%0.2f'%(mean2, std2))
    
    # x2 = np.linspace(np.min(y2), np.max(y2), 100)
    # #plt.plot(x2, mlab.normpdf(x2,mode2,std2), color='y')

    plt.xlabel("Z90 Mass")
    plt.ylabel("#frac of Events")
    plt.legend(loc='best')
    ax.set_xticks(np.arange(0.,200.,20))
    plt.grid()
    plt.show()
    fig.savefig("./plots/Z90_mass_lineshapes_BRT.png", dpi=600)
    fig.clear()
 
def roc_curve(y_bkg, y_sig):
    """ to get the false positive rate and true positive rate.
    Parameters:
    ----------
    y_bkg : numpy array type, bkg di-tau mass estimation.
    y_sig : numpy array type, sig di-tau mass estimation
    
    Returns:
    --------
    a tuple of rejection efficiency and acceptance efficiency for different cuts on mass.

    """
    
    bins = np.linspace(50,200,30)
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
