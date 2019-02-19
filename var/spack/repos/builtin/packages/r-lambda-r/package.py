##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RLambdaR(RPackage):
    """A language extension to efficiently write functional programs in R.
       Syntax extensions include multi-part function definitions, pattern
       matching, guard statements, built-in (optional) type safety."""

    homepage = "https://cran.rstudio.com/web/packages/lambda.r/index.html"
    #url      = "https://cran.rstudio.com/src/contrib/lambda.r_1.2.tar.gz"
    url = "https://cran.r-project.org/src/contrib/Archive/lambda.r/lambda.r_1.2.tar.gz"

    #version('1.2.3', '662f16f71a65366e0492d43ad1523db7')
    version('1.2', 'bda49898b85ad5902880a31f43b432e2')
