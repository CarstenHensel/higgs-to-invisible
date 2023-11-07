from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
             'lcgeo_DIR': "/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-02/lcgeo/v00-16-06",
             'DetectorModel': "ILD_l5_o1_v02",
             'CompactFile': "%(lcgeo_DIR)s/ILD/compact/%(DetectorModel)s/%(DetectorModel)s.xml",
             'OutputDirectory': "/nfs/dust/ilc/user/jtorndal/PhysicsAnalysis",
             'OutputBaseName': "e2e2hhECMStudies",
             'OutputRootFile': "%(OutputBaseName)s.root",
             'NumberOfHiggs': "2",
             'NumberOfJets': "4",
             'NumberOfIsoLeps': "2",
             'WhichPreselection': "llbbbb",
             'createRootTree': "false",
             'displayEvent': "false",
             'Verbosity': "DEBUG",
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = DEBUG
read.Files = ["/pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015806/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15806_0.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015806/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15806_1.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015806/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15806_0.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015806/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15806_1.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_0.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_1.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_2.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_3.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_4.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_5.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n000.d_dstm_15807_6.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_10.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_11.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_12.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_13.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_14.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_15.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_7.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_8.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n001.d_dstm_15807_9.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_16.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_17.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_18.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_19.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_20.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_21.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_22.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403001.Pe2e2hh.eL.pR.n002.d_dstm_15807_23.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_0.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_1.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_2.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_3.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_4.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_5.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n000.d_dstm_15807_6.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_10.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_11.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_12.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_13.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_14.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_15.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_7.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_8.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n001.d_dstm_15807_9.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_16.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_17.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_18.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_19.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_20.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_21.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_22.slcio
      /pnfs/desy.de/ilc/prod/ilc/mc-2020/ild/dst-merged/500-TDR_ws/hh/ILD_l5_o1_v02_nobg/v02-02-03/00015807/000/rv02-02-03.sv02-02-03.mILD_l5_o1_v02_nobg.E500-TDR_ws.I403002.Pe2e2hh.eR.pL.n002.d_dstm_15807_23.slcio"]
algList.append(read)

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = DEBUG
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["%(CompactFile)s" % CONSTANTS]
                         }

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = DEBUG
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["%(OutputDirectory)s/root/%(OutputBaseName)s_AIDA" % CONSTANTS],
                              "FileType": ["root"]
                              }

MyAddNeutralPFOCovMatLite = MarlinProcessorWrapper("MyAddNeutralPFOCovMatLite")
MyAddNeutralPFOCovMatLite.OutputLevel = DEBUG
MyAddNeutralPFOCovMatLite.ProcessorType = "AddNeutralPFOCovMat"
MyAddNeutralPFOCovMatLite.Parameters = {
                                        "AssumeNeutralPFOMassive": ["true"],
                                        "inputPfoCollection": ["PandoraPFOs"],
                                        "isClusterEnergyKinEnergy": ["false"],
                                        "outputPfoCollection": ["PandoraPFO_updatedNeutralPFOs"],
                                        "updatePFO4Momentum": ["false"],
                                        "useTrueJacobian": ["false"]
                                        }

MyHdecayMode = MarlinProcessorWrapper("MyHdecayMode")
MyHdecayMode.OutputLevel = DEBUG
MyHdecayMode.ProcessorType = "HdecayMode"
MyHdecayMode.Parameters = {
                           "HdecayModeCollection": ["HdecayMode"],
                           "MCParticleCollection": ["MCParticlesSkimmed"],
                           "nHiggs": ["%(NumberOfHiggs)s" % CONSTANTS]
                           }

MySLDecayFinder = MarlinProcessorWrapper("MySLDecayFinder")
MySLDecayFinder.OutputLevel = DEBUG
MySLDecayFinder.ProcessorType = "SLDecayFinder"
MySLDecayFinder.Parameters = {
                              "MCParticleCollection": ["MCParticlesSkimmed"],
                              "PfoCollection": ["PandoraPFOs"],
                              "SemiLeptonicDecays": ["SemiLeptonicDecays"]
                              }

mytruejet = MarlinProcessorWrapper("mytruejet")
mytruejet.OutputLevel = DEBUG
mytruejet.ProcessorType = "TrueJet"
mytruejet.Parameters = {
                        "FinalColourNeutralLink": ["FinalColourNeutralLink"],
                        "FinalColourNeutrals": ["FinalColourNeutrals"],
                        "FinalElementonLink": ["FinalElementonLink"],
                        "InitialColourNeutralLink": ["InitialColourNeutralLink"],
                        "InitialColourNeutrals": ["InitialColourNeutrals"],
                        "InitialElementonLink": ["InitialElementonLink"],
                        "MCParticleCollection": ["MCParticlesSkimmed"],
                        "RecoMCTruthLinkName": ["RecoMCTruthLink"],
                        "RecoParticleCollection": ["PandoraPFOs"],
                        "TrueJetMCParticleLink": ["TrueJetMCParticleLink"],
                        "TrueJetPFOLink": ["TrueJetPFOLink"],
                        "TrueJets": ["TrueJets"]
                        }

myCheatedMCOverlayRemoval = MarlinProcessorWrapper("myCheatedMCOverlayRemoval")
myCheatedMCOverlayRemoval.OutputLevel = DEBUG
myCheatedMCOverlayRemoval.ProcessorType = "CheatedMCOverlayRemoval"
myCheatedMCOverlayRemoval.Parameters = {
                                        "MCParticleCollection": ["MCParticlesSkimmed"],
                                        "MCTruthRecoLink": ["MCTruthRecoLink"],
                                        "OutputPfoCollection": ["PFOsWithoutMCOverlay"],
                                        "RecoMCTruthLink": ["RecoMCTruthLink"],
                                        "RecoParticleCollection": ["PandoraPFOs"]
                                        }

Thrust = MarlinProcessorWrapper("Thrust")
Thrust.OutputLevel = DEBUG
Thrust.ProcessorType = "ThrustReconstruction"
Thrust.Parameters = {
                     "inputCollectionName": ["PFOsWithoutMCOverlay"],
                     "typeOfThrustFinder": ["2"]
                     }

MyFastJetProcessor_2Jets = MarlinProcessorWrapper("MyFastJetProcessor_2Jets")
MyFastJetProcessor_2Jets.OutputLevel = DEBUG
MyFastJetProcessor_2Jets.ProcessorType = "FastJetProcessor"
MyFastJetProcessor_2Jets.Parameters = {
                                       "algorithm": ["ee_genkt_algorithm", "1.0", "1.0"],
                                       "clusteringMode": ["ExclusiveNJets", "2"],
                                       "findNrJets": ["2"],
                                       "findNrJetsCollectionPrefix": ["TwoJets_"],
                                       "jetOut": ["Durham_2Jets"],
                                       "recParticleIn": ["PFOsWithoutMCOverlay"],
                                       "recParticleOut": ["Durham_2JetsPFOs"],
                                       "recombinationScheme": ["E_scheme"],
                                       "storeParticlesInJets": ["true"]
                                       }

MyIsolatedLeptonTaggingProcessor = MarlinProcessorWrapper("MyIsolatedLeptonTaggingProcessor")
MyIsolatedLeptonTaggingProcessor.OutputLevel = DEBUG
MyIsolatedLeptonTaggingProcessor.ProcessorType = "IsolatedLeptonTaggingProcessor"
MyIsolatedLeptonTaggingProcessor.Parameters = {
                                               "CosConeLarge": ["0.95"],
                                               "CosConeSmall": ["0.98"],
                                               "CutOnTheISOElectronMVA": ["0.5"],
                                               "CutOnTheISOMuonMVA": ["0.7"],
                                               "DirOfISOElectronWeights": ["/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-02/MarlinReco/v01-31/Analysis/IsolatedLeptonTagging/example/isolated_electron_weights"],
                                               "DirOfISOMuonWeights": ["/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/v02-02-02/MarlinReco/v01-31/Analysis/IsolatedLeptonTagging/example/isolated_muon_weights_woYoke"],
                                               "InputPandoraPFOsCollection": ["PFOsWithoutMCOverlay"],
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
                                               "OutputIsoLeptonsCollection": ["ISOLeptons"],
                                               "OutputPFOsWithoutIsoLepCollection": ["PandoraPFOsWithoutIsoLep"],
                                               "UseYokeForMuonID": ["false"]
                                               }

MyLeptonPairing = MarlinProcessorWrapper("MyLeptonPairing")
MyLeptonPairing.OutputLevel = DEBUG
MyLeptonPairing.ProcessorType = "LeptonPairing"
MyLeptonPairing.Parameters = {
                              "ISOLeptons": ["ISOLeptons"],
                              "LeptonPair": ["LeptonPair"],
                              "PandoraPFOsWithoutIsoLep": ["PandoraPFOsWithoutIsoLep"],
                              "PandoraPFOsWithoutLepPair": ["PandoraPFOsWithoutLepPair"],
                              "RootFile": ["%(OutputDirectory)s/%(OutputBaseName)s_LeptonPairing.root" % CONSTANTS],
                              "fillRootTree": ["true"]
                              }

MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
MyFastJetProcessor.OutputLevel = DEBUG
MyFastJetProcessor.ProcessorType = "FastJetProcessor"
MyFastJetProcessor.Parameters = {
                                 "algorithm": ["ee_kt_algorithm"],
                                 "clusteringMode": ["ExclusiveNJets", "%(NumberOfJets)s" % CONSTANTS],
                                 "findNrJets": ["%(NumberOfJets)s" % CONSTANTS],
                                 "findNrJetsCollectionPrefix": ["Jets_"],
                                 "jetOut": ["DurhamJets"],
                                 "recParticleIn": ["PandoraPFOsWithoutIsoLep"],
                                 "recParticleOut": ["DurhamJetsPFOs"],
                                 "recombinationScheme": ["E_scheme"],
                                 "storeParticlesInJets": ["true"]
                                 }

JC4FT = MarlinProcessorWrapper("JC4FT")
JC4FT.OutputLevel = DEBUG
JC4FT.ProcessorType = "LcfiplusProcessor"
JC4FT.Parameters = {
                    "Algorithms": ["JetClustering", "JetVertexRefiner", "FlavorTag", "ReadMVA"],
                    "FlavorTag.BookName": ["bdt"],
                    "FlavorTag.CategoryDefinition1": ["nvtx==0"],
                    "FlavorTag.CategoryDefinition2": ["nvtx==1&&nvtxall==1"],
                    "FlavorTag.CategoryDefinition3": ["nvtx==1&&nvtxall==2"],
                    "FlavorTag.CategoryDefinition4": ["nvtx>=2"],
                    "FlavorTag.CategoryPreselection1": ["trk1d0sig!=0"],
                    "FlavorTag.CategoryPreselection2": ["trk1d0sig!=0"],
                    "FlavorTag.CategoryPreselection3": ["trk1d0sig!=0"],
                    "FlavorTag.CategoryPreselection4": ["trk1d0sig!=0"],
                    "FlavorTag.CategorySpectators1": ["aux", "nvtx"],
                    "FlavorTag.CategorySpectators2": ["aux", "nvtx"],
                    "FlavorTag.CategorySpectators3": ["aux", "nvtx"],
                    "FlavorTag.CategorySpectators4": ["aux", "nvtx"],
                    "FlavorTag.CategoryVariables1": ["trk1d0sig", "trk2d0sig", "trk1z0sig", "trk2z0sig", "trk1pt_jete", "trk2pt_jete", "jprobr25sigma", "jprobz25sigma", "d0bprob2", "d0cprob2", "d0qprob2", "z0bprob2", "z0cprob2", "z0qprob2", "nmuon", "nelectron", "trkmass"],
                    "FlavorTag.CategoryVariables2": ["trk1d0sig", "trk2d0sig", "trk1z0sig", "trk2z0sig", "trk1pt_jete", "trk2pt_jete", "jprobr2", "jprobz2", "vtxlen1_jete", "vtxsig1_jete", "vtxdirang1_jete", "vtxmom1_jete", "vtxmass1", "vtxmult1", "vtxmasspc", "vtxprob", "d0bprob2", "d0cprob2", "d0qprob2", "z0bprob2", "z0cprob2", "z0qprob2", "trkmass", "nelectron", "nmuon"],
                    "FlavorTag.CategoryVariables3": ["trk1d0sig", "trk2d0sig", "trk1z0sig", "trk2z0sig", "trk1pt_jete", "trk2pt_jete", "jprobr2", "jprobz2", "vtxlen1_jete", "vtxsig1_jete", "vtxdirang1_jete", "vtxmom1_jete", "vtxmass1", "vtxmult1", "vtxmasspc", "vtxprob", "1vtxprob", "vtxlen12all_jete", "vtxmassall"],
                    "FlavorTag.CategoryVariables4": ["trk1d0sig", "trk2d0sig", "trk1z0sig", "trk2z0sig", "trk1pt_jete", "trk2pt_jete", "jprobr2", "jprobz2", "vtxlen1_jete", "vtxsig1_jete", "vtxdirang1_jete", "vtxmom1_jete", "vtxmass1", "vtxmult1", "vtxmasspc", "vtxprob", "vtxlen2_jete", "vtxsig2_jete", "vtxdirang2_jete", "vtxmom2_jete", "vtxmass2", "vtxmult2", "vtxlen12_jete", "vtxsig12_jete", "vtxdirang12_jete", "vtxmom_jete", "vtxmass", "vtxmult", "1vtxprob"],
                    "FlavorTag.D0ProbFileName": ["/cvmfs/ilc.desy.de/sw/ILDConfig/v02-02-01/LCFIPlusConfig/vtxprob/d0probv2_ildl5_6q500.root"],
                    "FlavorTag.JetCollectionName": ["RefinedJets"],
                    "FlavorTag.PIDAlgo": ["lcfiplus"],
                    "FlavorTag.WeightsDirectory": ["/afs/desy.de/user/j/jtorndal/pool/lcfiweights"],
                    "FlavorTag.WeightsPrefix": ["6q500_v04_p00_ildl5"],
                    "FlavorTag.Z0ProbFileName": ["/cvmfs/ilc.desy.de/sw/ILDConfig/v02-02-01/LCFIPlusConfig/vtxprob/z0probv2_ildl5_6q500.root"],
                    "JetClustering.InputVertexCollectionName": ["BuildUpVertex"],
                    "JetClustering.JetAlgorithm": ["DurhamVertex"],
                    "JetClustering.MuonIDExternal": ["0"],
                    "JetClustering.MuonIDMaximum3DImpactParameter": ["5."],
                    "JetClustering.MuonIDMinimumD0Significance": ["5."],
                    "JetClustering.MuonIDMinimumProbability": ["0.5"],
                    "JetClustering.MuonIDMinimumZ0Significance": ["5."],
                    "JetClustering.NJetsRequested": ["%(NumberOfJets)s" % CONSTANTS],
                    "JetClustering.OutputJetCollectionName": ["VertexJets"],
                    "JetClustering.PrimaryVertexCollectionName": ["PrimaryVertex"],
                    "JetClustering.UseBeamJets": ["0"],
                    "JetClustering.UseMuonID": ["1"],
                    "JetClustering.VertexSelectionK0MassWidth": ["0.02"],
                    "JetClustering.VertexSelectionMaximumDistance": ["30."],
                    "JetClustering.VertexSelectionMinimumDistance": ["0.3"],
                    "JetClustering.YAddedForJetLeptonLepton": ["100"],
                    "JetClustering.YAddedForJetLeptonVertex": ["100"],
                    "JetClustering.YAddedForJetVertexVertex": ["100"],
                    "JetClustering.YCut": ["0."],
                    "JetVertexRefiner.InputJetCollectionName": ["VertexJets"],
                    "JetVertexRefiner.InputVertexCollectionName": ["BuildUpVertex"],
                    "JetVertexRefiner.MaxAngleSingle": ["0.5"],
                    "JetVertexRefiner.MaxCharmFlightLengthPerJetEnergy": ["0.1"],
                    "JetVertexRefiner.MaxPosSingle": ["30."],
                    "JetVertexRefiner.MaxSeparationPerPosSingle": ["0.1"],
                    "JetVertexRefiner.MinEnergySingle": ["1."],
                    "JetVertexRefiner.MinPosSingle": ["0.3"],
                    "JetVertexRefiner.OneVertexProbThreshold": ["0.001"],
                    "JetVertexRefiner.OutputJetCollectionName": ["RefinedJets"],
                    "JetVertexRefiner.OutputVertexCollectionName": ["RefinedVertex"],
                    "JetVertexRefiner.PrimaryVertexCollectionName": ["PrimaryVertex"],
                    "JetVertexRefiner.V0VertexCollectionName": ["BuildUpVertex_V0"],
                    "JetVertexRefiner.mind0sigSingle": ["5."],
                    "JetVertexRefiner.minz0sigSingle": ["5."],
                    "MCPCollection": [],
                    "MCPFORelation": [],
                    "MakeNtuple.AuxiliaryInfo": ["-1"],
                    "PFOCollection": ["PandoraPFOsWithoutLepPair"],
                    "PrimaryVertexCollectionName": ["PrimaryVertex"],
                    "PrintEventNumber": ["100"],
                    "ReadSubdetectorEnergies": ["1"],
                    "TrackHitOrdering": ["1"],
                    "UpdateVertexRPDaughters": ["0"],
                    "UseMCP": ["0"]
                    }

PreSelection = MarlinProcessorWrapper("PreSelection")
PreSelection.OutputLevel = DEBUG
PreSelection.ProcessorType = "PreSelection"
PreSelection.Parameters = {
                           "ECM": ["500."],
                           "JetCollectionName": ["RefinedJets"],
                           "LepPairCollection": ["LeptonPair"],
                           "inputPfoCollection": ["PandoraPFOs"],
                           "isolatedeptonCollection": ["ISOLeptons"],
                           "maxEvis": ["999."],
                           "maxdijetmass": ["180."],
                           "maxdijetmassdiff": ["80."],
                           "maxdileptonmassdiff": ["40."],
                           "maxmissingPT": ["70."],
                           "maxthrust": ["0.9"],
                           "minHHmass": ["0."],
                           "minblikeliness": ["0."],
                           "mindijetmass": ["60."],
                           "minmissingPT": ["0."],
                           "minnbjets": ["0"],
                           "nIsoLeps": ["2"],
                           "nJets": ["4"],
                           "outputFilename": ["%(OutputDirectory)s/%(OutputBaseName)s_PreSelection.root" % CONSTANTS],
                           "whichPreselection": ["%(WhichPreselection)s" % CONSTANTS]
                           }

MySLDCorrection = MarlinProcessorWrapper("MySLDCorrection")
MySLDCorrection.OutputLevel = DEBUG
MySLDCorrection.ProcessorType = "SLDCorrection"
MySLDCorrection.Parameters = {
                              "BSLDChargedSLD4InvMassCut": ["1.65"],
                              "BSLDChargedSLD5InvMassCut": ["1.70"],
                              "BSLDNeutralSLD4InvMassCut": ["1.88"],
                              "BSLDNeutralSLD5InvMassCut": ["2.0"],
                              "BuildUpVertex": ["BuildUpVertex"],
                              "CSLDChargedSLD4InvMassCut": ["0.00"],
                              "CSLDChargedSLD5InvMassCut": ["0.00"],
                              "CSLDNeutralSLD4InvMassCut": ["0.0"],
                              "CSLDNeutralSLD5InvMassCut": ["0.0"],
                              "JetCollection": ["RefinedJets"],
                              "JetSLDLinkName": ["JetSLDLink"],
                              "MCParticleCollection": ["MCParticlesSkimmed"],
                              "MCTruthRecoLinkCollection": ["MCTruthRecoLink"],
                              "NuSLDLinkName": ["NuSLDLink"],
                              "PfoCollection": ["PandoraPFOsWithoutLepPair"],
                              "PrimaryVertex": ["PrimaryVertex"],
                              "RecoMCTruthLinkCollection": ["RecoMCTruthLink"],
                              "ReconstructedNeutrino": ["recoNeutrinos"],
                              "RootFile": ["%(OutputDirectory)s/%(OutputBaseName)s_SLDCorrection.root" % CONSTANTS],
                              "SLDJetLinkName": ["SLDJetLink"],
                              "SLDNuLinkName": ["SLDNuLink"],
                              "SemiLeptonicDecayVertex": ["SemiLeptonicDecayVertex"],
                              "SemiLeptonicDecayVertexRP": ["SemiLeptonicDecay_RP"],
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
                              "isoLeptonsCollection": ["LeptonPair"],
                              "mcNurecoNuLinkName": ["mcNurecoNuLink"],
                              "nIterFlightDirCorrection": ["1"],
                              "neutralCosAcceptanceAngle": ["0.5"],
                              "recoFourMomentumOfVisibles": ["2"],
                              "recoNumcNuLinkName": ["recoNumcNuLink"],
                              "vertexingScenario": ["4"]
                              }

MyErrorFlow = MarlinProcessorWrapper("MyErrorFlow")
MyErrorFlow.OutputLevel = DEBUG
MyErrorFlow.ProcessorType = "ErrorFlow"
MyErrorFlow.Parameters = {
                          "CovMatFactorNeutralHadrons": ["1.8"],
                          "CovMatFactorPhotons": ["1.3"],
                          "EnableConfusionTerm": ["true"],
                          "InputPFOCollection": ["RefinedJets"],
                          "OutputPFOCollection": ["OutputErrorFlowJets"],
                          "PropagateConfusion2Mom": ["true"],
                          "useFullCovMatforNeutrals": ["true"]
                          }

MyZHHKinFitLeptonChannel = MarlinProcessorWrapper("MyZHHKinFitLeptonChannel")
MyZHHKinFitLeptonChannel.OutputLevel = DEBUG
MyZHHKinFitLeptonChannel.ProcessorType = "ZHHKinFitLeptonChannel"
MyZHHKinFitLeptonChannel.Parameters = {
                                       "ECM": ["500."],
                                       "ISRPzMax": ["125.6"],
                                       "InputIsoLeptonsCollection": ["LeptonPair"],
                                       "JetCollectionName": ["RefinedJets"],
                                       "JetPullsOutputCollection": ["JetPulls"],
                                       "JetSLDRelationCollection": ["JetSLDLink"],
                                       "LeptonPullsOutputCollection": ["LeptonPulls"],
                                       "SLDNeutrinoRelationCollection": ["SLDNuLink"],
                                       "SLDVertexCollection": ["SemiLeptonicDecayVertex"],
                                       "SigmaAnglesScaleFactor": ["1.3"],
                                       "SigmaEnergyScaleFactor": ["1.5"],
                                       "SigmaInvPtScaleFactor": ["1.1"],
                                       "fithypothesis": ["MH"],
                                       "fitter": ["0"],
                                       "ievttrace": ["-1"],
                                       "includeISR": ["true"],
                                       "outputFilename": ["%(OutputDirectory)s/%(OutputBaseName)s_Kinfit.root" % CONSTANTS],
                                       "outputJetCollection": ["JetsPreFit"],
                                       "outputLeptonCollection": ["LeptonsPreFit"],
                                       "recoNumcNuLinkName": ["recoNumcNuLink"],
                                       "traceall": ["false"]
                                       }

MyLeptonErrorAnalysis = MarlinProcessorWrapper("MyLeptonErrorAnalysis")
MyLeptonErrorAnalysis.OutputLevel = DEBUG
MyLeptonErrorAnalysis.ProcessorType = "LeptonErrorAnalysis"
MyLeptonErrorAnalysis.Parameters = {
                                    "LeptonResidualsOutputCollection": ["LeptonResiduals"],
                                    "MCParticleCollection": ["MCParticlesSkimmed"],
                                    "MCTruthTrackLinkCollection": ["MCTruthMarlinTrkTracksLink"],
                                    "RecoParticleCollection": ["PandoraPFOs"],
                                    "TrackMCTruthLinkCollection": ["MarlinTrkTracksMCTruthLink"],
                                    "inputIsolepCollection": ["LeptonPair"]
                                    }

MyJetErrorAnalysis_woNu = MarlinProcessorWrapper("MyJetErrorAnalysis_woNu")
MyJetErrorAnalysis_woNu.OutputLevel = DEBUG
MyJetErrorAnalysis_woNu.ProcessorType = "JetErrorAnalysis"
MyJetErrorAnalysis_woNu.Parameters = {
                                      "JetResidualsOutputCollection": ["JetResiduals_woNu"],
                                      "RecoJetCollection": ["RefinedJets"],
                                      "matchMethod": ["0"]
                                      }

MyJetErrorAnalysis = MarlinProcessorWrapper("MyJetErrorAnalysis")
MyJetErrorAnalysis.OutputLevel = DEBUG
MyJetErrorAnalysis.ProcessorType = "JetErrorAnalysis"
MyJetErrorAnalysis.Parameters = {
                                 "JetResidualsOutputCollection": ["JetResiduals"],
                                 "RecoJetCollection": ["JetsKinFit"],
                                 "matchMethod": ["0"]
                                 }

MyMisclustering = MarlinProcessorWrapper("MyMisclustering")
MyMisclustering.OutputLevel = DEBUG
MyMisclustering.ProcessorType = "Misclustering"
MyMisclustering.Parameters = {
                              "RecoJetCollection": ["RefinedJets"],
                              "matchMethod": ["0"],
                              "outputFilename": ["%(OutputDirectory)s/%(OutputBaseName)s_Misclustering.root" % CONSTANTS]
                              }

MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
MyLCIOOutputProcessor.OutputLevel = DEBUG
MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
MyLCIOOutputProcessor.Parameters = {
                                    "KeepCollectionNames": ["IsolatedLeptons", "PandoraPFOsWithoutLepPair", "RefinedJets", "RefinedJetsPFOs", "OutputErrorFlowJets", "TrueJets", "FinalColourNeutrals", "InitialColourNeutrals", "TrueJetPFOLink", "TrueJetMCParticleLink", "FinalElementonLink", "InitialElementonLink", "FinalColourNeutralLink", "InitialColourNeutralLink", "HdecayMode", "IsolatedLeptons", "RefinedJets"],
                                    "LCIOOutputFile": ["%(OutputDirectory)s/slcio/%(OutputBaseName)s.slcio" % CONSTANTS],
                                    "LCIOWriteMode": ["WRITE_NEW"]
                                    }

algList.append(InitDD4hep)
algList.append(MyAIDAProcessor)
algList.append(MyAddNeutralPFOCovMatLite)
algList.append(MyHdecayMode)
algList.append(myCheatedMCOverlayRemoval)
algList.append(Thrust)
algList.append(MyFastJetProcessor_2Jets)
algList.append(MyIsolatedLeptonTaggingProcessor)
algList.append(MyLeptonPairing)
algList.append(MyFastJetProcessor)
algList.append(JC4FT)
algList.append(PreSelection)
# algList.append(mytruejet)  # MyHdecayMode.GoodEvent
# algList.append(MyMisclustering)  # MyHdecayMode.GoodEvent
algList.append(MyLCIOOutputProcessor)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=DEBUG
              )
