# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCoveralls(PythonPackage):
    """Seamless integration of coveralls.io with coverage.py."""

    homepage = "https://github.com/coveralls-clients/coveralls-python"
    url      = "https://pypi.io/packages/source/c/coveralls/coveralls-1.5.1.tar.gz"

    version('1.5.1', 'df04fe62f9c69ec736ea65f06c9f42dd')

    depends_on('py-certifi')
    depends_on('py-chardet')
    depends_on('py-coverage')
    depends_on('py-docopt')
    depends_on('py-pyopenssl@0.14:')
    depends_on('py-requests')
    depends_on('py-urllib3')
