Author: Giulia Ripellino

Contact: giulia.ripellino@cern.ch

This folder will allow you to create your own madgraph sample for exotic Higgs decays.

TO DO: What final states do we want to generate?

First, set up the FCC analysis environment (necessary e.g to enable use of python 3.7 which is needed for MagGraph):

(This needs to be done every new log in?)

```
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
export PYTHONPATH=/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccanalyses-0.2.0pre02-6kok72w65toi2vvgedijdoqnd4hgg2wu/python:$PYTHONPATH
export PATH=/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccanalyses-0.2.0pre02-6kok72w65toi2vvgedijdoqnd4hgg2wu/python/bin:$PATH
```

Now download the latest version of madgraph (http://madgraph.phys.ucl.ac.be/ or directly at https://launchpad.net/mg5amcnlo). Here we're using MadGraph5 v3.4.0. 

Copy the Madgraph tarball to your local area on lxplus:

```
scp MG5_aMC_v3.4.0.tar username@lxplus.cern.ch:/path/to/your/dir
```

Then ssh to lxplus and unzip the tarball 
```
tar -xf MG5_aMC_v3.4.0.tar
```

Then download the HAHM_MG5model_v1 model from http://insti.physics.sunysb.edu/~curtin/hahm_mg.html. Copy to lxplus and unzip with the same procedure.

Move the HAHM_variableMW_UFO and HAHM_variablesw_UFO into the Madgraph5 models directory: `MG5_aMC_v3_4_0/models/`.

Down below follows instructions how to generate samples for exotic Higgs decays by directly changing in the param_card. For instructions on how to generate samples with a processcard instead see further down.

Now run:
```
cd MG5_aMC_v3_4_0
./bin/mg5_aMC
```

Then enter (for Higgs to dark photons):
```
set auto_convert_model T
import model --modelname HAHM_variableMW_UFO
generate h > zp zp 
output PROC_HAHM_variableMW_UFO_DarkPhoton
```

or (for Higgs to scalars)
```
generate h > hs hs 
output PROC_HAHM_variableMW_UFO_DarkScalar
```

Now set parameters in `PROC_HAHM_variableMW_UFO_<Model>/Cards/param_card.dat`:

For scalar case: Set epsilon=1.000000e-09 and mZD=1.000000e+03

For dark photon case: kap = 1.000000e-09 and MHS=1.000000e+03 

Now run
```
./bin/mg5_aMC mg5_proc_card.dat
```
to create the LHE file, where `mg5_proc_card.dat` is the madgraph proc card you are interested in generating.

The resulting events will be stored in `PROC_HAHM_variableMW_UFO_DarkScalar/Events/run_01/unweighted_events.lhe.gz` file.

Unzip it (`gunzip unweighted_events.lhe.gz`) and give the *absolute* path to DarkScalar_pythia.cmnd file to generate the delphes root file.

You also need to grab the latest official Delphes card and edm4hep tcl file:
```
#cd to one directory up from FCCeePhysicsPerformance/
git clone https://github.com/HEP-FCC/FCC-config.git
cd FCC-config/
git checkout spring2021
cd ../FCCeePhysicsPerformance/case-studies/BSM/LLP/ExoticHiggsDecays/SampleGeneration/
```

To create delphes root file you need to do the following on your command line:

```
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
DelphesPythia8_EDM4HEP ../../../../../../FCC-config/FCCee/Delphes/card_IDEA.tcl ../../../../../../FCC-config/FCCee/Delphes/edm4hep_IDEA.tcl MG5_aMC_v3_4_0/DarkScalar_pythia.cmnd DarkScalar.root
```

This will crash because of some Pythia version issue: https://answers.launchpad.net/mg5amcnlo/+question/263774

Therefore change the first line of header of your .lhe file

LesHouchesEvents version=“3.0” —> LesHouchesEvents version=“2.0”

Do not open the file in an editor, will take forever to open. Change it in emacs or wim or similar.

The resulting DarkScalar.root is your EDM sample!

--------
Creating samples using a processcard. The instructions below uses MadGraph v3.4.1 but otherwise the first part is exactly the same.
In this folder there is a prototype processcard named "testDarkScalar_proc_card_mg5.dat" generating the process e+ e- -> Z -> Z h with Z -> e+ e-/mu+ mu- and h -> 2hs -> 4b at the center-of-mass energy 240 GeV.
The mass of the dark scalar is set to 20 GeV and the kinetic mixing coupling kappa to 0.01, see the processcard for more details.

Put this processcard in your MG5_aMC_v3_4_1 directory and run:

```
# standing in directory MG5_aMC_v3_4_1
./bin/mg5_aMC testDarkScalar_proc_card_mg5.dat
```

The resulting events will be stored in `HS_zll_HSbbbb_mHS20GeV/Events/run_01/unweighted_events.lhe.gz` file.
Unzip it and give the *absolute* path to the DarkScalar_pythia.cmnd file to generate the delphes root file.

```
# standing in directory MG5_aMC_v3_4_1/HS_zll_HSbbbb_mHS20GeV/Events/run_01/
gunzip -c unweighted_events.lhe.gz > your/path/to/SampleGeneration/HS_zll_HSbbbb_mHS20GeV.lhe
```

Change the first line of header of your .lhe file

LesHouchesEvents version=“3.0” —> LesHouchesEvents version=“2.0”

Then do the same procedure as above:

You also need to grab the latest official Delphes card and edm4hep tcl file:
```
#cd to one directory up from FCCeePhysicsPerformance/
git clone https://github.com/HEP-FCC/FCC-config.git
cd FCC-config/
git checkout spring2021
cd ../FCCeePhysicsPerformance/case-studies/BSM/LLP/ExoticHiggsDecays/SampleGeneration/
```

To create delphes root file you need to do the following on your command line (make sure you have the .lhe file and the .cmnd file in the same directory as you are running in):

```
# standing in FCCeePhysicsPerformance/case-studies/BSM/LLP/ExoticHiggsDecays/SampleGeneration/
source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
DelphesPythia8_EDM4HEP ../../../../../../FCC-config/FCCee/Delphes/card_IDEA.tcl ../../../../../../FCC-config/FCCee/Delphes/edm4hep_IDEA.tcl DarkScalar_pythia.cmnd DarkScalar.root
```

The resulting DarkScalar.root is your EDM sample!




