import os
import multiprocessing

from avocado import Test
from avocado.utils import build
from avocado.utils import process


class QEMUBuild(Test):

    def setUp(self):
        source_location = os.path.expanduser("~/src/qemu")
        os.chdir(source_location)
        process.run("git checkout master")
        process.run("git pull")

    def test(self):
        source_location = os.path.expanduser("~/src/qemu")
        configure_parameters = "--cc=/bin/ccache"
        build_dir = os.path.join(source_location, "build")

        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
        os.chdir(build_dir)

        configure_location = os.path.join(source_location, "configure")
        configure_command = "%s %s" % (configure_location,
                                       configure_parameters)

        process.run(configure_command)
        build.make(build_dir,
                   extra_args="-j%s" % multiprocessing.cpu_count())

        arch = target.split("-")[0]
        qemu_executable = os.path.join(build_dir,
                                       target, "qemu-system-%s" % arch)
        process.run("%s --version" % qemu_executable)
