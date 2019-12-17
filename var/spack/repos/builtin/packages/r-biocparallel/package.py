# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RBiocparallel(RPackage):
    """This package provides modified versions and novel implementation of
       functions for parallel evaluation, tailored to use with Bioconductor
       objects."""

    homepage = "https://bioconductor.org/packages/BiocParallel/"
    git      = "https://git.bioconductor.org/packages/BiocParallel.git"
    url      = "https://bioconductor.org/packages/3.10/bioc/src/contrib/BiocParallel_1.20.0.tar.gz"

    version('1.20.0', sha256='9aff5449e966c6301288edbcee17e37a0ff8f2eda7d544bb47b627044853f6f1')
    version('1.14.2', commit='1d5a44960b19e9dbbca04c7290c8c58b0a7fc299')
    version('1.10.1', commit='a76c58cf99fd585ba5ea33065649e68f1afe0a7d')

    depends_on('r-futile-logger', type=('build', 'run'))
    depends_on('r-snow', type=('build', 'run'))
    depends_on('r-bh', type=('build', 'link', 'run'), when='@1.14.2:')
    depends_on('r@3.4.0:3.4.9', when='@1.10.1', type=('build', 'run'))
    depends_on('r@3.5.0:3.5.9', when='@1.14.2', type=('build', 'run'))
    depends_on('r@3.0:', when='@1.20.0', type=('build', 'run'))
