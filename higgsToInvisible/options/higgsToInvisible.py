from Gaudi.Configuration import *


path = "/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/"
files = [path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00002.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00003.root"]

from Configurables import k4DataSvc
from Configurables import MarlinProcessorWrapper

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
input.collections = ["PandoraPFOs"]

from Configurables import HtoInvAlg
myalg = HtoInvAlg()
myalg.RecoParticleColl = 'PandoraPFOs'
#myalg.MuonColl = 'Muons'
myalg.OutputLevel = INFO

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


#MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
#MyFastJetProcessor.OutputLevel = DEBUG
#MyFastJetProcessor.ProcessorType = "FastJetProcessor"
#MyFastJetProcessor.Parameters = {
#                                 "algorithm": ["ee_kt_algorithm"],
#                                 "clusteringMode": ["ExclusiveNJets", "2"],
#                                 "findNrJets": ["2"],
#                                 "findNrJetsCollectionPrefix": ["Jets_"],
#                                 "jetOut": ["Durham_2Jets"],
#                                 "recParticleIn": ["PandoraPFOsWithoutIsoLep"],
#                                 "recParticleOut": ["Durham_2JetsPFOs"],
#                                 "recombinationScheme": ["E_scheme"],
#                                 "storeParticlesInJets": ["true"]
#                                 }




from Configurables import PodioOutput
output = PodioOutput('output')
output.filename = 'tst.root'


from Configurables import ApplicationMgr
ApplicationMgr( TopAlg=[input, myalg, output],
                EvtSel="NONE",
                EvtMax=10,
		ExtSvc=[evtSvc],
                OutputLevel=INFO,
                )
