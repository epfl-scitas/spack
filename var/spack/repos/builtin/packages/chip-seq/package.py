# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ChipSeq(MakefilePackage):
    """The ChIP-Seq software provides methods for the analysis of ChIP-seq data
     and other types of mass genome annotation data."""

    homepage = "https://ccg.epfl.ch/chipseq"
    url      = "https://sourceforge.net/projects/chip-seq/files/chip-seq/1.5.5/chip-seq.1.5.5.tar.gz/download"

    version('1.5.5', '4e08c0558e2304415c766fa0bd3cbebd')
    version('1.5.4', 'faf1098bfd4e32a23c0a92309b81b2df')
    version('1.5.3', 'e60bc8392cb9ca9a661b3ea68f668184')

    depends_on('perl', type=('run',))

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        if '@:1.5.4' in self.spec:
            makefile.filter('binDir = .*', 'binDir = ' + self.prefix.bin)
            makefile.filter('mv', 'mkdir -p ${binDir}; mv')
        makefile.filter('CC = .*', 'CC = ' + env['CC'])

    @property
    def install_targets(self):
        targets = []
        if '@1.5.5:' in self.spec:
            targets = [
                'prefix={0}'.format(self.prefix), 'install-man', 'install-dat'
            ]

        targets += ['install']

        return targets
