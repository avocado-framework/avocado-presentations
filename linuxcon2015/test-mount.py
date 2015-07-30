from avocado import Test, fail_on
from avocado.utils import process

class BindMount(Test):

    @fail_on
    def test(self):
        process.run("mount /srv/tmp")
        process.run("grep /srv/tmp /proc/mounts")
        process.run("umount /srv/tmp")
        process.run("grep -v /srv/tmp /proc/mounts")
