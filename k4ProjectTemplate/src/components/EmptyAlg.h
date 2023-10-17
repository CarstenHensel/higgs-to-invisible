#pragma once

// GAUDI
#include "Gaudi/Property.h"
#include "GaudiAlg/GaudiAlgorithm.h"

#include "edm4hep/ReconstructedParticleCollection.h"
#include "k4FWCore/DataHandle.h"

#include "TFile.h"
#include "TH1.h"
#include "TNtuple.h"

class EmptyAlg : public GaudiAlgorithm {
public:
  explicit EmptyAlg(const std::string&, ISvcLocator*);
  virtual ~EmptyAlg();
  /**  Initialize.
   *   @return status code
   */
  StatusCode initialize() final;
  /**  Execute.
   *   @return status code
   */
  StatusCode execute() final;
  /**  Finalize.
   *   @return status code
   */
  StatusCode finalize() final;

private:
  // member variable
  DataHandle<edm4hep::ReconstructedParticleCollection> m_recoParticleCollHandle{
      "ReconstructedParticleCollection", Gaudi::DataHandle::Reader, this};

  DataHandle<edm4hep::ReconstructedParticleCollection> m_jetsCollectionHandle{
      "Jets", Gaudi::DataHandle::Writer, this};

  int m_event_counter = 0;	

  int m_member = 0;
  typedef std::map<std::string, TH1*> HistoMap;
  HistoMap histos;
  void fillHisto(std::string key, double value);
  void fillHisto(const char *name, const char *title, int nbinsx, double xlow, double xup, double value);
  double calcInvariantMass();
};
