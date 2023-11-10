#include "LeptonPairingAlg.h"

DECLARE_COMPONENT(LeptonPairingAlg)

LeptonPairingAlg::LeptonPairingAlg(const std::string& aName, ISvcLocator* aSvcLoc) : GaudiAlgorithm(aName, aSvcLoc) {
  declareProperty("RecoParticleColl", m_recoParticleCollHandle, "RecoParticle collection");
  declareProperty("IsolatedLeptonsColl", m_isolatedLeptonsCollHandle, "Isolated Leptons collection");

}

LeptonPairingAlg::~LeptonPairingAlg(){
} // destructor

StatusCode LeptonPairingAlg::initialize() {
  return StatusCode::SUCCESS; 
} // initialize()

StatusCode LeptonPairingAlg::execute() {
  const auto *isoLeptonColl = m_isolatedLeptonsCollHandle.get(); 
  if (isoLeptonColl->size() > 1) {
    
  } // if (isoLeptonColl->size() > 1)
  return StatusCode::SUCCESS; 
} // execute()


StatusCode LeptonPairingAlg::finalize() { 
  return StatusCode::SUCCESS; 
} // finalize()


