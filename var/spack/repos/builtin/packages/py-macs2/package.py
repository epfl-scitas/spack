# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMacs2(PythonPackage):
    """MACS Model-based Analysis of ChIP-Seq.

    py-macs and py-macs2 are hosted in the same git repository,
    but no files clash and they can be activated simultaneously.
    py-macs (v1) is kept around as the results are different.
    """

    homepage = "https://github.com/taoliu/MACS"
    url      = "https://pypi.io/packages/source/M/MACS2/MACS2-2.1.1.20160309.tar.gz"

    version('2.1.1.20160309',
            '2008ba838f83f34f8e0fddefe2a3a0159f4a740707c68058f815b31ddad53d26')           

    depends_on('python@2.7:2.8')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-numpy@1.6:', type=('build', 'run'))
