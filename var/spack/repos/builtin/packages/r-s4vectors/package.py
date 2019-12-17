# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RS4vectors(RPackage):
    """The S4Vectors package defines the Vector and List virtual classes and
       a set of generic functions that extend the semantic of ordinary
       vectors and lists in R. Package developers can easily implement
       vector-like or list-like objects as concrete subclasses of Vector or
       List. In addition, a few low-level concrete subclasses of general
       interest (e.g. DataFrame, Rle, and Hits) are implemented in the
       S4Vectors package itself (many more are implemented  in the IRanges
       package and in other Bioconductor infrastructure packages)."""

    homepage = "https://bioconductor.org/packages/S4Vectors/"
    git      = "https://git.bioconductor.org/packages/S4Vectors.git"
    url      = "https://bioconductor.org/packages/3.10/bioc/src/contrib/S4Vectors_0.24.1.tar.gz"

    version('0.24.1', sha256='fdbed7310cf01d4f62345f67c6efc3e31248bff7793fb897436f20fb06ad27e7')
    version('0.18.3', commit='d6804f94ad3663828440914920ac933b934aeff1')
    version('0.16.0', commit='00fec03fcbcb7cff37917fab0da28d91fdf9dc3d')
    version('0.14.7', commit='40af17fe0b8e93b6a72fc787540d2961773b8e23')

    depends_on('r-biocgenerics@0.21.1:', type=('build', 'run'), when='@0.14.7')
    depends_on('r-biocgenerics@0.23.3:', type=('build', 'run'), when='@0.16.0:0.18.3')
    depends_on('r-biocgenerics@0.31.1:', type=('build', 'run'), when='@0.24.1:')
    depends_on('r@3.4.0:3.4.9', when='@0.14.7', type=('build', 'run'))
    depends_on('r@3.5.0:3.5.9', when='@0.18.3', type=('build', 'run'))
    depends_on('r@3.6.0:', when='@0.24.1', type=('build', 'run'))
