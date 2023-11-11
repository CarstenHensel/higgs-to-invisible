#include "LeptonPairingAlg.h"
#include "edm4hep/ReconstructedParticle.h"
#include "edm4hep/Vector3f.h"
#include <vector>
#include <TLorentzVector.h>


DECLARE_COMPONENT(LeptonPairingAlg)

using namespace edm4hep;

template<class T>
double inv_mass(T* p1, T* p2){
  double e = p1->getEnergy()+p2->getEnergy() ;
  double px = p1->getMomentum()[0]+p2->getMomentum()[0];
  double py = p1->getMomentum()[1]+p2->getMomentum()[1];
  double pz = p1->getMomentum()[2]+p2->getMomentum()[2];
  return( sqrt( e*e - px*px - py*py - pz*pz  ) );
}


LeptonPairingAlg::LeptonPairingAlg(const std::string& aName, ISvcLocator* aSvcLoc) : GaudiAlgorithm(aName, aSvcLoc) {
  declareProperty("RecoParticleColl", m_recoParticleCollHandle, "RecoParticle collection");
  declareProperty("IsolatedLeptonsColl", m_isolatedLeptonsCollHandle, "Isolated Leptons collection");
  declareProperty("PFOsWOIsoLepColl", m_PFOsWOIsoLepCollHandle, "Isolated Leptons collection");
  declareProperty("doPhotonRecovery", m_doPhotonRecovery, "Do Photon Recovery");
  declareProperty("diLeptinInvariantMass", m_diLepInvMass, "Di-lepton Invariant Mass");
}

LeptonPairingAlg::~LeptonPairingAlg(){
} // destructor

StatusCode LeptonPairingAlg::initialize() {
  return StatusCode::SUCCESS; 
} // initialize()

StatusCode LeptonPairingAlg::execute() {
  const auto *isoLeptonColl = m_isolatedLeptonsCollHandle.get();
  int nLeptons = isoLeptonColl->size();
  if (nLeptons > 1) {

    std::vector< ReconstructedParticle > LeptonPair = {};
    int _lepton_type;
     double cosFSRCut; // the angle of BS and FSR around the direction of charged lepton

     if (m_doPhotonRecovery) cosFSRCut = 0.99;

     if (nLeptons == 2) {
       const ReconstructedParticle lepton1 = isoLeptonColl->at( 0 );
       const ReconstructedParticle lepton2 = isoLeptonColl->at( 1 );
       //Check if same type and have opposite charge
       if (lepton1.getType() + lepton2.getType() == 0) {
	 _lepton_type = abs(lepton1.getType());
	 LeptonPair = {lepton1, lepton2};
	 
	 float pairmass = inv_mass(&lepton1, &lepton2);
	 float delta = fabs(pairmass-m_diLepInvMass);
	 std::cout << "invariant mass " << pairmass << " " << delta << std::endl;      
	
       }
     } else {
       float mindelta = 99999.;
       for ( int i_lep1 = 0 ; i_lep1 < nLeptons - 1; ++i_lep1 ) {
	   const ReconstructedParticle lepton1 = isoLeptonColl->at( i_lep1 );
	   for ( int i_lep2 = i_lep1 + 1 ; i_lep2 < nLeptons ; ++i_lep2 ) {
	     const ReconstructedParticle lepton2 = isoLeptonColl->at( i_lep2 );
	     //Check if same type and have opposite charge 
	     if (lepton1.getType() + lepton2.getType() == 0) {
	       _lepton_type = abs(lepton1.getType());
	       float pairmass = inv_mass(&lepton1, &lepton2);
	       float delta = abs(pairmass-m_diLepInvMass);
	       if (delta > mindelta) continue;
	       mindelta = delta;  
	       LeptonPair = {lepton1, lepton2};
	     } 
	   }
       }
     } // if  (nLeptons == 2)
     std::vector<ReconstructedParticle*> photons;
     if (LeptonPair.size() == 2) {
       const auto *PFOsWOIsoLepCollection = m_PFOsWOIsoLepCollHandle.get();
       // recovery of FSR and BS
       MutableReconstructedParticle recoLepton1 = LeptonPair[0].clone();
       this->doPhotonRecovery(&(LeptonPair[0]), PFOsWOIsoLepCollection, &recoLepton1,cosFSRCut, photons);
       MutableReconstructedParticle recoLepton2 = LeptonPair[1].clone();
       this->doPhotonRecovery(&(LeptonPair[1]), PFOsWOIsoLepCollection, &recoLepton2,cosFSRCut, photons);
    
       //m_LepPairCollection->push_back(recoLepton1);
       //m_LepPairCollection->push_back(recoLepton2);
     }
     
    
  } // if (isoLeptonColl->size() > 1)
  return StatusCode::SUCCESS; 
} // execute()


StatusCode LeptonPairingAlg::finalize() { 
  return StatusCode::SUCCESS; 
} // finalize()


float LeptonPairingAlg::dotProduct(Vector3f v1, Vector3f v2) {
  return v1[0] * v2[0] + v1[1] * v2[1] * v1[2] * v2[2];
}


void LeptonPairingAlg::doPhotonRecovery(edm4hep::ReconstructedParticle* lepton,
					const edm4hep::ReconstructedParticleCollection* pfoCollection,
					edm4hep::MutableReconstructedParticle* recoLepton,
					double cosFSRCut,
					std::vector<edm4hep::ReconstructedParticle*> &photons) {
  // recover the BS and FSR photons
  TLorentzVector* lorentzLepton = new TLorentzVector(lepton->getMomentum()[0], lepton->getMomentum()[1], lepton->getMomentum()[2], static_cast<double>(lepton->getEnergy()));
  std::array _tmpArray = lepton->getCovMatrix();
  std::vector<float> leptonCovMat(_tmpArray.begin(), _tmpArray.end());


  for (const auto pfo : *pfoCollection) {
    if (pfo.getType() == 22) {
      Vector3f photonMomentum = pfo.getMomentum();
      Vector3f leptonMomentum = lepton->getMomentum();
      auto _tmp1 = this->dotProduct(photonMomentum, leptonMomentum);
      auto _tmp2 = sqrt(this->dotProduct(photonMomentum, photonMomentum)) * sqrt(this->dotProduct(leptonMomentum, leptonMomentum));
      auto cosLeptonPhoton = _tmp1 / _tmp2;
      std::cout << "cos lepton photon " << cosLeptonPhoton << std::endl;
    } // pfo == 22
  } // pfo loop
 

  
  
  /*  recoLepton->addParticle(lepton);
  int nPFOs = colPFO->getNumberOfElements();
  for (int i = 0; i < nPFOs; i++) {
    ReconstructedParticle *recPart = dynamic_cast<ReconstructedParticle*>(colPFO->getElementAt(i));
    if (recPart == electron) continue;
    if (isolep::isFoundInVector(recPart,photons)) continue;
    Bool_t isFSR = isolep::getFSRTag(electron,recPart,fCosFSRCut);
    if (! isFSR) continue;
    photons.push_back(recPart);
    recoElectron->addParticle(recPart);
    if (lepType == 11) {
      // do split algorithm only for electron
      Bool_t isSplit = isolep::getSplitTag(electron,recPart);
      if (isSplit) continue;
    }
    else if (lepType == 13) {
    }
    lortzElectron += TLorentzVector(recPart->getMomentum(),recPart->getEnergy());
    std::transform(electronCovMat.begin(), electronCovMat.end(), recPart->getCovMatrix().begin(), 
		   electronCovMat.begin(), std::plus<float>());
  }
  Double_t energy = lortzElectron.E();
  Double_t mass   = lortzElectron.M();
  Double_t momentum[3] = {lortzElectron.Px(),lortzElectron.Py(),lortzElectron.Pz()};
  Double_t charge = electron->getCharge();
  recoElectron->setMomentum(momentum);
  recoElectron->setEnergy(energy);
  recoElectron->setMass(mass);
  recoElectron->setCharge(charge);
  recoElectron->setType(94);
  recoElectron->setCovMatrix(electronCovMat);
  */
}

