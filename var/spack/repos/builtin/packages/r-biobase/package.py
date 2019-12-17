# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#
from spack import *


class RBiobase(RPackage):
    """Functions that are needed by many other packages
    or which replace R functions."""

    homepage = "https://www.bioconductor.org/packages/Biobase/"
    git      = "https://git.bioconductor.org/packages/Biobase.git"
    url      = "https://bioconductor.org/packages/3.10/bioc/src/contrib/Biobase_2.46.0.tar.gz"

    version('2.46.0', sha256='f4e1ad15ffc281c7f4b049b58a880ca987e12d61bb37cc772a95e2361008a4bf')
    version('2.40.0', commit='6555edbbcb8a04185ef402bfdea7ed8ac72513a5')
    version('2.38.0', commit='83f89829e0278ac014b0bc6664e621ac147ba424')
    version('2.36.2', commit='15f50912f3fa08ccb15c33b7baebe6b8a59ce075')

    depends_on('r-biocgenerics@0.16.1:', type=('build', 'run'))
    depends_on('r-biocgenerics@0.27.1:', when='@2.46.0:', type=('build', 'run'))
    depends_on('r@3.4.0:3.4.9', when='@2.36.2', type=('build', 'run'))
    depends_on('r@3.5.0:3.5.9', when='@2.40.0', type=('build', 'run'))
    depends_on('r@2.1.0:', when='@2.46.0', type=('build', 'run'))
