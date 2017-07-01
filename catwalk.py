#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  catwalk.py - learning how to climb trees. ;-)
#
#  This little ditty does a recursive listing of the contents of
#  the argument given in os.walk(), but only prints out those
#  matching pattern (in this case, files ending in .asc)
#
#  Copyright 2009 Kevin Cole <kevin.cole@novawebcoop.org> 2009.07.01
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#
#


from   __future__ import print_function
from   six.moves  import input           # use raw_input when I say input
from   os.path    import expanduser      # Cross-platform home directory finder
from   os.path    import join
import os
import sys
import re

__appname__    = "catwalk"
__author__     = "Kevin Cole"
__agency__     = "NOVA Web Development, LLC"
__copyright__  = "Copyright \N{copyright sign} 2009"
__credits__    = ["Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Kevin Cole"
__email__      = "kevin.cole@novawebdevelopment.org"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""


def fetch(root, targets):
    """
    Returns a list of fully qualified filenames under 'root' that
    match the regular expression provided by 'targets'
    """
    for path, dirs, files in os.walk(root):
        for file in files:
            if not targets.search(file):  # Skip files that don't match
                continue
            yield join(path, file)         # Like "%s/%s" % (path, file)


def main():
    _ = os.system("clear")
    print("{0} v.{1}\n{2} ({3})\n{4}, {5} <{6}>\n"
          .format(__appname__,
                  __version__,
                  __copyright__,
                  __license__,
                  __author__,
                  __agency__,
                  __email__))

#   tree = "/home/kjcole/Projects/Morphilios/luthor/database"
#   pattern = re.compile(r"(morf|syll|word)-[AB]-\w{4}\.asc$")  # File regex
#   pattern = re.compile(r"(lex|voc|nov)-[AB]-\w{4}\.asc$")     # File regex
    tree = input("Root directory:    ")
    regex = input("Filename pattern: ")
    pattern = re.compile(regex)

    for nextfile in fetch(tree, pattern):
        print(nextfile)
        fi = open(nextfile, "r")
        try:
            for line in fi:
                print(line[:-1])
        except UnicodeDecodeError:
            print("{0} has text encoding errors.".format(nextfile))
            sys.exit(1)
        fi.close()
        #input("Continue? ")

    print("-" * 78)
    return 0


if __name__ == "__main__":
    main()
