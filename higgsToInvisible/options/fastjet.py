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

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = DEBUG
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["%(CompactFile)s" % CONSTANTS]
                         }

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

MySLDCorrection = MarlinProcessorWrapper("MySLDCorrection")
MySLDCorrection.OutputLevel = DEBUG
MySLDCorrection.ProcessorType = "SLDCorrection"
MySLDCorrection.Parameters = {
                              "BSLDChargedSLD4InvMassCut": ["1.80"],
                              "BSLDChargedSLD5InvMassCut": ["1.50"],
                              "BSLDMode": ["1"],
                              "BSLDNeutralSLD4InvMassCut": ["2.80"],
                              "BSLDNeutralSLD5InvMassCut": ["2.50"],
                              "BuildUpVertex": ["BuildUpVertex"],
                              "CSLDChargedSLD4InvMassCut": ["0.00"],
                              "CSLDChargedSLD5InvMassCut": ["0.00"],
                              "CSLDMode": ["1"],
                              "CSLDNeutralSLD4InvMassCut": ["0.00"],
                              "CSLDNeutralSLD5InvMassCut": ["0.00"],
                              "JetCollection": ["Durham_2Jets"],
                              "JetSLDLinkName": ["JetSLDLink"],
                              "MCParticleCollection": ["%(MCparticleCollectionName)s" % CONSTANTS],
                              "MCTruthRecoLinkCollection": ["MCTruthRecoLink"],
                              "NuSLDLinkName": ["NuSLDLink"],
                              "PfoCollection": ["declusteredJetIsoleps"],
                              "PrimaryVertex": ["PrimaryVertex"],
                              "RecoMCTruthLinkCollection": ["RecoMCTruthLink"],
                              "ReconstructedNeutrino": ["recoNeutrinos"],
                              "RootFile": ["%(OutputDirectory)s/%(OutputBaseName)s_SLDCorrection_%(OutputBaseName_iter)s.root" % CONSTANTS],
                              "SLDJetLinkName": ["SLDJetLink"],
                              "SLDMode": ["1"],
                              "SLDNuLinkName": ["SLDNuLink"],
                              "SemiLeptonicDecayVertex": ["SemiLeptonicDecayVertex"],
                              "SemiLeptonicDecayVertexRP": ["SemiLeptonicDecay_RP"],
                              "TSLDMode": ["1"],
                              "chargedCosAcceptanceAngleSLD4": ["0.5"],
                              "chargedCosAcceptanceAngleSLD5": ["0.5"],
                              "cheatCharged4momentum": ["false"],
                              "cheatFlightDirection": ["false"],
                              "cheatLepton4momentum": ["false"],
                              "cheatNeutral4momentum": ["false"],
                              "cheatPVAcharged": ["false"],
                              "cheatPVAneutral": ["false"],
                              "cheatSLDLeptons": ["true"],
                              "displayEvent": ["%(displayEvent)s" % CONSTANTS],
                              "fillRootTree": ["%(createRootTree)s" % CONSTANTS],
                              "includeBSLD": ["true"],
                              "includeCSLD": ["false"],
                              "includeTSLD": ["false"],
                              "isoLeptonsCollection": ["IsolatedLeptons"],
                              "mcNurecoNuLinkName": ["mcNurecoNuLink"],
                              "nIterFlightDirCorrection": ["1"],
                              "neutralCosAcceptanceAngle": ["0.5"],
                              "recoFourMomentumOfVisibles": ["2"],
                              "recoNumcNuLinkName": ["recoNumcNuLink"],
                              "sigmaAlphaNu": ["0.100"],
                              "sigmaENu": ["4.00"],
                              "vertexingScenario": ["4"]
                              }

MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
MyLCIOOutputProcessor.OutputLevel = DEBUG
MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
MyLCIOOutputProcessor.Parameters = {
                                    "KeepCollectionNames": ["SemiLeptonicDecayVertex", "SemiLeptonicDecay_RP", "recoNeutrinos", "JetSLDLink", "SLDJetLink", "mcNurecoNuLink", "recoNumcNuLink", "NuSLDLink", "SLDNuLink"],
                                    "LCIOOutputFile": ["%(OutputDirectory)s/%(OutputBaseName)s.slcio" % CONSTANTS],
                                    "LCIOWriteMode": ["WRITE_NEW"]
                                    }

algList.append(InitDD4hep)
algList.append(MyIsolatedLeptonTaggingProcessor)
algList.append(MyFastJetProcessor)
algList.append(MySLDCorrection)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=DEBUG
              )
