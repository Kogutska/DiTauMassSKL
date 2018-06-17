#!/usr/bin/env python2.7

import sys, os, re, gc, glob, argparse
import shutil, array, logging
from multiprocessing import Process    

# local 
import numpy as np
from ditaumassskl.parallel import run_pool
 
# Setup cmd args
parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='+', 
                    help='ntuples to append BDT score to them')
parser.add_argument('action',
                    help='remove, add branch or add tree',choices=['rm', 'ab', 'at', 'skim'])
parser.add_argument('--log', '-l', help='logging level', default='INFO')
parser.add_argument('--sys', action='store_true', help='include sys trees or not')
args = parser.parse_args() 

# setup ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

# # external C++ libs
# ext_funcs = ["/home/sbahrase/WorkDesk/HPlusTauNu/HPlusTauNuAnalysisCode/FakeFactors/CorrectUpsilon_1D_QCD.C",
#              "/home/sbahrase/WorkDesk/HPlusTauNu/HPlusTauNuAnalysisCode/FakeFactors/CorrectUpsilon_1D_WCR.C",
#              ]
# for f in ext_funcs :
#     ROOT.gROOT.ProcessLine(".L %s"%f)

#--# consts
#--#--------------------------------------------
log = logging.getLogger(os.path.basename(__file__))
log.setLevel(args.log.upper())

#--# put what you want here
Y_BRANCHES = [
    # "upsilon_smirnov_transform:=CorrectUpsilon_1D_WCR(2.0*tau_0_allTrk_pt/tau_0_pt-1, tau_0_n_tracks)",
    "n_jets_l1j25:=1",
    "HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo:=1",
    "ditau_tau0_HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo:=1",
    "ditau_tau1_HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo:=1",

    "theory_weights_nominal:=1",
    "jet_NOMINAL_central_jets_global_effSF_JVT:=1",
    "jet_NOMINAL_central_jets_global_ineffSF_JVT:=1",
    "ditau_tau0_sf_NOMINAL_TauEffSF_HLT_tau35_medium1_tracktwo_JETIDBDTTIGHT:=1",
    "ditau_tau1_sf_NOMINAL_TauEffSF_HLT_tau25_medium1_tracktwo_JETIDBDTTIGHT:=1",
    "jet_NOMINAL_forward_jets_global_effSF_JVT:=1",
    "jet_NOMINAL_forward_jets_global_ineffSF_JVT:=1",
    "ditau_tau0_sf_NOMINAL_TauEffSF_selection:=1",
    "ditau_tau1_sf_NOMINAL_TauEffSF_selection:=1",
    "ditau_tau0_sf_NOMINAL_TauEffSF_JetBDTtight:=1",
    "ditau_tau1_sf_NOMINAL_TauEffSF_JetBDTtight:=1",
    "NOMINAL_pileup_random_run_number:=200000",#random_run_number",
    "NOMINAL_pileup_combined_weight:=1"
    #"ditau_higgs_pt:=parent_pt"
    ]

RM_BRANCHES = [
    #"FastBDT*",
    "HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo",
    ]

SYSTEMATICS= [
    ("upsilon_up", "upsilon_smirnov_transform", "CorrectUpsilon_1D_QCD(2.0*tau_0_allTrk_pt/tau_0_pt-1, tau_0_n_tracks)"),
    ]

SELECTION = ""

#-----------------------------------------------
def get_trees(tfile):
    """
    Retrun a list of TTrees in a given root file.
    """
    trees = set()
    trees.add(tfile.Get('NOMINAL'))
    if args.sys:
        keys = [k.GetName() for k in tfile.GetListOfKeys()]
        keys = filter(lambda k: isinstance(tfile.Get(k), ROOT.TTree), keys)
        for k in keys:
            if k=='EventLoop_FileExecuted' or 'upsilon' in k:
                continue
            trees.add(tfile.Get(k))

    return trees

#-----------------------------------------------
def setup_branches(tree, branches):
    """setup output branches.
    """
    out_branches = dict()
    for branch in branches:
        if ':=' in branch:
            fname, tform = branch.split(':=')
            tform.strip()
            fname.strip()
            branch = branch.split(':=')[0]
        else:
            fname, tform = branch, branch
        
        # if  branch is already in tree do nothing.
        if branch in [b.GetName() for b in tree.GetListOfBranches()]:
            log.warning("%s is already in %s "%(branch, tree.GetName()))
            continue
        branch_val = array.array('i', [0])
        tbranch = tree.Branch(fname, branch_val, fname+"/I")
            
        # setup branch tfomula
        tform = ROOT.TTreeFormula(fname, tform, tree)
        tform.SetQuickLoad(True)
        out_branches[branch] = (branch_val, tform, tbranch)
    
    return out_branches
 
#-----------------------------------------------
def remove_branches(file_name, branches=RM_BRANCHES, **kwargs):
    """
    Remove the given list of branches from tree
    """
    tfile = ROOT.TFile.Open(file_name, "UPDATE")
    trees = get_trees(tfile)
    for tree in trees:
        for br in branches:
            tree.SetBranchStatus(br, 0)
        # copy_tree = tree.Clone()    
        # # now over-write tree with active branches only
        # entries = tree.GetEntries()
        # for it, entry in enumerate(tree):
        #     copy_tree.LoadTree(it)
        #     # Overwrite a branch value. This changes the value that will be written to
        #     # the new tree but leaves the value unchanged in the original tree on disk.
        #     # "entry" is actually the buffer, which is shared between both trees.
        #     copy_tree.Fill()
        tree.Write(tree.GetName(), ROOT.TObject.kOverwrite)
    tfile.Close()     

    return 

#-----------------------------------------------
def add_branches(file_name, 
                 branches=Y_BRANCHES,
                 **kwargs):
    
    tfile = ROOT.TFile.Open(file_name, "UPDATE")
    trees = get_trees(tfile)
    for tree in trees:
        print tree.GetName()
        # add corrected upsilon branches
        tbranches = setup_branches(tree, branches)
        nEntries = tree.GetEntries()

        # Loop over events in tree
        tree_name = tree.GetName()
        tree.SetCacheSize(32*2**20)
        tree.SetCacheLearnEntries()
        totalEntries = tree.GetEntries()
        blockSize = 2**16
        blocks = totalEntries/blockSize
        for _, tbranch in tbranches.iteritems():
            log.info('adding %s branch to %s tree'%(tbranch[2].GetName(), tree_name))
            tval, tform, tb = tbranch 
            for block in xrange(blocks+1):
                for entry in xrange(block*blockSize,
                                    min(totalEntries, (block+1)*blockSize)):
                    if (entry%10000==0):
                        log.info("Tree: {0}, Event: {1}/{2}".format(tree_name, entry+1, totalEntries))
                    tree.LoadTree(entry)
                    tval[0] = int(tform.EvalInstance())
                    tb.Fill()

        tree.Write(tree.GetName(), ROOT.TObject.kOverwrite)

    tfile.Close()
    return 


#-----------------------------------------------
def add_syst_trees(file_name, systematics=SYSTEMATICS, 
                   over_write=True, **kwargs):
    """
    Append systs to the ntuples, and then copy the nominal tree 
    with a different syst branch for the systematics.
    """
    tfile = ROOT.TFile.Open(file_name, "UPDATE")

    # add syst trees
    for sys in systematics:
        sysName, varName, varForm = sys[0], sys[1], sys[2]
        log.info("---- Adding %s SYST tree ----"%sysName)
        if sysName in [k.GetName() for k in tfile.GetListOfKeys()]:
            log.warning("%s SYST tree already exists in %s"%(sysName, file_name))
            if over_write:
                log.warning('over-writing existing tree')
                ROOT.gDirectory.Delete(sysName)
                tfile.Close()
                tfile = ROOT.TFile.Open(file_name, "UPDATE")
            else:
                continue

        nom_tree = tfile.NOMINAL
        syst_tree = nom_tree.CloneTree(0)
        syst_tree.SetName(sysName)
        syst_tree.SetTitle(sysName)

        # append branch with syst variation to syst tree
        form = ROOT.TTreeFormula(varName, varForm, nom_tree)
        form.SetQuickLoad(True)
        val = array.array('f', [0.])
        new_branch = syst_tree.Branch(varName, val, varName+"/F")

        nom_tree.SetCacheSize(32*2**20)
        nom_tree.SetCacheLearnEntries()
        totalEntries = nom_tree.GetEntries()
        blockSize = 2**16
        blocks = totalEntries/blockSize
        for block in xrange(blocks+1):
            for entry in xrange(block*blockSize,
                                min(totalEntries, (block+1)*blockSize)):
                if (entry%10000==0):
                    log.info("------->>>>------: {0}/{1}".format(entry+1, totalEntries))
                nom_tree.GetEntry(entry)
                val[0] = form.EvalInstance()
                new_branch.Fill()
                syst_tree.Fill()
        syst_tree.Write(sysName, ROOT.TObject.kOverwrite)
        
    tfile.Close()
    return 


#-----------------------------------------------
def skim_tree(file_name, **kwargs):
    """
    skim tree based on some selections.
    """
    tfile = ROOT.TFile.Open(file_name, "UPDATE")
    trees = get_trees(tfile)
    for tree in trees:
        ctree = tree.CloneTree(0)
        entries = tree.GetEntries()
        for i, event in enumerate(tree):
            if i%10000==0:
                print "---- %i/%i ----"%(i+1, entries)
            # -- # set the selections here 
            if (event.bsm_tj_dirty_jet > 0):
                continue
            if (event.tau_0_pt < 30000): 
                continue
            if (event.n_jets < 3):
                continue
            if (event.n_taus==0):
                continue
            if (event.tau_0_jet_bdt_score<0.5 and event.tau_0_jet_bdt_score_sig<0.01): 
                continue

            ctree.Fill()
        ctree.Write(tree.GetName(), ROOT.TObject.kOverwrite)

    tfile.Close()
    
    return

#-----------------------------------------------
def merge_tfiles(indir):
    """
    hadd all files in indir
    """
    for root, dirs, files in os.walk(indir):
        for d in dirs:
            files = glob.glob("%s/%s/user*.root*.nn"%(root, d))
            dest_file = os.path.join(root, d, "user.hbaluchb.%s.merged.NTUP.1017v01_hist.root"%d)
            print d
            print sorted(files)
            #subprocess.call("hadd %s %s"%(dest_file, " ".join(sorted(files))), shell=True) #<! hadd sucks, files should be ordered !
            print 70*"--"


    return 

#-----------------------------------------------
def merge_ext_trees(target_file, ext_files, 
                    tree_name="NOMINAL", hist_name="h_metadata"):
    """
    chain trees together.
    """
    
    



#-----------------------------------------------
# simple class for parallel processing
#-----------------------------------------------
class Job(Process):
    """
    simpel worker class for parallel
    processing. the run method is necessary,
    which will overload the run method of Procces.
    """
    
    def __init__(self, workfunc, input, **workfunc_args):
        super(Job, self).__init__()
        self.workfunc = workfunc
        self.input = input
        self.workfunc_args = workfunc_args
        self.copy_input = False
        if 'copy_input' in workfunc_args:
            self.copy_input = workfunc_args['copy_input']
        
    def run(self):
        input = self.input
        workfunc  = self.workfunc 
        workfunc_args = self.workfunc_args
        
        # copy to new file
        if self.copy_input:
            output = input+'.brt'
            if os.path.exists(output):
                log.warning(" {} already exists (will skip copying if file is in good shape)" .format(output))
                tf = ROOT.TFile.Open(output, 'READ')
                if not tf:
                    log.warning("{} exists but it ZOMBIE, replacing it".format(output))
                    os.remove(output)
                    shutil.copy(input, output)
            else:
                log.info("copying {0} to {1} ...".format(input, output))
                shutil.copy(input, output)
        else:
            output = input
        
        # the actual work happens here
        workfunc(output, **workfunc_args)
        return 

#------------------------------------------------------------------------------    
if __name__=='__main__':
    # whats's the input for workfunc
    if not args.files:
        raise IOError('input file pls?')
    dfiles = args.files
    # what's the work
    workfunc_args = dict()
    workfunc_args['copy_input']  = True
    if args.action=='rm':
        workfunc = remove_branches
        workfunc_args['branches'] = RM_BRANCHES
        
    elif args.action=='ab':
        workfunc = add_branches
        workfunc_args['branches'] = Y_BRANCHES
        
    elif args.action=='at':
        workfunc = add_syst_trees
        workfunc_args['systematics'] = SYSTEMATICS

    elif args.action=='skim':
        workfunc = skim_tree
    
    elif args.action=="merge-files":
        if not (args.indir):
            raise IOError("input dir pls?\n")
        workfunc = merge_tfiles
        
    
    else:
        raise Exception(" requested--- %s --- action is not supported"%args.action)
    
    # --# sort files based on size to start the heavier ones sooner.
    dfiles.sort(key=lambda f: os.path.getsize(f), reverse=True)
    jobs = [Job(workfunc, f, **workfunc_args) for f in dfiles]
    
    # --# run jobs
    run_pool(jobs, n_jobs=-1)

