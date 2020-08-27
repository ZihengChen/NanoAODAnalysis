import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object

from PhysicsAnalysis.NanoAODAnalysis.WBrSelectionHelper import get_config


class WBrSelection(Module):
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
        self.out.branch("b_channel",  "I")
        self.out.branch("b_multiplicity_electrons", "I")
        self.out.branch("b_multiplicity_muons", "I")
        self.out.branch("b_multiplicity_taus", "I")
        self.out.branch("b_multiplicity_jets", "I")
        self.out.branch("b_multiplicity_bjets", "I")
        self.out.branch("b_dilepton_m", "F")

        self.add_branch_object("b_leptonOne") # p4, relIso, pdgId
        self.add_branch_object("b_leptonTwo") # p4, relIso, pdgId



    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
        

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        self.event = event

        # HLT
        passTrigger = self.check_hlt()
        if not passTrigger: 
            return False

        # muon loop
        self.loop_over_muons()
        # electron loop
        self.loop_over_electrons()
        # tau loop
        self.loop_over_taus()
        # jet loop
        self.loop_over_jets()

        # event selection
        eventSelected = self.event_selection()

        # return selected = true or false
        return eventSelected


    # -----------------------------
    # object selection
    # -----------------------------
    # HLT
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


    # muons
    def loop_over_muons(self):
        self.muons = []
        for mu in Collection(self.event,"Muon"):
            # apply cut
            if mu.pt>10 and abs(mu.eta)<2.4 and mu.tightId and mu.pfRelIso03_all < 0.15:
                self.muons.append(mu)

    # electrons
    def loop_over_electrons(self):
        self.electrons = []
        for el in Collection(self.event,"Electron"):
            # apply cut
            if el.pt>20 and abs(el.eta)<2.5 and el.cutBased>=4 and el.pfRelIso03_all < 0.0588:
                self.electrons.append(el)

    # taus
    def loop_over_taus(self):
        self.taus = []
        for tau in Collection(self.event,"Tau"):
            # check overlap with passing muon
            muOverlap = any([tau.DeltaR(mu) < 0.3 for mu in self.muons])
            # check overlap with passing electon
            elOverlap = any([tau.DeltaR(el) < 0.3 for el in self.electrons])


            # apply cut
            # receipe for deep2017v2p1 # all WP is tight
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDRecommendationForRun2
            if tau.pt>20 and abs(tau.eta)<2.3 \
                and (not muOverlap) and (not elOverlap) \
                and tau.idDecayModeNewDMs \
                and tau.idDeepTau2017v2p1VSe>=32 \
                and tau.idDeepTau2017v2p1VSjet>=32 \
                and tau.idDeepTau2017v2p1VSmu>=8 \
                :
                self.taus.append(tau)

    # jets
    def loop_over_jets(self):
        self.jets  = []
        self.bjets = []
        for jet in Collection(self.event,"Jet"):
            # check overlap with passing muon
            muOverlap = any([jet.DeltaR(mu) < 0.4 for mu in self.muons])
            # check overlap with passing electon
            elOverlap = any([jet.DeltaR(el) < 0.4 for el in self.electrons])
            # check overlap with passing tau
            tauOverlap = any([jet.DeltaR(tau) < 0.4 for tau in self.taus])

            # apply cut
            if jet.pt>30 and abs(jet.eta)<2.4 and jet.jetId >= 2 and (not muOverlap) and (not elOverlap) and (not tauOverlap):
                self.jets.append(jet)
                # count btag
                # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation#Recommendation_for_13_TeV_Data
                if jet.btagDeepB > self.cfg["cutDeepCSVM"]:
                    self.bjets.append(jet)






    # -----------------------------
    # event selection
    # -----------------------------
    def event_selection(self):
        # return bool eventSelected

        self.channel = 0

        # MARK: mumu
        if len(self.muons) == 2 and len(self.electrons) == 0 and len(self.taus) == 0:
            
            # hlt cut
            if not ( self.passMuTrigger ): return False
            # lepton pt cut
            if not (self.muons[0].pt>self.cfg["cutMu1Pt"] and self.muons[1].pt>self.cfg["cutMu2Pt"] ): return False
            # oppo sign cut
            if self.muons[0].charge * self.muons[1].charge > 0: return False
            # nJets cut
            if len(self.jets)<2: return False

            # # z-veto cut
            self.dileptonMass = (self.muons[0].p4()+self.muons[1].p4()).M()
            # if 80<self.dileptonMass <100: return False
            
            # fill Channel
            self.channel = 1
            self.fill_branch_object("b_leptonOne", p4=self.muons[0].p4(), pdgId=self.muons[0].charge*13, relIso=self.muons[0].pfRelIso03_all )
            self.fill_branch_object("b_leptonTwo", p4=self.muons[1].p4(), pdgId=self.muons[1].charge*13, relIso=self.muons[1].pfRelIso03_all ) 
            

    
        # MARK: ee
        elif len(self.electrons) == 2 and len(self.muons) == 0 and len(self.taus) == 0:

            # hlt cut
            if not (self.passElTrigger): return False 
            # lepton pt cut
            if not (self.electrons[0].pt>self.cfg["cutEl1Pt"] and self.electrons[1].pt>self.cfg["cutEl2Pt"] ): return False
            # oppo sign cut
            if self.electrons[0].charge * self.electrons[1].charge > 0: return False
            # nJets cut
            if len(self.jets)<2: return False
            # # z-veto cut
            self.dileptonMass = (self.electrons[0].p4()+self.electrons[1].p4()).M()
            # if 80<self.dileptonMass<100: return False
                
            # fill Channel
            self.channel = 2
            self.fill_branch_object("b_leptonOne", p4=self.electrons[0].p4(), pdgId=self.electrons[0].charge*11, relIso=self.electrons[0].pfRelIso03_all )
            self.fill_branch_object("b_leptonTwo", p4=self.electrons[1].p4(), pdgId=self.electrons[1].charge*11, relIso=self.electrons[1].pfRelIso03_all )

        # MARK: emu
        elif len(self.electrons) == 1 and len(self.muons) == 1 and len(self.taus) == 0:
            hltTest1 = self.passMuTrigger and self.muons[0].pt>self.cfg["cutMu1Pt"] and self.electrons[0].pt>self.cfg["cutEl2Pt"] 
            hltTest2 = self.passElTrigger and self.electrons[0].pt>self.cfg["cutEl1Pt"] and self.muons[0].pt>self.cfg["cutMu2Pt"] 

            # hlt cut
            if not (hltTest1 | hltTest2): return False 
            # oppo sign cut
            if self.muons[0].charge * self.electrons[0].charge > 0: return False
            # nJets cut
            if len(self.jets)<2: return False

            self.dileptonMass = (self.muons[0].p4()+self.electrons[0].p4()).M()

            # fill Channel
            self.channel = 3
            self.fill_branch_object("b_leptonOne", p4=self.muons[0].p4(), pdgId=self.muons[0].charge*13, relIso=self.muons[0].pfRelIso03_all )
            self.fill_branch_object("b_leptonTwo", p4=self.electrons[0].p4(), pdgId=self.electrons[0].charge*11, relIso=self.electrons[0].pfRelIso03_all )

        # MARK: mutau
        elif len(self.electrons) == 0 and len(self.muons) == 1 and len(self.taus) == 1:
            # hlt cut
            if not self.passMuTrigger: return False
            # lepton pt cut
            if self.muons[0].pt<self.cfg["cutMu1Pt"]: return False
            # oppo sign cut
            if self.muons[0].charge * self.taus[0].charge > 0: return False
            # nJets cut
            if len(self.jets)<2: return False

            self.dileptonMass = (self.muons[0].p4()+self.taus[0].p4()).M()

            # fill Channel
            self.channel = 5
            self.fill_branch_object("b_leptonOne", p4=self.muons[0].p4(), pdgId=self.muons[0].charge*13, relIso=self.muons[0].pfRelIso03_all )
            self.fill_branch_object("b_leptonTwo", p4=self.taus[0].p4(), pdgId=self.taus[0].charge*15, relIso=(self.taus[0].rawIsodR03/self.taus[0].pt) )

        # MARK: etau
        elif len(self.electrons) == 1 and len(self.muons) == 0 and len(self.taus) == 1:
            # hlt cut
            if not self.passElTrigger: return False
            # lepton pt cut
            if self.electrons[0].pt<self.cfg["cutEl1Pt"]: return False
            # oppo sign cut
            if self.electrons[0].charge * self.taus[0].charge > 0: return False
            # nJets cut
            if len(self.jets)<2: return False

            self.dileptonMass = (self.electrons[0].p4()+self.taus[0].p4()).M()

            # fill Channel
            self.channel = 9
            self.fill_branch_object("b_leptonOne", p4=self.electrons[0].p4(), pdgId=self.electrons[0].charge*11, relIso=self.electrons[0].pfRelIso03_all )
            self.fill_branch_object("b_leptonTwo", p4=self.taus[0].p4(), pdgId=self.taus[0].charge*15, relIso=(self.taus[0].rawIsodR03/self.taus[0].pt) )


        # MARK: not selected
        else:
            return False

        # only passed event come here
        # print self.passElTrigger, self.passMuTrigger
        # fill event info and return
        self.out.fillBranch("b_channel", self.channel)
        self.out.fillBranch("b_multiplicity_electrons", len(self.electrons) )
        self.out.fillBranch("b_multiplicity_muons", len(self.muons))
        self.out.fillBranch("b_multiplicity_taus", len(self.taus))
        self.out.fillBranch("b_multiplicity_jets", len(self.jets))
        self.out.fillBranch("b_multiplicity_bjets", len(self.bjets))

        self.out.fillBranch("b_dilepton_m", self.dileptonMass )
        return True



    # -----------------------------
    # helper methods
    # -----------------------------
    def fill_branch_object(self, objName, p4, pdgId, relIso):
        self.out.fillBranch(objName+"_pt", p4.Pt())
        self.out.fillBranch(objName+"_eta", p4.Eta())
        self.out.fillBranch(objName+"_phi", p4.Phi())
        self.out.fillBranch(objName+"_m", p4.M())
        self.out.fillBranch(objName+"_pdgId", pdgId)
        self.out.fillBranch(objName+"_relIso", relIso)
    
    def add_branch_object(self, objName):
        self.out.branch(objName+"_pt",   "F")
        self.out.branch(objName+"_eta",  "F")
        self.out.branch(objName+"_phi",  "F")
        self.out.branch(objName+"_m",    "F")
        self.out.branch(objName+"_pdgId", "I")
        self.out.branch(objName+"_relIso", "F")


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

WBrSelectionModule = lambda year, isData : WBrSelection(year, isData) 

