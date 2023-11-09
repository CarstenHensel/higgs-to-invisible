#include "LeptonPairing.h"

DECLARE_COMPONENT(LeptonPairing)

LeptonPairing::LeptonPairing(const std::string& aName, ISvcLocator* aSvcLoc) : GaudiAlgorithm(aName, aSvcLoc) {
  declareProperty("RecoParticleColl", m_recoParticleCollHandle, "RecoParticle collection");
  declareProperty("IsolatedLeptonsColl", m_isolatedLeptonsCollHandle, "Isolated Leptons collection");

}

StatusCode LeptonPairing::initialize() {
  m_event_counter = 0;
  return StatusCode::SUCCESS; 
} // initialize()

StatusCode LeptonPairing::execute() { 
  return StatusCode::SUCCESS; 
} // execute()


StatusCode LeptonPairing::finalize() { 
  return StatusCode::SUCCESS; 
} // finalize()


