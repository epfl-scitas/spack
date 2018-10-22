# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Sicer(Package):
    """A clustering approach for identification of enriched domains
    from histone modification ChIP-Seq data."""

    homepage = "https://home.gwu.edu/~wpeng/Software.htm"
    url      = "https://home.gwu.edu/~wpeng/SICER_V1.1.tgz"

    version('1.1', '1c146ffc9cdd90716a5d025171cba33b')

    depends_on('python',   type='run')
    depends_on('py-numpy', type='run')
    depends_on('py-scipy', type='run')

    def url_for_version(self, version):
        url = "https://home.gwu.edu/~wpeng/SICER_V{0}.tgz"
        return url.format(version.up_to(2))

    def install(self, spec, prefix):
        # everything must live under SICER
        install_tree('SICER', prefix.SICER)

        # replacing a placeholder path in all the scripts
        filter_file(r'/home/data/SICER1\.1', prefix,
                    *(find(prefix.SICER, '*.sh', recursive=True)),
                    backup=False)

        # one of the scripts is not executable by default
        set_executable(os.path.join(prefix.SICER, 'SICER.sh'))

        # link the main scripts from bin/ to avoid changing PATH
        mkdirp(prefix.bin)
        for f in find(prefix.SICER, '*.sh', recursive=False):
            os.symlink(f, os.path.join(prefix.bin, os.path.basename(f)))

        # utility/fragment-size-estimation.sh is broken (and left unlinked)
        # it could be patched and would introduce dependencies on
        # gnuplot and ghostscript
