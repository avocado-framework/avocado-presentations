from avocado import Test, fail_on
from avocado.utils import process

class BindMount(Test):

    DEFAULT_MOUNT_POINT = "/srv/tmp"

    @fail_on(process.CmdError)
    def test_mount(self):
        mount_point = self.params.get("mountpoint", default=self.DEFAULT_MOUNT_POINT)
        process.run("mount %s" % mount_point)
        self.assertIn(mount_point, open("/proc/mounts").read())

    @fail_on(process.CmdError)
    def test_umount(self):
        mount_point = self.params.get("mountpoint", default=self.DEFAULT_MOUNT_POINT)
        if not mount_point in open("/proc/mounts").read():
            process.run("mount %s" % mount_point)

        process.run("umount %s" % mount_point)
        self.assertNotIn(mount_point, open("/proc/mounts").read())
