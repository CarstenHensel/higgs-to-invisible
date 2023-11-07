#include "HtoInvAlg.h"
#include "GaudiKernel/MsgStream.h"
#include <vector>
#include <TLorentzVector.h>
#include "edm4hep/ReconstructedParticle.h"

DECLARE_COMPONENT(HtoInvAlg)

HtoInvAlg::HtoInvAlg(const std::string& aName, ISvcLocator* aSvcLoc) : GaudiAlgorithm(aName, aSvcLoc) {
    declareProperty("RecoParticleColl", m_recoParticleCollHandle, "RecoParticle collection");
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

auto *jetColl = m_jetsCollectionHandle.createAndPut();
jetColl->setSubsetCollection();

double sqrts =250.0;

const auto *recoColl = m_recoParticleCollHandle.get();
int muonsFound = 0;
std::vector<TLorentzVector> muons;
std::vector<TLorentzVector>photons;
std::vector<edm4hep::ReconstructedParticle> photonCandidates;
std::vector<edm4hep::ReconstructedParticle> muonCandidates;
double SCorr;
double EMuonCorr;
double photon_winkel;
std::vector<double> muon_energies;

for (const auto reco : *recoColl) {
  auto   particles = reco.getType();
     fillHisto("particles", "particles",200,-100,100, particles);
    if (std::abs(reco.getType()) == 13) {
        muonCandidates.push_back(reco);
        TLorentzVector muon = TLorentzVector();
        muon.SetPxPyPzE(reco.getMomentum()[0], reco.getMomentum()[1], reco.getMomentum()[2], reco.getEnergy());
	muons.push_back(muon);
        muonsFound++;
    }
    if (std::abs(reco.getType()) == -13,13){
      auto cos_theta_muons=reco.getMomentum()[0]/reco.getMomentum()[0,1,2];
	fillHisto("cos_theta_muons", "cos_theta_muons",200,-1,1,cos_theta_muons);
    }
    if (std::abs(reco.getType()) == 22) {
      photonCandidates.push_back(reco);
      TLorentzVector photon = TLorentzVector();
      photon.SetPxPyPzE(reco.getMomentum()[0], reco.getMomentum()[1], reco.getMomentum()[2], reco.getEnergy());
      photons.push_back(photon);
       info() << "photon energy " << reco.getEnergy() << endmsg;
       double cos_theta = reco.getMomentum()[2] / reco.getEnergy();
       photon_winkel = sqrt(atan(reco.getMomentum() [1]/reco.getMomentum() [2])*atan(reco.getMomentum()[1]/reco.getMomentum() [2])+atan(reco.getMomentum() [0]/reco.getMomentum()[2])*atan(reco.getMomentum() [0]/reco.getMomentum() [2]));
       if (std::abs(photon_winkel) <0.3) {
	 fillHisto("SpectrumPhotonElektron","SprectrumPhotonElektron", 200,0,50, reco.getEnergy());
           sqrts = sqrts - reco.getEnergy();	
       }
       fillHisto("ISR cos theta", "ISR cos theta", 200, -1, 1, cos_theta);
       fillHisto("ISR spectrum", "ISR spectrum", 200, 0, 50, reco.getEnergy());
       fillHisto("photon", "photon", 200,0,4,photon_winkel);
    } 
}
 std::vector<TLorentzVector>::iterator muon = muons.begin();
 std::vector<TLorentzVector>::iterator photon = photons.begin();

 for (muon; muon <muons.end(); muon++){
   for (photon;photon <photons.end(); photon++){
     auto g_px = (*photon).Px();
     auto g_py = (*photon).Py();
     auto g_pz = (*photon).Pz();
     auto g_e = (*photon).E();
     auto m_px = (*muon).Px();
     auto m_py = (*muon).Py();
     auto m_pz = (*muon).Pz();
     auto m_e = (*muon).E();
     auto deltaR = sqrt((atan(g_py/g_pz)-atan(m_py/m_pz))*(atan(g_py/g_pz)-atan(m_py/m_pz))+((atan(g_px/g_pz)-atan(m_px/m_pz))*(atan(g_px/g_pz)-atan(m_px/m_pz))));
     fillHisto("DeltaR","DeltaR",200,0,4,deltaR);

        if (deltaR < 0.3){
       EMuonCorr = m_e + g_e;
       muon_energies.push_back(EMuonCorr);
       fillHisto("SpectrumPhotonMyon","SpectrumPhotonMyon",200,0,50,g_e);
     }else{
       muon_energies.push_back(m_e);
     }
	  }
}

std::vector<TLorentzVector>::iterator Photon = photons.begin();

 for (Photon;Photon <photons.end(); Photon++){
   auto g_px = (*Photon).Px();
   auto g_py = (*Photon).Py();
   auto g_pz = (*Photon).Pz();
   auto g_e = (*Photon).E();
  
   auto theta_photon = sqrt(atan(g_py/g_pz)*atan(g_py/g_pz)+atan(g_px/g_pz)*atan(g_px/g_pz));
   fillHisto("theta_photon","theta_photon",200,0,4,theta_photon);
   
   if (theta_photon < 0.3){
     SCorr = 250 - g_e;
   }

 }
if (muonsFound > 1){

fillHisto("invariant mass", "invariant mass", 240, 0, 120, (muons[0]+muons[1]).M());
auto me1 = 0.0;
auto me2 = 0.0;
if (muon_energies.size() >1){
   me1 = muon_energies[0];
   me2 = muon_energies[0];
}else{
   me1 = muons[0].E();
   me2 = muons[1].E();
}

auto RecoilMassCorrE = sqrt((sqrts-(muons[0]+muons[1]).E())*(sqrts-(muons[0]+muons[1]).E())-((muons[0]+muons[1]).P())*((muons[0]+muons[1]).P()));
auto RecoilMassCorrM = sqrt ((250-(me1+me2))*(250-(me1+me2))-((muons[0]+muons[1]).P())*((muons[0]+muons[1]).P()));
auto RecoilMassCorrEM = sqrt ((sqrts-(me1+me2))*(sqrts-(me1+me2))-((muons[0]+muons[1]).P())*((muons[0]+muons[1]).P()));
muons[0].SetE(me1);
muons[1].SetE(me2);
auto InvMassCorr = (muons[0]+muons[1]).M();
 if ((photon_winkel >0.1)&&(photon_winkel <0.3)){
     fillHisto("RecoilMassCorrEP","RecoilMassCorrEP",400,0,200,RecoilMassCorrE);
     fillHisto("RecoilMassCorrMP","RecoilMassCorrMP",400,0,200,RecoilMassCorrM);
     fillHisto("RecoilMassCorrEMP","RecoilMassCorrEMP",400,0,200,RecoilMassCorrEM);
  }
fillHisto("InvMassCorr","InvMassCorr",240,0,120,InvMassCorr);
fillHisto("RecoilMassCorrE","RecoilMassCorrE",400,0,200,RecoilMassCorrE);
fillHisto("RecoilMassCorrM","RecoilMassCorrM",400,0,200,RecoilMassCorrM);
fillHisto("RecoilMassCorrEM","RecoilMassCorrEM",400,0,200,RecoilMassCorrEM);

//double recoil_corrected = std::sqrt(pow(sqrts-(muons[0]+muons[1]).E(),2) - pow((muons[0]+muons[1]).P(),2));
double recoil = std::sqrt(pow(250-(muons[0]+muons[1]).E(),2) - pow((muons[0]+muons[1]).P(),2));
info() << recoil << " " << (muons[0]+muons[1]).E() << " " << (muons[0]+muons[1]).P() << endmsg;
//fillHisto("recoil mass corrected", "recoild mass corrected", 200, 0, 200, recoil_corrected);
fillHisto("recoil mass", "recoild mass", 400, 0, 200, recoil);

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
