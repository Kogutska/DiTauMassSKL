# python imports
import os
import pickle

#sklearn imports
from sklearn.tree import (DecisionTreeRegressor,
                          ExtraTreeRegressor,
                          export_graphviz
                          )
from sklearn.ensemble import (AdaBoostRegressor,
                              BaggingRegressor,
                              ExtraTreesRegressor,
                              GradientBoostingRegressor, 
                              RandomForestRegressor
                              )
## local imports
from . import log

class Regressor():
    """
    """
    def __init__(self,
                 output_name = '',
                 ):
        self.output = output_name

    def book_base_clf (self, base_name = 'DecisionTreeRegressor', **params):
        """
        base classifier 
        """
        if base_name != "DecisionTreeRegressor":
            raise Exception ("Not Implemented Yet")
        
        if "criterion" not in params:               params["criterion"] = "mse"
        if "splitter" not in params:                params["splitter"] = "best"
        if "max_features" not in params:            params["max_features"] = None
        if "min_samples_split" not in params:       params["min_samples_split"] = 2
        if "min_samples_leaf" not in params:        params["min_samples_leaf"] =200
        if "min_weight_fraction_leaf" not in params:params["min_weight_fraction_leaf"] =  0.02
        if "max_features" not in params:            params["max_features"] = 'auto'
        if "max_leaf_nodes" not in params:          params["max_leaf_nodes"] = None
        if "random_state" not in params:            params["random_state"] = None
        if "presort" not in params :                params["presort"] = 'auto'
        base_clf = DecisionTreeRegressor(**params)
        return base_clf
        
    def book_meta_clf(self,meta_name = '', **params):
        """
        Book the meta clf (set all the parameters)
        """
        if meta_name == "AdaBoostRegressor":
            if "base_estimator" not in params:          params["base_estimator"]=self.book_base_clf(base_name="DecisionTreeRegressor")       
            if "n_estimators" not in params :           params["n_estimators"] = 100
            if "learning_rate" not in params :          params["learning_rate"] = 1.
            if "loss" not in params :                   params["loss"] = "square" # {'linear,square,exponential}
            if "random_state" not in params :           params["random_state"] = None
            clf = AdaBoostRegressor (**params)
            
        if meta_name == "BaggingRegressor":
            if "base_estimator" not in params:          params["base_estimator"]=self.base_clf()
            if "n_estimators" not in params:            params["n_estimators"] = 50
            if "max_samples" not in params:             params["max_samples"] = 1.
            if "max_features" not in params:            params["max_features"] = 1.

            if "bootstrap" not in params:               params["bootstrap"] = True
            if "bootstrap_features" not in params:      params["bootstrap_features"] = False
            if "oob_score" not in params:               params["oob_score"] = False
            if "warm_start" not in params:              params["warm_start"] = False
            if "n_jobs" not in params:                  params["n_jobs"] = 20
            if "random_state" not in params:            params["random_state"] = None
            if "verbose" not in params:                 params["verbose"] = 1
            clf = BaggingRegressor(**params)

        if meta_name == "ExtraTreesRegressor":
            if "n_estimators" not in params:            params["n_estimators"] = 200
            if "min_samples_split" not in params:       params["min_samples_split"] = 2
            if "min_samples_leaf" not in params:        params["min_samples_leaf"] = 200
            if "min_weight_fraction_leaf" not in params:params["min_weight_fraction_leaf"] =  0.02
            if "max_features" not in params:            params["max_features"] = 'auto'
            if "max_leaf_nodes" not in params:          params["max_leaf_nodes"] = None

            if "bootstrap" not in params:               params["bootstrap"] = False
            if "oob_score" not in params:               params["oob_score"] = False
            if "warm_start" not in params:              params["warm_start"] = False
            if "n_jobs" not in params:                  params["n_jobs"] = 20
            if "random_state" not in params:            params["random_state"] = None
            if "verbose" not in params:                 params["verbose"] = 1
            clf = ExtraTreesRegressor(**params)

        if meta_name == "RandomForestRegressor":
            if "n_estimators" not in params:            params["n_estimators"] = 100
            if "min_samples_split" not in params:       params["min_samples_split"] = 2
            if "min_samples_leaf" not in params:        params["min_samples_leaf"] = 200
            if "min_weight_fraction_leaf" not in params:params["min_weight_fraction_leaf"] =  0.02
            if "max_features" not in params:            params["max_features"] = 'auto'
            if "max_leaf_nodes" not in params:          params["max_leaf_nodes"] = None

            if "bootstrap" not in params:               params["bootstrap"] = True
            if "oob_score" not in params:               params["oob_score"] = False
            if "warm_start" not in params:              params["warm_start"] = False
            if "n_jobs" not in params:                  params["n_jobs"] = 20
            if "random_state" not in params:            params["random_state"] = None
            if "verbose" not in params:                 params["verbose"] = 1
            clf = RandomForestRegressor(**params)


        if meta_name == "GradientBoostingRegressor":
            if "n_estimators" not in params:            params["n_estimators"] = 100
            if "learning_rate" not in params :          params["learning_rate"] = 1.
            if "loss" not in params :                   params["loss"] = "huber" # linear, square, exponential

            if "min_samples_split" not in params:       params["min_samples_split"] = 2
            if "min_samples_leaf" not in params:        params["min_samples_leaf"] = 200
            if "min_weight_fraction_leaf" not in params:params["min_weight_fraction_leaf"] =  0.02
            if "max_features" not in params:            params["max_features"] = 'auto'
            if "max_leaf_nodes" not in params:          params["max_leaf_nodes"] = None

            if "warm_start" not in params:              params["warm_start"] = False
            if "random_state" not in params:            params["random_state"] = None
            if "verbose" not in params:                 params["verbose"] = 1

            if "alpha" not in params :                  params["alpha"] = 0.9
            if "init" not in params :                   params["init"] = None
            if "presort" not in params :                params["presort"] = 'auto'

            clf = GradientBoostingRegressor (**params)
            
        log.info(params)
        return clf
                
    def train(self, data,features, target, meta_clf ,**kwargs):
        log.info("Training BRT ... ")
        ## get a sub sample of the original sample
        #sub_data= data.sample(frac=0.01, random_state=1)

        ## select specific columns (features/targets)
        train_data=data.reindex(columns=features)
        
        ## be careful target should be of size (train_sample size, )
        ## first convert dataframe object to numpy array then flatten it
        target_data= data.reindex(columns=target).as_matrix().ravel()

        ## print DataFrame object's shape to make sure it's right for the training
        regressor = meta_clf.fit(train_data, target_data)
        return regressor
    
    
