from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
             'lcgeo_DIR': "/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-03/lcgeo/v00-16-07",
             'DetectorModel': "ILD_l5_o1_v02",
             'CompactFile': "%(lcgeo_DIR)s/ILD/compact/%(DetectorModel)s/%(DetectorModel)s.xml",
             'OutputDirectory': "path_to_output_files",
             'createRootTree': "true",
             'displayEvent': "false",
             'OutputBaseName': "SLDCorrection",
             'OutputBaseName_iter': "0",
             'Verbosity': "MESSAGE",
             'MCparticleCollectionName': "MCParticlesSkimmed",
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = DEBUG
#CH read.Files = ["input_DTS.slcio"]
read.Files = ["/eos/experiment/clicdp/grid/ilc/user/t/tjunping/data/slcio/E250_overlay/Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.slcio"]
algList.append(read)


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

MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
MyFastJetProcessor.OutputLevel = DEBUG
MyFastJetProcessor.ProcessorType = "FastJetProcessor"
MyFastJetProcessor.Parameters = {
                                 "algorithm": ["ee_kt_algorithm"],
                                 "clusteringMode": ["ExclusiveNJets", "2"],
                                 "findNrJets": ["2"],
                                 "findNrJetsCollectionPrefix": ["Jets_"],
                                 "jetOut": ["Durham_2Jets"],
                                 "recParticleIn": ["PandoraPFOsWithoutIsoLep"],
                                 "recParticleOut": ["Durham_2JetsPFOs"],
                                 "recombinationScheme": ["E_scheme"],
                                 "storeParticlesInJets": ["true"]
                                 }


MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
MyLCIOOutputProcessor.OutputLevel = DEBUG
MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
MyLCIOOutputProcessor.Parameters = {
                                    "KeepCollectionNames": ["SemiLeptonicDecayVertex", "SemiLeptonicDecay_RP", "recoNeutrinos", "JetSLDLink", "SLDJetLink", "mcNurecoNuLink", "recoNumcNuLink", "NuSLDLink", "SLDNuLink"],
                                    "LCIOOutputFile": ["%(OutputDirectory)s/%(OutputBaseName)s.slcio" % CONSTANTS],
                                    "LCIOWriteMode": ["WRITE_NEW"]
                                    }

algList.append(MyIsolatedLeptonTaggingProcessor)
algList.append(MyFastJetProcessor)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=DEBUG
              )
