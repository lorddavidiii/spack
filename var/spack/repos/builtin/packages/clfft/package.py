# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Clfft(CMakePackage, CudaPackage):
    """a software library containing FFT functions written in OpenCL"""

    homepage = "https://github.com/clMathLibraries/clFFT"
    git      = "https://github.com/bema-aei/clFFT.git"

    version("2.12.2", commit="de4cab2ec2a90078b827f9a480a446a009637f61")

    variant('client', default=False,
            description='build client and callback client')
    variant("cuda", default=True, description="Build with CUDA-openCL")

    depends_on('boost@1.33.0:', when='+client')

    root_cmakelists_dir = 'src'

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DBUILD_CLIENT:BOOL={0}'.format((
                'ON' if '+client' in spec else 'OFF')),
            '-DBUILD_CALLBACK_CLIENT:BOOL={0}'.format((
                'ON' if '+client' in spec else 'OFF'))
        ]
        return args
