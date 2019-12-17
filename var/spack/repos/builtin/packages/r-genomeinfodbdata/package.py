# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGenomeinfodbdata(RPackage):
    """for mapping between NCBI taxonomy ID and species. Used by functions
       in the GenomeInfoDb package."""

    homepage = "https://bioconductor.org/packages/GenomeInfoDbData/"
    url      = "https://bioconductor.org/packages/3.10/data/annotation/src/contrib/GenomeInfoDbData_1.2.2.tar.gz"

    version('1.2.2', sha256 = "6853c968d79f033050a6d2aee6370c491e6512d28031cecac3bd14e7834af711")
    version('1.1.0', '6efdca22839c90d455843bdab7c0ecb5d48e3b6c2f7b4882d3210a6bbad4304c',
            url='https://bioconductor.org/packages/3.7/data/annotation/src/contrib/GenomeInfoDbData_1.1.0.tar.gz')
    version('0.99.0', '85977b51061dd02a90153db887040d05',
            url='https://bioconductor.org/packages/3.5/data/annotation/src/contrib/GenomeInfoDbData_0.99.0.tar.gz')

    depends_on('r@3.4.0:3.4.9', when='@0.99.0', type=('build', 'run'))
    depends_on('r@3.5.0:3.5.9', when='@1.1.0', type=('build', 'run'))
    depends_on('r@3.5.0:', when='@1.2.2', type=('build', 'run'))
