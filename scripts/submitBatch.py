#! /usr/bin/env python
import PhysicsAnalysis.NanoAODAnalysis.BatchMaster as bm

import sys
# das_client -query="dataset=/SingleElectron/Run2016*-02Apr2020-v1/NANOAOD" # | wc -l
# python PhysicsAnalysis/NanoAODAnalysis/python/WBrAnalyzer.py localout ../../mc.root --year=2018 --isData=0 --max-entries=30000 
# python PhysicsAnalysis/NanoAODAnalysis/python/WBrAnalyzer.py localout ../../data.root --year=2018 --isData=1 --max-entries=30000 



# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch.sh'
analyzer   = 'WBrAnalyzer'
stage_dir  = 'batch'
output_dir = '/store/user/zchen/batchout'
location   = 'lpc'

nEvtPerJob = 4 # in unit of 1e6

# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}



#################################################
#                                               #
#---------------  Running data   ---------------#
#                                               #
#################################################
# dataset, nEvtPerJobIn1e6, year, isData, suffix


# Single Electron
samplesDict['2016_SingleElectron'] = [ 
    bm.JobConfig( '/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016B_ver2'),
    bm.JobConfig( '/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016C'),
    bm.JobConfig( '/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016D'),
    bm.JobConfig( '/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016E'),
    bm.JobConfig( '/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016F'),
    bm.JobConfig( '/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016G'),
    bm.JobConfig( '/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleElectronRun2016H')]

samplesDict['2017_SingleElectron'] = [ 
    bm.JobConfig( '/SingleElectron/Run2017B-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleElectronRun2017B'),
    bm.JobConfig( '/SingleElectron/Run2017C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleElectronRun2017C'),
    bm.JobConfig( '/SingleElectron/Run2017D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleElectronRun2017D'),
    bm.JobConfig( '/SingleElectron/Run2017E-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleElectronRun2017E'),
    bm.JobConfig( '/SingleElectron/Run2017F-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleElectronRun2017F')]

samplesDict['2018_SingleElectron'] = [
    bm.JobConfig( '/EGamma/Run2018A-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleElectronRun2018A'),
    bm.JobConfig( '/EGamma/Run2018B-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleElectronRun2018B'),
    bm.JobConfig( '/EGamma/Run2018C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleElectronRun2018C'),
    bm.JobConfig( '/EGamma/Run2018D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleElectronRun2018D')]



# Single Muon
samplesDict['2016_SingleMuon'] = [ 
    bm.JobConfig( '/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016B_ver2'),
    bm.JobConfig( '/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016C'),
    bm.JobConfig( '/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016D'),
    bm.JobConfig( '/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016E'),
    bm.JobConfig( '/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016F'),
    bm.JobConfig( '/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016G'),
    bm.JobConfig( '/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD', nEvtPerJob, "2016", 1, '2016_SingleMuonRun2016H')]

samplesDict['2017_SingleMuon'] = [ 
    bm.JobConfig( '/SingleMuon/Run2017B-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleMuonRun2017B'),
    bm.JobConfig( '/SingleMuon/Run2017C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleMuonRun2017C'),
    bm.JobConfig( '/SingleMuon/Run2017D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleMuonRun2017D'),
    bm.JobConfig( '/SingleMuon/Run2017E-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleMuonRun2017E'),
    bm.JobConfig( '/SingleMuon/Run2017F-02Apr2020-v1/NANOAOD', nEvtPerJob, "2017", 1, '2017_SingleMuonRun2017F')]

samplesDict['2018_SingleMuon'] = [
    bm.JobConfig( '/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleMuonRun2018A'),
    bm.JobConfig( '/SingleMuon/Run2018B-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleMuonRun2018B'),
    bm.JobConfig( '/SingleMuon/Run2018C-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleMuonRun2018C'),
    bm.JobConfig( '/SingleMuon/Run2018D-02Apr2020-v1/NANOAOD', nEvtPerJob, "2018", 1, '2018_SingleMuonRun2018D')]





#################################################
#                                               #
#--------------- Running 2016 MC ---------------#
#                                               #
#################################################
# top
samplesDict['2016_top'] = [
    # leptonic tt  
    bm.JobConfig( 
    dataset='/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_TTTo2L2Nu'),

    # semilep tt 
    bm.JobConfig( 
    dataset='/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_TTToSemiLeptonic'),

    # hadronic tt  
    bm.JobConfig( 
    dataset='/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_TTToHadronic'),

    # tW top 
    bm.JobConfig( 
    dataset='/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_STtWTop'),

    # tW antitop 
    bm.JobConfig(
    dataset='/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_STtWAntiTop'),
]

# w
samplesDict['2016_w'] = [
    # wjets inclusive
    bm.JobConfig( 
    dataset='/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_WJets'),
]

# z
samplesDict['2016_z'] = [
    # zjets inclusive
    bm.JobConfig(
    dataset='/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=0, suffix='2016_ZJets'),
]


#################################################
#                                               #
#--------------- Running 2017 MC ---------------#
#                                               #
#################################################
# top
samplesDict['2017_top'] = [
    # leptonic tt 
    bm.JobConfig( 
    dataset='/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_TTTo2L2Nu'),

    # semilep tt 
    bm.JobConfig( 
    dataset='/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_TTToSemiLeptonic'),

    # hadronic tt
    bm.JobConfig( 
    dataset='/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_TTToHadronic'),

    # tW top
    bm.JobConfig( 
    dataset='/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_STtWTop'),
    
    # tW antitop
    bm.JobConfig( 
    dataset='/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_STtWAntiTop'),
]

# w
samplesDict['2017_w'] = [
    # wjets inclusive
    bm.JobConfig( 
    dataset='/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_WJets'),
]


# z
samplesDict['2017_z'] = [
    # zjets inclusive
    bm.JobConfig( 
    dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM',
    nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=0, suffix='2017_ZJets'),
]


#################################################
#                                               #
#--------------- Running 2018 MC ---------------#
#                                               #
#################################################
# top
samplesDict['2018_top'] = [
    # leptonic tt 
    bm.JobConfig( 
        dataset='/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',         
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_TTTo2L2Nu'),
    
    # semilep tt
    bm.JobConfig( 
    dataset='/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_TTToSemiLeptonic'),
    
    # hadronic tt
    bm.JobConfig( 
    dataset='/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',         
    nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_TTToHadronic'),        
    
    # tW top 
    bm.JobConfig( 
        dataset='/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM',         
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_STtWTop'),   
    # tW antitop
    bm.JobConfig( 
        dataset='/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM',         
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_STtWAntiTop'),        
]

# w
samplesDict['2018_w'] = [
    # wjets inclusive
    bm.JobConfig( 
        dataset='/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_WJets'),
]


# z
samplesDict['2018_z'] = [
    # zjets inclusive
    bm.JobConfig( 
        dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=0, suffix='2018_ZJets'),
]


# -----------------------------
# submit to batch
# -----------------------------
samplesToSubmit = samplesDict.keys()

configs = []
for s in samplesToSubmit:
    if s[:4] in ["2016","2017","2018"]:
        configs += samplesDict[s]

batchMaster = bm.BatchMaster(
    analyzer    = analyzer,
    config_list = configs, 
    stage_dir   = stage_dir,
    output_dir  = output_dir,
    executable  = executable,
    location    = location
)

batchMaster.submit_to_batch(doSubmit=True)




# # vv
# samplesDict['2016_vv'] = [
#     bm.JobConfig( 
#         dataset='/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2016", isData=False, suffix='2016_WWTo2L2Nu'),

#     bm.JobConfig( 
#         dataset='/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2016", isData=False, suffix='2016_WZ'),
# ]

# # vv
# samplesDict['2017_vv'] = [
#     bm.JobConfig( 
#         dataset='/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2017", isData=False, suffix='2017_WWTo2L2Nu'),

#     bm.JobConfig( 
#         dataset='/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2017", isData=False, suffix='2017_WZ'),
# ]



# # vv
# samplesDict['2016_vv'] = [
#     bm.JobConfig( 
#         dataset='/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2016", isData=False, suffix='2016_WWTo2L2Nu'),

#     bm.JobConfig( 
#         dataset='/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM',
#         nEvtPerJobIn1e6=10, year="2016", isData=False, suffix='2016_WZ'),
# ]



# samplesDict['2017_SingleElectron'] = [ # 46, 117, 32, 66, 104 nanoaod files



# nanov = "02Apr2020-v1"

# # Single Electron
# samplesDict['2016_SingleElectron'] = [ #  43, 99, 62, 54, 95, 101 nanoaod files 
#     bm.JobConfig( '/SingleElectron/Run2016{}-{}/NANOAOD'.format(era,nanov), 30, "2016", True, '2016_SingleElectronRun2016{}'.format(era)) for era,nj in z) ]
# samplesDict['2017_SingleElectron'] = [ # 46, 117, 32, 66, 104 nanoaod files
#     bm.JobConfig( '/SingleElectron/Run2017{}-{}/NANOAOD'.format(era,nanov), 30, "2017", True, '2017_SingleElectronRun2017{}'.format(era)) for era,nj in zip("BCDEF",[10,20,10,10,20]) ]
# samplesDict['2018_SingleElectron'] = [ # 255, 100, 112, 479 nanoaod files
#     bm.JobConfig( '/EGamma/Run2018{}-{}/NANOAOD'.format(era,nanov), 40, "2018", True, '2018_SingleElectronRun2018{}'.format(era)) for era in "ABC" ] + [
#     bm.JobConfig( '/EGamma/Run2018{}-{}/NANOAOD'.format(era,nanov), 60, "2018", True, '2018_SingleElectronRun2018{}'.format(era)) for era in "D" ]
 
