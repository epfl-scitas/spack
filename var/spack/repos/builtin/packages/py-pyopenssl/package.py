# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyopenssl(PythonPackage):
    """High-level wrapper around a subset of the OpenSSL library."""

    homepage = "https://pyopenssl.org/"
    url      = "https://pypi.io/packages/source/p/pyOpenSSL/pyOpenSSL-18.0.0.tar.gz"

    version('18.0.0', 'c92e9c85b520b7e153fef0f7f3c5dda7')

    depends_on('py-asn1crypto')
    depends_on('py-cffi')
    depends_on('py-cryptography@2.2.1:', when='@18.0.0:')
    depends_on('py-enum34')
    depends_on('py-idna')
    depends_on('py-ipaddress')
    depends_on('py-pycparser')
    depends_on('py-six@1.5.2:')
    depends_on('python@2.7:', when='@18.0.0:')
