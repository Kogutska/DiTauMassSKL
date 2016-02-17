

import pandas.core.common as com
from pandas.core.index import Index

from pandas.tools import plotting
from pandas.tools.plotting import scatter_matrix


# Create a pandas DataFrame for our data
# this provides many convenience functions
# for exploring your dataset
# need to reshape y so it is a 2D array with one column
df = pd.DataFrame(np.hstack((X, y.reshape(y.shape[0], -1))),
                  columns=branch_names+['y'])
"""
Draw histogram of the DataFrame's series comparing the distribution
in `data1` to `data2`.
grid : boolean, default True
Whether to show axis grid lines
xlabelsize : int, default None
If specified changes the x-axis label size
xrot : float, default None
rotation of x axis labels
ylabelsize : int, default None
If specified changes the y-axis label size
yrot : float, default None
rotation of y axis labels
Number of histogram bins to be used
kwds : other plotting keyword arguments
To be passed to hist function
"""
                    
class PlotFactory():
    def __init__ (data1, data2,features, grid=True,
                  xlabelsize=None, xrot=None, ylabelsize=None,
                  yrot=None, bins=10, **kwargs):
        self.data1 = data1
        self.data2 = data2 
        self.features = features
        self.xlabelsize = xlabelsize
        self.xrot = xrot
        self.ylabelsize = ylabelsize
        self.yrot
        self.bins = bins
        
    def compare_variables(self, cuts= None, **kwargs): 
        # data1: DataFrame
        # data2: DataFrame
        # column: string or sequence
        # If passed, will be used to limit data to a subset of columns
        
        if 'alpha' not in self.kwargs:
            kwargs['alpha'] = 0.5
            
        # if column is not None:
        #     if not isinstance(column, (list, np.ndarray, Index)):
        #         column = [column]
        #     data1 = data1[column]
        #     data2 = data2[column]
        
        if cuts != None:
            if passed_cut (evt, cuts)
            
        
        self.data1 = self.data1._get_numeric_data()
        self.data2 = self.data2._get_numeric_data()
        naxes = len(self.data1.columns)
            
        fig, axes = plotting._subplots(naxes=naxes, ax=ax, squeeze=False,
                                       sharex=sharex,
                                       sharey=sharey,
                                       figsize=figsize,
                                       layout=layout)
        _axes = plotting._flatten(axes)
 
        for i, col in enumerate(com._try_sort(self.data1.columns)):
            ax = _axes[i]
            low = min(data1[col].min(), data2[col].min())
            high = max(data1[col].max(), data2[col].max())
            ax.hist(data1[col].dropna().values,
                    bins=bins, range=(low,high), **kwds)
            ax.hist(data2[col].dropna().values,
                    bins=bins, range=(low,high), **kwds)
            ax.set_title(col)
            ax.grid(grid)
            
            plotting._set_ticks_props(axes, xlabelsize=xlabelsize, xrot=xrot,
                                      ylabelsize=ylabelsize, yrot=yrot)
            fig.subplots_adjust(wspace=0.3, hspace=0.7)
            
            return axes

