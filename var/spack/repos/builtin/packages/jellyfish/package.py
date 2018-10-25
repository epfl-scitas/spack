# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Jellyfish(AutotoolsPackage):
    """JELLYFISH is a tool for fast, memory-efficient counting of k-mers in
       DNA."""

    homepage = "http://www.cbcb.umd.edu/software/jellyfish/"
    url      = "https://github.com/gmarcais/Jellyfish/releases/download/v2.2.7/jellyfish-2.2.7.tar.gz"
    list_url = "http://www.cbcb.umd.edu/software/jellyfish/"

    version('2.2.10', '4001a6c2a4c588b20eafb66c9766f78f')
    version('2.2.9',  '3c3a406c69d18a47199e7f123abb2b49')
    version('2.2.8',  'f621078473740925ef493dff1a0ee2f6')
    version('2.2.7',  'f741192d9061f28e34cb67c86a1027ab',
            url='https://github.com/gmarcais/Jellyfish/releases/download/v2.2.7/jellyfish-2.2.7.tar.gz')
    version('1.1.12', '175e6fc48ca0b4ba845614cdb4467387')
    version('1.1.11', 'dc994ea8b0896156500ea8c648f24846',
            url='http://www.cbcb.umd.edu/software/jellyfish/jellyfish-1.1.11.tar.gz')

    depends_on('perl', type=('build', 'run'))
    depends_on('python', type=('build', 'run'))
