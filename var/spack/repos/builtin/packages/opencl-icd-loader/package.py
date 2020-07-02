# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class OpenclIcdLoader(CMakePackage):
    """Khronos Group OpenCL 1.2 installable client driver (ICD) loader"""

    homepage = "https://www.khronos.org/registry/OpenCL/"
    url      = "https://github.com/KhronosGroup/OpenCL-ICD-Loader/archive/v2020.06.16.tar.gz"

    version('2020.06.16', sha256='e7a0c161376bfb46b869e292d4593a64f4ff7b358837494a5f2d765d9a2af683')
    version('2020.03.13', sha256='cafcfa9e48d523d0534e6879af2badd7006b3c646eab5f05314de72a2c542816')

    depends_on('opencl-headers')
    provides('opencl@:2.2')
