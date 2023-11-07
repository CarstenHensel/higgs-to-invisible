#include "HtoInvAlg.h"
#include "GaudiKernel/MsgStream.h"
#include <vector>
#include <TLorentzVector.h>
#include "edm4hep/ReconstructedParticle.h"

DECLARE_COMPONENT(HtoInvAlg)

HtoInvAlg::HtoInvAlg(const std::string& aName, ISvcLocator* aSvcLoc) : GaudiAlgorithm(aName, aSvcLoc) {
    declareProperty("RecoParticleColl", m_recoParticleCollHandle, "RecoParticle collection");
    declareProperty("IsolatedLeptonsColl", m_isolatedLeptonsCollHandle, "Isolated Leptons collection");
}

HtoInvAlg::~HtoInvAlg() {
}

StatusCode HtoInvAlg::initialize() {
  m_event_counter = 0;
  return StatusCode::SUCCESS; 
}

StatusCode HtoInvAlg::execute() { 

m_event_counter += 1;

std::cout << "event count " << m_event_counter << std::endl;


double sqrts =250.0;

const auto *isoLeptonColl = m_isolatedLeptonsCollHandle.get(); 
 
const auto *recoColl = m_recoParticleCollHandle.get();
int muonsFound = 0;
std::vector<TLorentzVector> muons;
std::vector<edm4hep::ReconstructedParticle> muonCandidates;
for (const auto reco : *recoColl) {
    if (std::abs(reco.getType()) == 13) {
        muonCandidates.push_back(reco);
        TLorentzVector muon = TLorentzVector();
        muon.SetPxPyPzE(reco.getMomentum()[0], reco.getMomentum()[1], reco.getMomentum()[2], reco.getEnergy());
	muons.push_back(muon);
        muonsFound++;
    }
    if (std::abs(reco.getType()) == 22) {
       info() << "photon energy " << reco.getEnergy() << endmsg;
       double cos_theta = reco.getMomentum()[2] / reco.getEnergy();
       if (std::abs(cos_theta) > 0.9) {
           sqrts = sqrts - reco.getEnergy();	
       }
       fillHisto("ISR cos theta", "ISR cos theta", 50, -1, 1, cos_theta);
       fillHisto("ISR spectrum", "ISR spectrum", 50, 0, 50, reco.getEnergy());
    } 
}
if (muonsFound > 1){

fillHisto("invariant mass", "invariant mass", 120, 0, 120, (muons[0]+muons[1]).M());

double recoil_corrected = std::sqrt(pow(sqrts-(muons[0]+muons[1]).E(),2) - pow((muons[0]+muons[1]).P(),2));
double recoil = std::sqrt(pow(250-(muons[0]+muons[1]).E(),2) - pow((muons[0]+muons[1]).P(),2));
info() << recoil << " " << (muons[0]+muons[1]).E() << " " << (muons[0]+muons[1]).P() << endmsg;
fillHisto("recoil mass corrected", "recoild mass", 200, 0, 200, recoil_corrected);
fillHisto("recoil mass", "recoild mass", 200, 0, 200, recoil);

}

std::cout << "CH in the event loop" << std::endl;
info() << "CH in the event loop info()" << endmsg;
return StatusCode::SUCCESS; 
}

StatusCode HtoInvAlg::finalize() { 
    std::unique_ptr<TFile> myFile( TFile::Open("file.root", "RECREATE") );
    //myFile->WriteObject(&myObject, "MyObject");
    for (auto const& x : histos) {
    	std::cout << x.first  // string (key)
                  << ':' 
            	  << x.second // string's value 
             	  << std::endl;
   	x.second->Write();
        myFile->WriteObject(x.second, "MyObject");
    }
    myFile->Close();

return StatusCode::SUCCESS; 
}


void HtoInvAlg::fillHisto(const char *name, const char *title, int nbinsx, double xlow, double xup, double value){
  if (histos.find(name) == histos.end()) {
	// key not found
        histos[name] = new TH1F(name, title, nbinsx, xlow, xup);
  }
  histos[name]->Fill(value);

}
