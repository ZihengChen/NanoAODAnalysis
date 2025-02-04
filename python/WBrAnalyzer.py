#!/usr/bin/env python

import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import countHistogramsModule
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetRecalib import *

# constomized analysis modules
from PhysicsAnalysis.NanoAODAnalysis.WBrSelection import WBrSelectionModule
from PhysicsAnalysis.NanoAODAnalysis.WBrPreproc import WBrPreprocModule



def get_lumi_json(year, isData):
    
    if isData:
        if year == "2016":
            jsonInput = "PhysicsAnalysis/NanoAODAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
        elif year == "2017":
            jsonInput = "PhysicsAnalysis/NanoAODAnalysis/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"
        elif year == "2018":
            jsonInput = "PhysicsAnalysis/NanoAODAnalysis/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
        
        print "use lumin mask: " + jsonInput
    else:
        jsonInput = None
        print "no json lumin mask is needed for MC."

    return jsonInput

def handle_list_of_input_files(inputFiles):
    inputFilesFull = []

    for f in inputFiles:
        sufix = f.split(".")[-1]
        # handle root file. do no thing
        if sufix == "root":
            inputFilesFull.append(f)
        # handle txt files which contains names of root file
        elif sufix == "txt":
            ftxt = open(f)
            inputFiles = ftxt.readlines()
            inputFiles = [ inputFile.strip() for inputFile in inputFiles ]
            ftxt.close()
            inputFilesFull += inputFiles
        
    return inputFilesFull



if __name__ == "__main__":


    #-----------------------------------------------
    # parsing arg and option
    #-----------------------------------------------
    from optparse import OptionParser
    parser = OptionParser(usage=''' 
        %prog [options] outputDir inputFiles. where inputFiles can be 'nanoaod1.root nanoaod2.root' or 'input.txt'
        e.g.  python PhysicsAnalysis/NanoAODAnalysis/python/WBrAnalyzer.py localout test/inputMC.txt --postfix=0 --year=2018 --isData=0 --max-entries=1000 ''')
    
    parser.add_option("-s", "--postfix",dest="postfix", type="string", default=None, help="Postfix which will be appended to the file name (default: _Friend for friends, _Skim for skims)")
    parser.add_option("--year", dest="year", type="string", default="2016", help="which year of the dataset (defalt: 2016)")
    parser.add_option("--isData", dest="isData", type="int", default=1, help="whether DATA or MC (defalt is 1) is data")
    parser.add_option("-N", "--max-entries", dest="maxEntries", type="long",  default=None, help="max n event per file(default is None, all events in tree)")

    (options, args) = parser.parse_args()

    # get inputs and outDir from args
    if len(args) < 2: parser.print_help(); sys.exit(1)
    outdir, inputFiles = args[0], args[1:]


    #-----------------------------------------------
    # set analyzer process
    #-----------------------------------------------
    # setup modules
    modules = []
    # counting ngen
    modules.append( countHistogramsModule() )
    # pre processing
    modules.append(WBrPreprocModule(options.year, options.isData) )
    
    if not options.isData:
        # btag reweighting
        eval("modules.append( btagSF_deepcsvM_{}())".format(options.year))


    # my selection
    modules.append( WBrSelectionModule(options.year, options.isData)  )
 

    if not options.isData:
        # pu reweighting
        eval("modules.append( puAutoWeight_{}())".format(options.year))
        # prefiring reweighting
        if options.year in ["2016","2017"]:
            eval("modules.append( PrefCorr{}())".format(options.year))
    

    print("{} modules will be applied".format(len(modules)))
    
    # make list of inputFiles for .txt
    inputFilesFull = handle_list_of_input_files(inputFiles)

    # setup json:
    jsonInput = get_lumi_json(options.year, options.isData)        

    # outputbranchsel
    outputbranchsel = "PhysicsAnalysis/NanoAODAnalysis/scripts/keep_and_drop_output.txt"
    print "use file for keep and drop features: " + outputbranchsel

    # run analyzer
    p=PostProcessor(
        outdir, inputFilesFull, 
        modules    = modules,
        jsonInput  = jsonInput,
        maxEntries = options.maxEntries,
        outputbranchsel = outputbranchsel,
        postfix = options.postfix
    )
    p.run()