# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class I7z(Package):
    """A better i7 (and now i3, i5) reporting tool for Linux."""

    homepage = "https://code.google.com/archive/p/i7z/"
    url      = "https://github.com/afontenot/i7z.git"

    version('afontenot', git="https://github.com/afontenot/i7z.git")
    version('epfl-scitas', git="https://github.com/epfl-scitas/i7z.git")

    depends_on('ncurses')

    def install(self, spec, prefix):
        make()
        make('prefix={0}'.format(prefix), 'install')
