# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Tophat(AutotoolsPackage):
    """TopHat is a fast splice junction read mapper for RNA-Seq.

     It aligns RNA-Seq reads to mammalian-sized genomes using the ultra
     high-throughput short read aligner Bowtie, and then analyzes the
     the mapping results to identify splice junctions between exons."""

    homepage = "http://ccb.jhu.edu/software/tophat/index.shtml"
    url      = "https://github.com/infphilo/tophat/archive/v2.1.1.tar.gz"

    version('2.1.2', 'db844fd7f53c519e716cd6222e6195b2')
    version('2.1.1', 'ffd18de2f893a95eb7e9d0c5283d241f')

    depends_on('autoconf', type='build')
    # 2.1.1 only builds with automake@1.15.1.  There's a patch here:
    # https://github.com/spack/spack/pull/8244, which was incorporated
    # upstream in 2.1.2, which is known to build with 1.16.1 and 1.15.1.
    depends_on('automake',                        type='build')
    depends_on('automake@1.15.1', when='@:2.1.1', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('boost@1.47:')
    depends_on('bowtie2', type='run')

    # uses make_pair which changed signature with C++14
    # a patch exists: https://github.com/DaehwanKimLab/tophat/pull/38
    # but there might be unexpected side effects
    # conflicts('%gcc@6:')

    parallel = False

    def configure_args(self):
        return ["--with-boost={0}".format(self.spec['boost'].prefix)]
