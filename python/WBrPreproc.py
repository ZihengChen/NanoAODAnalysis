import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object

from PhysicsAnalysis.NanoAODAnalysis.WBrSelectionHelper import get_config


class WBrPreproc(Module):
    def __init__(self, year, isData):
        self.year = year
        self.isData = isData
        self.cfg = get_config(year, isData)
        pass 


    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        # event info

        self.out.branch("b_passMuTrigger",  "O")
        self.out.branch("b_passElTrigger",  "O")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
        

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        self.event = event

        # if self.event.nJet <= 1:
        #     return False

        # HLT
        passTrigger = self.check_hlt()
        if not passTrigger: 
            return False
        
        # fill
        self.out.fillBranch("b_passMuTrigger", self.passMuTrigger)
        self.out.fillBranch("b_passElTrigger", self.passElTrigger)
        return True




    def check_hlt(self):
        HLT =  Object(self.event, "HLT")

        passTrigger = False

        # muon trigger
        self.passMuTrigger = eval("HLT.{}".format(self.cfg["muTrg"]))
        passTrigger |= self.passMuTrigger

        # electron trigger
        self.passElTrigger = eval("HLT.{}".format(self.cfg["elTrg"]))
        passTrigger |= self.passElTrigger

        return passTrigger



# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

WBrPreprocModule = lambda year, isData : WBrPreproc(year, isData) 


