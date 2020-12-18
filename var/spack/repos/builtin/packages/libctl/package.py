# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libctl(AutotoolsPackage):
    """libctl is a free Guile-based library implementing flexible
    control files for scientific simulations."""

    homepage = "http://ab-initio.mit.edu/wiki/index.php/Libctl"
    url      = "https://github.com/NanoComp/libctl/releases/download/v4.5.0/libctl-4.5.0.tar.gz"

    version('4.5.0', sha256='621e46a238c4d5e8ce0866183f8e04abac6e1a94d90932af0d56ee61370ea153')
    version('4.4.0', sha256='d44336bd1b75dfcd9b9f157518823b6290075eb2d45e7f90d55979e91815df94')
    version('4.3.0', sha256='c0ff5e0a3d81ed70240181552fe2c2381ed7928ea138115dcfa196e7310de674')
    version('3.2.2', '5fd7634dc9ae8e7fa70a68473b9cbb68',
            url='http://ab-initio.mit.edu/libctl/libctl-3.2.2.tar.gz')

    depends_on('guile')

    def configure_args(self):
        spec = self.spec

        return [
            '--enable-shared',
            'GUILE={0}'.format(join_path(
                spec['guile'].prefix.bin, 'guile')),
            'GUILE_CONFIG={0}'.format(join_path(
                spec['guile'].prefix.bin, 'guile-config')),
        ]
