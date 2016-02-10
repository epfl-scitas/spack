import os
import llnl.util.tty as tty

from spack import *


class Intelmpi(Package):
    """
    Intel (R) MPI Library 5.1 focuses on making applications perform better on Intel (R) architecture based
    clusters implementing the high performance Message Passing Interface Version 3.0 specification on multiple fabrics.
    It enables you to quickly deliver maximum end user performance even if you change or upgrade to new interconnects,
    without requiring changes to the software or operating environment.
    """
    homepage = 'https://software.intel.com/en-us/intel-mpi-library'
    url = 'fakeurl'
    licensed = True
    only_binary = True

    version('5.1.1')

    provides('mpi')

    def install(self, spec, prefix):
        tty.message('mpi : using Intel MPI external package')

    def setup_dependent_environment(self, module, spec, dep_spec):
        """
        For dependencies, make mpicc's use spack wrapper.
        """
        os.environ['MPICH_CC']  = 'icc'
        os.environ['MPICH_CXX'] = 'icpc'
        os.environ['MPICH_F77'] = 'ifort'
        os.environ['MPICH_F90'] = 'ifort'

        os.environ['I_MPI_ROOT'] = '/ssoft/intelmpi/5.1.1/RH6/all/x86_E5v2/impi/5.1.1.109'
        os.environ['I_MPI_PMI_LIBRARY'] = '/usr/lib64/libpmi.so'
        os.environ['I_MPI_FABRICS'] = 'shm:tmi'
        os.environ['IPATH_NO_CPUAFFINITY'] = '1'

        os.environ['LD_LIBRARY_PATH'] = '/ssoft/intel/15.0.0/RH6/all/x86_E5v2/composer_xe_2015.2.164/ipp/lib/intel64:/ssoft/intel/15.0.0/RH6/all/x86_E5v2/composer_xe_2015.2.164/tbb/lib/intel64/gcc4.4:/ssoft/intel/15.0.0/RH6/all/x86_E5v2/composer_xe_2015.2.164/mkl/lib/intel64:/ssoft/intel/15.0.0/RH6/all/x86_E5v2/composer_xe_2015.2.164/compiler/lib/intel64:/ssoft/intelmpi/5.1.1/RH6/all/x86_E5v2/impi/5.1.1.109/lib64/'
        #module.mpicc = join_path(self.prefix.bin, 'mpicc')
