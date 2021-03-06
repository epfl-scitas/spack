# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import argparse

import llnl.util.tty as tty

import spack.cmd
import spack.environment as ev
from spack.filesystem_view import YamlFilesystemView

description = "activate a package extension"
section = "extensions"
level = "long"


def setup_parser(subparser):
    subparser.add_argument(
        '-f', '--force', action='store_true',
        help="activate without first activating dependencies")
    subparser.add_argument(
        '-v', '--view', metavar='VIEW', type=str,
        help="the view to operate on")
    subparser.add_argument(
        'spec', nargs=argparse.REMAINDER,
        help="spec of package extension to activate")


def activate(parser, args):

    # Somehow activation is sensible to quoting on the command line
    # The code below is a quick fix to parse the spec as if it was unquoted,
    # and work around a subtle bug. The bug itself is still to be found
    pieces = []
    for x in args.spec:
        pieces.extend(x.split())
    args.spec = pieces

    specs = spack.cmd.parse_specs(args.spec)
    if len(specs) != 1:
        tty.die("activate requires one spec.  %d given." % len(specs))

    env = ev.get_env(args, 'activate')
    spec = spack.cmd.disambiguate_spec(specs[0], env)
    if not spec.package.is_extension:
        tty.die("%s is not an extension." % spec.name)

    if args.view:
        target = args.view
    else:
        target = spec.package.extendee_spec.prefix

    view = YamlFilesystemView(target, spack.store.layout)

    if spec.package.is_activated(view):
        tty.msg("Package %s is already activated." % specs[0].short_spec)
        return

    # TODO: refactor FilesystemView.add_extension and use that here (so there
    # aren't two ways of activating extensions)
    spec.package.do_activate(view, with_dependencies=not args.force)
