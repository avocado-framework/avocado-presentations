from avocado import Test, fail_on
from avocado.utils import process

class BindMount(Test):

    @fail_on
    def test_mount(self):
        # Please don't actually write your test like this
        process.run("grep -q -v /srv/tmp /proc/mounts || umount /srv/tmp",
                    shell=True)
        process.run("mount /srv/tmp")
        process.run("grep /srv/tmp /proc/mounts")

    @fail_on
    def test_umount(self):
        # Please don't actually write your test like this
        process.run("grep -q /srv/tmp /proc/mounts || mount /srv/tmp",
                    shell=True)
        process.run("umount /srv/tmp")
        process.run("grep -v /srv/tmp /proc/mounts")
