# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
from spack import *


class Meep(AutotoolsPackage):
    """Meep (or MEEP) is a free finite-difference time-domain (FDTD) simulation
    software package developed at MIT to model electromagnetic systems."""

    homepage = "http://ab-initio.mit.edu/wiki/index.php/Meep"
    url      = "https://github.com/NanoComp/meep/archive/v1.16.1.tar.gz"
    list_url = "http://ab-initio.mit.edu/meep/old"

    version('1.16.1', sha256='2ba80a09b0feb2ba64dd3422fa297ba87351bdf085d3d631f6ac220a8edae87d')
    version('1.16.0', sha256='03b8bccad3760cf08f342860d6a31bfe2cac6ebc5df8f324cc2bc87b9c374132')
    version('1.15.0', sha256='be50ccded3f1fb97e5c3a4e0351e2ff864d2a94c95ed80e29613d63a72c371f7')
    version('1.14.0', sha256='e3b37247a808d4450cc836aafae0156b18264af6ec22dd4ebff7292569f8d8c7')
    version('1.3',   '18a5b9e18008627a0411087e0bb60db5')
    version('1.2.1', '9be2e743c3a832ae922de9d955d016c5')
    version('1.1.1', '415e0cd312b6caa22b5dd612490e1ccf')

    variant('blas',    default=True, description='Enable BLAS support')
    variant('lapack',  default=True, description='Enable LAPACK support')
    variant('harminv', default=True, description='Enable Harminv support')
    variant('guile',   default=True, description='Enable Guilde support')
    # this is not optional since it is a dependency of the scheme and python
    # interfaces that cannot really by turned off
    # https://github.com/NanoComp/meep/blob/5ceb8ca73ec4c2113e47fcea07de70c184258d44/scheme/Makefile.am#L37
    # variant('libctl', default=True, description='Enable libctl support')
    variant('mpi',     default=True, description='Enable MPI support')
    variant('hdf5',    default=True, description='Enable HDF5 support')
    variant('gsl',     default=True, description='Enable GSL support')

    depends_on('m4', when='@1.3.1:')
    depends_on('autoconf', when='@1.3.1:')
    depends_on('automake', when='@1.3.1:')

    depends_on('blas',        when='+blas')
    depends_on('lapack',      when='+lapack')
    depends_on('harminv',     when='+harminv')
    depends_on('guile',       when='+guile')
    # according to the documentation meep need depends on libctl @4.0: but
    # according to the configure it is @4.2:
    # https://github.com/NanoComp/meep/commit/97f4df0453417ff5b3876524845cc80b79f835e7
    depends_on('libctl@4.2:', when='@1.8.0:')
    depends_on('libctl@4.1:', when='@1.5.0:1.7.0')
    depends_on('libctl@4.0:', when='@1.4.0:1.4.3')
    depends_on('libctl@3.2:', when='@:1.3')
    depends_on('mpi',         when='+mpi')
    depends_on('hdf5~mpi',    when='+hdf5~mpi')
    depends_on('hdf5+mpi',    when='+hdf5+mpi')
    depends_on('gsl',         when='+gsl')

    depends_on('mpb')
    depends_on('swig')
    # python is not a variant of this package but is someone wants to do it
    # mpb is required by default since the swig code does not compiles
    # without it it might be optional if python is optional
    #
    # `--with-python` is also a default of the configure
    extends('python')
    depends_on('py-numpy', type=('build', 'link', 'run'))

    # build in source fails do to symlink of a file created (materials.scm...)
    # this comes from
    # https://github.com/NanoComp/meep/commit/0f483e2f51fd5eaee92c5d6595f9026042daea61
    # if configure is done in the source tree it tries to replace the file
    # with by a symlink to itself, this results in bug:
    # https://github.com/NanoComp/meep/issues/837
    # that was reported by a spack user but discarded by the developers
    # as a system problem and not a bug
    @property
    def build_directory(self):
        return os.path.join(self.stage.path, 'spack-build')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--enable-shared'
        ]

        if '+blas' in spec:
            config_args.append('--with-blas={0}'.format(
                spec['blas'].libs))
        else:
            config_args.append('--without-blas')

        if '+lapack' in spec:
            config_args.append('--with-lapack={0}'.format(
                spec['lapack'].libs))
        else:
            config_args.append('--without-lapack')

        if '+libctl' in spec:
            config_args.append('--with-libctl={0}'.format(
                join_path(spec['libctl'].prefix.share, 'libctl')))
        else:
            config_args.append('--without-libctl')

        if '+mpi' in spec:
            config_args.append('--with-mpi')
        else:
            config_args.append('--without-mpi')

        if '+hdf5' in spec:
            config_args.append('--with-hdf5')
        else:
            config_args.append('--without-hdf5')

        # `--with-scheme` need maintainer mode to compile and is on by default
        # https://github.com/NanoComp/meep/blob/5ceb8ca73ec4c2113e47fcea07de70c184258d44/scheme/Makefile.am#L32
        # `--without-scheme` is not an option since it makes the compilation fail
        # with some swig errors
        config_args.append('--enable-maintainer-mode')

        return config_args

    def check(self):
        spec = self.spec

        # aniso_disp test fails unless installed with harminv
        # near2far test fails unless installed with gsl
        if '+harminv' in spec and '+gsl' in spec:
            # Most tests fail when run in parallel
            # 2D_convergence tests still fails to converge for unknown reasons
            make('check', parallel=False)
