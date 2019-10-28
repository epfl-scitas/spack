# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Polymake(Package):
    """polymake is open source software for research in polyhedral geometry"""
    homepage = "https://polymake.org/doku.php"
    url      = "https://polymake.org/lib/exe/fetch.php/download/polymake-3.0r1.tar.bz2"

    version('3.5', sha256='c649f8536ccef5a5e22b82c514a09278ebcd99d0815aa7170461fe12843109bd')
    version('3.0r2', '08584547589f052ea50e2148109202ab')
    version('3.0r1', '63ecbecf9697c6826724d8a041d2cac0')

    # Note: Could also be built with nauty instead of bliss
    depends_on("bliss")
    depends_on("boost")
    depends_on("cddlib")
    depends_on("gmp")
    depends_on("lrslib")
    depends_on("mpfr")
    depends_on("ninja", type='build', when='@3.2:')
    depends_on("perl")
    depends_on("perl-json")
    depends_on("perl-term-readkey")
    depends_on("perl-term-readline-gnu")
    depends_on("perl-xml-libxml")
    depends_on("perl-xml-libxslt")
    depends_on("perl-xml-writer")
    depends_on("ppl")
    depends_on("ppl@1.2:", when='@3.2:')
    depends_on("readline")

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix,
                  "--with-bliss=%s" % spec["bliss"].prefix,
                  "--with-boost=%s" % spec["boost"].prefix,
                  "--with-cdd=%s" % spec["cddlib"].prefix,
                  "--with-gmp=%s" % spec["gmp"].prefix,
                  "--with-lrs=%s" % spec["lrslib"].prefix,
                  "--with-mpfr=%s" % spec["mpfr"].prefix,
                  "--with-ppl=%s" % spec["ppl"].prefix)
        make()
        make("install")
