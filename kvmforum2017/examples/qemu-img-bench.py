import os

from avocado import Test
from avocado.utils import process


class QemuImgBench(Test):

    def setUp(self):
        self.qemu_img = self.params.get("qemu_img", "*", default="/usr/bin/qemu-img")
        self.img_path = os.path.join(self.workdir, "img.img")
        process.run("%s create %s 1G" % (self.qemu_img, self.img_path))

    def test_count_positive(self):
        cmd = "%s bench -c 1 %s" % (self.qemu_img, self.img_path)
        process.run(cmd)

    def test_count_negative(self):
        cmd = "%s bench -c -1 %s" % (self.qemu_img, self.img_path)
        self.assertRaises(process.CmdError, process.run, cmd)

    def test_count_zero(self):
        # While it's debatable if a count of zero is valid or not for
        # this specific operation, let's assume it's not.
        #
        # This will only PASS with a patched version of qemu-img
        #
        cmd = "%s bench -c 0 %s" % (self.qemu_img, self.img_path)
        self.assertRaises(process.CmdError, process.run, cmd)
