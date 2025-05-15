# higgs-to-invisible package


This repository can be a starting point and template for projects using the Key4HEP software stack.


## Dependencies

* ROOT

* PODIO

* Gaudi

* k4FWCore

## Installation


``` bash
bash
source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh
git clone https://github.com/CarstenHensel/higgs-to-invisible.git
cd higgs-to-invisible/
source setup.sh
mkdir build install
cd build;
cmake .. -DCMAKE_INSTALL_PREFIX=../install -DPython_EXECUTABLE=$(which python3)
make install
```

## Execute 

and then run the algorithm like this:

``` bash
k4run ../higgsToInvisible/options/higgsToInvisible.py
```


## References:
These could perhaps be usefule for newcomers.
1. [lhcb-98-064 COMP](https://cds.cern.ch/record/691746/files/lhcb-98-064.pdf)
2. [Hello World in the Gaudi Framework](https://lhcb.github.io/DevelopKit/02a-gaudi-helloworld)
