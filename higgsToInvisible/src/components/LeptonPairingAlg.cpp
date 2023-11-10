#include "LeptonPairingAlg.h"
#include "edm4hep/ReconstructedParticle.h"
#include <vector>

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

     double cosFSRCut; // the angle of BS and FSR around the direction of charged lepton

     if (m_doPhotonRecovery) cosFSRCut = 0.99;

     if (nLeptons == 2) {
       const ReconstructedParticle lepton1 = isoLeptonColl->at( 0 );
       const ReconstructedParticle lepton2 = isoLeptonColl->at( 1 );
       //Check if same type and have opposite charge
       if (lepton1.getType() + lepton2.getType() == 0) {
	 LeptonPair = {lepton1, lepton2};
	
       }
     } else {
       float mindelta = 99999.;
       for ( int i_lep1 = 0 ; i_lep1 < nLeptons - 1; ++i_lep1 ) {
	   const ReconstructedParticle lepton1 = isoLeptonColl->at( i_lep1 );
	   for ( int i_lep2 = i_lep1 + 1 ; i_lep2 < nLeptons ; ++i_lep2 ) {
	     const ReconstructedParticle lepton2 = isoLeptonColl->at( i_lep2 );
	     //Check if same type and have opposite charge 
	     if (lepton1.getType() + lepton2.getType() == 0) {
	       float pairmass = inv_mass(&lepton1, &lepton2);
	       float delta = abs(pairmass-m_diLepInvMass);
	       if (delta > mindelta) continue;
	       mindelta = delta;  
	       LeptonPair = {lepton1, lepton2};
	     } 
	   }
       }
     }

     
    
  } // if (isoLeptonColl->size() > 1)
  return StatusCode::SUCCESS; 
} // execute()


StatusCode LeptonPairingAlg::finalize() { 
  return StatusCode::SUCCESS; 
} // finalize()


