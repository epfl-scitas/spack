# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mpb(AutotoolsPackage):
    """MPB is a free and open-source software package for computing electromagnetic
    band structures and modes."""

    homepage = "https://github.com/NanoComp/mpb"
    url      = "https://github.com/NanoComp/mpb/releases/download/v1.11.1/mpb-1.11.1.tar.gz"

    version('1.11.1', sha256='dc55b081c56079727dac92d309f8e4ea84ca6eea9122ec24b7955f8c258608e1')
    version('1.11.0', sha256='5852a0a40cd035ffcbab9cfdab759be731bfe1d9c8cc491120acbac26731d4a0')
    version('1.10.0', sha256='3cd3366aca40eacb8fc01476adfd9e376fd0f81ef6109cef4f85b15218a3514f')
    version('1.9.0',  sha256='c7b91d82bd8e63ea029d58cbf6d73904a99bc20436badf6aac30fc4a90850883')
    version('1.8.0',  sha256='2d2fa2a7b656057e8902665aa3f05e82a603f36bb5db17bc914663d3da59f9c9')

    variant('mpi',     default=True, description='Enable MPI support')
    variant('hdf5',    default=True, description='Enable HDF5 support')

    depends_on('blas')
    depends_on('lapack')
    depends_on('guile')
    depends_on('libctl@3.2:', when='@:1.11.0')
    depends_on('libctl@4.0.0:', when='@1.11.1:')
    depends_on('fftw')
    depends_on('mpi',         when='+mpi')
    depends_on('hdf5~mpi',    when='+hdf5~mpi')
    depends_on('hdf5+mpi',    when='+hdf5+mpi')

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--enable-shared'
        ]

        config_args.append('--with-blas={0}'.format(
            spec['blas'].libs))
        config_args.append('--with-lapack={0}'.format(
            spec['lapack'].libs))
        config_args.append('--with-libctl={0}'.format(
            join_path(spec['libctl'].prefix.share, 'libctl')))

        if spec.satisfies('^fftw@:2.99'):
            config_args.append('--with-fftw2')

        if '+mpi' in spec:
            config_args.append('--with-mpi')

        if '+hdf5' in spec:
            config_args.append('--with-hdf5')
        else:
            config_args.append('--without-hdf5')

        return config_args
