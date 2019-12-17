# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class REdger(RPackage):
    """Differential expression analysis of RNA-seq expression profiles with
       biological replication. Implements a range of statistical methodology
       based on the negative binomial distributions, including empirical Bayes
       estimation, exact tests, generalized linear models and quasi-likelihood
       tests. As well as RNA-seq, it be applied to differential signal analysis
       of other types of genomic data that produce counts, including ChIP-seq,
       SAGE and CAGE."""

    homepage = "https://bioconductor.org/packages/edgeR/"
    git      = "https://git.bioconductor.org/packages/edgeR.git"
    url      = "https://bioconductor.org/packages/3.10/bioc/src/contrib/edgeR_3.28.0.tar.gz"

    version('3.28.0', sha256='036ea5bf3b4fe2b6a0ea8f081e7d9071eb34d4ad132708763a2bcce89733f4d4')
    version('3.22.3', commit='e82e54afc9398ac54dc4caba0f7ae5c43e572203')
    version('3.18.1', commit='101106f3fdd9e2c45d4a670c88f64c12e97a0495')

    depends_on('r-limma@3.41.5:', type=('build', 'run'), when='@3.28')
    depends_on('r-limma@:3.41.4', type=('build', 'run'), when='@:3.27')
    depends_on('r-locfit', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'link', 'run'))

    depends_on('r@3.6.0:', when='@3.28.0')
    depends_on('r@3.5.0:3.5.9', when='@3.22.3')
    depends_on('r@3.4.0:3.4.9', when='@3.18.1')
