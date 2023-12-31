from Gaudi.Configuration import *



path = "/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/"
files = [path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00002.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00003.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00004.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00005.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00006.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00007.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00008.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00009.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00010.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00011.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00012.root"]

from Configurables import k4DataSvc
from Configurables import MarlinProcessorWrapper, EDM4hep2LcioTool, Lcio2EDM4hepTool

evtSvc = k4DataSvc('EventDataSvc')
# muons:
#evtSvc.input = '/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.root'
evtSvc.inputs = files
# hadrons:
#evtSvc.input = '/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/Dirac-Dst-E250-qqh_zz_4n.eR.pL-00001.root'
# example file:
#evtSvc.input = '/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/rv02-02.sv02-02.mILD_l5_o1_v02.E250-SetA.I402003.Pe2e2h.eL.pR.n000.d_dstm_15089_0_edm4hep.root'

from Configurables import PodioInput
input = PodioInput("InputReader")
input.collections = ["PandoraPFOs", "PrimaryVertex", "PandoraClusters", "MarlinTrkTracks"]

from Configurables import LcioEvent
lcio_read = LcioEvent()
lcio_read.OutputLevel = DEBUG
lcio_read.Files = ["/eos/experiment/clicdp/grid/ilc/user/t/tjunping/data/slcio/E250_overlay/Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.slcio"]


from Configurables import HtoInvAlg
myalg = HtoInvAlg()
myalg.RecoParticleColl = 'PandoraPFOs'
myalg.IsolatedLeptonsColl = 'IsolatedLeptons'
#myalg.MuonColl = 'Muons'
myalg.OutputLevel = INFO


# Isolated Lepton Processor

MyIsolatedLeptonTaggingProcessor = MarlinProcessorWrapper("MyIsolatedLeptonTaggingProcessor")
MyIsolatedLeptonTaggingProcessor.OutputLevel = DEBUG
MyIsolatedLeptonTaggingProcessor.ProcessorType = "IsolatedLeptonTaggingProcessor"
MyIsolatedLeptonTaggingProcessor.Parameters = {
                                               "CosConeLarge": ["0.95"],
                                               "CosConeSmall": ["0.98"],
                                               "CutOnTheISOElectronMVA": ["2.0"],
                                               "CutOnTheISOMuonMVA": ["0.7"],
                                               "DirOfISOElectronWeights": ["/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-03/MarlinReco/v01-32/Analysis/IsolatedLeptonTagging/example/isolated_electron_weights"],
                                               "DirOfISOMuonWeights": ["/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-03/MarlinReco/v01-32/Analysis/IsolatedLeptonTagging/example/isolated_muon_weights_woYoke"],
                                               "InputPandoraPFOsCollection": ["PandoraPFOs"],
                                               "InputPrimaryVertexCollection": ["PrimaryVertex"],
                                               "IsSelectingOneIsoLep": ["false"],
                                               "MaxD0SigForElectron": ["50"],
                                               "MaxD0SigForMuon": ["20"],
                                               "MaxEOverPForElectron": ["1.3"],
                                               "MaxEOverPForMuon": ["0.3"],
                                               "MaxZ0SigForElectron": ["50"],
                                               "MaxZ0SigForMuon": ["20"],
                                               "MinEOverPForElectron": ["0.5"],
                                               "MinEecalOverTotEForElectron": ["0.9"],
                                               "MinEyokeForMuon": ["1.2"],
                                               "MinPForElectron": ["5"],
                                               "MinPForMuon": ["5"],
                                               "OutputIsoLeptonsCollection": ["IsolatedLeptons"],
                                               "OutputPFOsWithoutIsoLepCollection": ["PandoraPFOsWithoutIsoLep"],
                                               "UseYokeForMuonID": ["false"]
                                               }




edm4hep2LcioConv = EDM4hep2LcioTool("EDM4hep2Lcio")
lcio2edm4hepConv = Lcio2EDM4hepTool("Lcio2EDM4hep")
edm4hep2LcioConv.convertAll = False
edm4hep2LcioConv.collNameMapping = {
        'PrimaryVertex':                   'PrimaryVertex',
        'PandoraPFOs':                     'PandoraPFOs',
        "PandoraClusters": "PandoraClusters",
        "MarlinTrkTracks": "MarlinTrkTracks"
      }


lcio2edm4hepConv.convertAll = False
lcio2edm4hepConv.collNameMapping = {
     'PandoraPFOs': 'PandoraPFOs',
     'IsolatedLeptons': 'IsolatedLeptons',
     'PandoraPFOsWithoutIsoLep': 'PandoraPFOsWithoutIsoLep',
     "PandoraClusters": "PandoraClusters",
     "MarlinTrkTracks": "MarlinTrkTracks"
     }




MyIsolatedLeptonTaggingProcessor.EDM4hep2LcioTool = edm4hep2LcioConv
MyIsolatedLeptonTaggingProcessor.Lcio2EDM4hepTool = lcio2edm4hepConv



# Lepton Pairing Processor
from Configurables import LeptonPairingAlg

MyLeptonPairing = LeptonPairingAlg()
MyLeptonPairing.RecoParticleColl = 'PandoraPFOs'
MyLeptonPairing.IsolatedLeptonsColl = 'IsolatedLeptons'
MyLeptonPairing.PFOsWOIsoLepColl = 'PandoraPFOsWithoutIsoLep'
MyLeptonPairing.doPhotonRecovery = True
MyLeptonPairing.diLeptinInvariantMass = 91.1876




from Configurables import PodioOutput
output = PodioOutput('output')
output.filename = 'tst.root'


from Configurables import ApplicationMgr
ApplicationMgr( TopAlg=[input, MyIsolatedLeptonTaggingProcessor, MyLeptonPairing, myalg, output],
                EvtSel="NONE",
                EvtMax=50,
		ExtSvc=[evtSvc],
                OutputLevel=INFO,
               )
