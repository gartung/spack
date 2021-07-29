# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libuuid(AutotoolsPackage):
    """Portable uuid C library"""

    homepage = "http://sourceforge.net/projects/libuuid/"
    url = "https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.32/util-linux-2.32.1.tar.gz"

    version('2.32.1', sha256='3bbf9f3d4a33d6653cf0f7e4fc422091b6a38c3b1195c0ee716c67148a1a7122')
    
    provides('uuid')

    def configure_args(self):
        args = ['--disable-all-programs', '--enable-libuuid']
        return args
