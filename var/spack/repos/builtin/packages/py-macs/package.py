# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMacs(PythonPackage):
    """MACS Model-based Analysis of ChIP-Seq.

    py-macs and py-macs2 are hosted in the same git repository,
    but no files clash and they can be activated simultaneously.
    py-macs (v1) is kept around as the results are different.
    """

    homepage = "http://liulab.dfci.harvard.edu/MACS/index.html"
    url      = "https://github.com/downloads/taoliu/MACS/MACS-1.4.2-1.tar.gz"

    version('1.4.2-1',
            '950dab09fe1335c8bbb34a896c21e3e2')

    depends_on('python@2.6:2.7')
