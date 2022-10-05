source /cvmfs/fcc.cern.ch/sw/latest/setup.sh
export PYTHONPATH=/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccanalyses-0.2.0pre02-6kok72w65toi2vvgedijdoqnd4hgg2wu/python:$PYTHONPATH
export PATH=/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccanalyses-0.2.0pre02-6kok72w65toi2vvgedijdoqnd4hgg2wu/python/bin:$PATH

fccanalysis run analysis_stage1.py --output dataFrame.root --files-list DarkScalar_v2.root

python plots.py