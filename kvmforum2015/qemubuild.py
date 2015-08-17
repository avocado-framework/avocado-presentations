import os
import multiprocessing

from avocado import Test, fail_on
from avocado.utils import build
from avocado.utils import process


class QEMUBuild(Test):

    """
    Builds QEMU from source (buildbot-like)
    """

    def setUp(self):
        # Getting parameters
        source_location = self.params.get("source_location",
                                          default="~/src/qemu")
        source_location = os.path.expanduser(source_location)
        git_branch = self.params.get("git_branch", default="master")
        git_pull = self.params.get("git_pull", default="True")

        # Real action
        os.chdir(source_location)
        process.run("git checkout %s" % git_branch)
        if git_pull == "True":
            process.run("git pull")


    @fail_on
    def test(self):
        # Getting parameters
        source_location = self.params.get("source_location", default="~/src/qemu")
        source_location = os.path.expanduser(source_location)
        configure_parameters = self.params.get("configure_parameters", default="")
        target = self.params.get("target", default="x86_64-softmmu")
        build_suffix = self.params.get("build_suffix", default="build")
        build_dir = os.path.join(source_location, build_suffix, target)

        # Real action
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
        os.chdir(build_dir)

        # Configure / make
        configure_location = os.path.join(source_location, "configure")
        configure_command = "%s %s" % (configure_location,
                                       configure_parameters)
        if target:
            configure_command = "%s --target-list=%s" % (configure_command,
                                                         target)
        process.run(configure_command)
        build.make(build_dir,
                   extra_args="-j%s" % multiprocessing.cpu_count())

        # Run what we just built
        arch = target.split("-")[0]
        qemu_executable = os.path.join(build_dir,
                                       target, "qemu-system-%s" % arch)
        process.run("%s --version" % qemu_executable)
