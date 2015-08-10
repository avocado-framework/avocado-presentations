from avocado import Test, fail_on
from avocado.utils import process

class BindMount(Test):

    @fail_on(process.CmdError)
    def test_mount(self):
        if "/srv/tmp" in open("/proc/mounts").read():
            process.run("umount /srv/tmp")

        process.run("mount /srv/tmp")
        self.assertIn("/srv/tmp", open("/proc/mounts").read())

    @fail_on(process.CmdError)
    def test_umount(self):
        if not "/srv/tmp" in open("/proc/mounts").read():
            process.run("mount /srv/tmp")

        process.run("umount /srv/tmp")
        self.assertNotIn("/srv/tmp", open("/proc/mounts").read())
