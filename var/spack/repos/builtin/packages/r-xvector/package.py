# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RXvector(RPackage):
    """Memory efficient S4 classes for storing sequences "externally" (behind
       an R external pointer, or on disk)."""

    homepage = "https://bioconductor.org/packages/XVector/"
    git      = "https://git.bioconductor.org/packages/XVector.git"
    url      = "https://bioconductor.org/packages/3.10/bioc/src/contrib/XVector_0.26.0.tar.gz"

    version('0.26.0', sha256='675be1d93136a360dd84c525143e486d87292580f35873ff74aed0ef097a4f68')
    version('0.20.0', commit='a83a7ea01f6a710f0ba7d9fb021cfa795b291cb4')
    version('0.16.0', commit='54615888e1a559da4a81de33e934fc0f1c3ad99f')

    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-biocgenerics@0.19.2:', when='@0.20.0:', type=('build', 'run'))
    depends_on('r-s4vectors', type=('build', 'run'))
    depends_on('r-s4vectors@0.17.24:', when='@0.20.0', type=('build', 'run'))
    depends_on('r-s4vectors@0.21.13:', when='@0.26.0', type=('build', 'run'))
    depends_on('r-iranges', type=('build', 'run'))
    depends_on('r-iranges@2.13.16:', when='@0.20.0', type=('build', 'run'))
    depends_on('r-iranges@2.15.12:', when='@0.26.0', type=('build', 'run'))
    depends_on('r-zlibbioc', type=('build', 'run'))
    depends_on('r@3.4.0:3.4.9', when='@0.16.0', type=('build', 'run'))
    depends_on('r@3.5.0:3.5.9', when='@0.20.0', type=('build', 'run'))
    depends_on('r@2.8.0:', when='@0.20.0', type=('build', 'run'))
