# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gurobi(Package):
    """The Gurobi Optimizer was designed from the ground up to be the fastest,
    most powerful solver available for your LP, QP, QCP, and MIP (MILP, MIQP,
    and MIQCP) problems.

    Note: Gurobi is licensed software. You will need to create an account on
    the Gurobi homepage and download Gurobi Optimizer yourself. Spack will
    search your current directory for the download file. Alternatively, add
    this file to a mirror so that Spack can find it. For instructions on how to
    set up a mirror, see http://spack.readthedocs.io/en/latest/mirrors.html

    Please set the path to licence file with the following command (for bash)
    export GRB_LICENSE_FILE=/path/to/gurobi/license/. See section 4 in
    $GUROBI_HOME/docs/quickstart_linux.pdf for more details."""

    homepage = "http://www.gurobi.com/index"

    version('9.1.0', '628c4e2c6fc34193f9dd5852d34b3e1b')
    version('8.1.1', sha256='c030414603d88ad122246fe0e42a314fab428222d98e26768480f1f870b53484')
    version('7.5.2', sha256='d2e6e2eb591603d57e54827e906fe3d7e2e0e1a01f9155d33faf5a2a046d218e')

    # Licensing
    license_required = True
    license_files    = ['gurobi.lic']
    license_vars     = ['GRB_LICENSE_FILE']
    license_url      = 'http://www.gurobi.com/downloads/download-center'

    def url_for_version(self, version):
        url = "https://packages.gurobi.com/{0}/gurobi{1}_linux64.tar.gz"
        return url.format(version.up_to(2), version)

    def install(self, spec, prefix):
        install_tree('linux64', join_path(prefix, 'linux64'))

    def setup_environment(self, spack_env, run_env):
        run_env.set('GRB_LICENSE_FILE', join_path(prefix, 'gurobi.lic'))
        run_env.set('GUROBI_HOME', join_path(prefix, 'linux64'))
        run_env.prepend_path('PATH', join_path(prefix, 'linux64', 'bin'))
        run_env.prepend_path('LD_LIBRARY_PATH', join_path(prefix, 'linux64',
                                                          'lib'))
