from Gaudi.Configuration import *


path = "/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/"
files = [path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00002.root",
         path + "Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00003.root"]

from Configurables import k4DataSvc
evtSvc = k4DataSvc('EventDataSvc')
# muons:
#evtSvc.input = '/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00001.root'
evtSvc.inputs = files
# hadrons:
#evtSvc.input = '/afs/cern.ch/user/c/chensel/ILD/lcio_edm4hep/edm4hep/Dirac-Dst-E250-qqh_zz_4n.eL.pR-00100.edm4hep.root'
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

from Configurables import PodioOutput
output = PodioOutput('output')
output.filename = 'tst.root'


from Configurables import ApplicationMgr
ApplicationMgr( TopAlg=[input, myalg, output],
                EvtSel="NONE",
                EvtMax=-1,
		ExtSvc=[evtSvc],
                OutputLevel=INFO,
                )
