import os

from avocado import Test, fail_on
from avocado.utils import process


class QemuImgConvert(Test):

    def setUp(self):
        self.qemu_img = self.params.get("qemu_img", "*", default="/usr/bin/qemu-img")
        self.input_filename = os.path.join(self.workdir, "input.img")
        self.fmt = self.params.get("fmt", "*", default="raw")
        self.input_size = self.params.get("input_size", "*", default="1G")
        cmd = "%s create -f %s %s %s" % (self.qemu_img,
                                         self.fmt,
                                         self.input_filename,
                                         self.input_size)
        process.run(cmd)

    @fail_on(process.CmdError)
    def test(self):
        output_fmt = self.params.get("output_fmt", "*", default="raw")
        output_filename = os.path.join(self.workdir, "output.img")
        cache = self.params.get("cache", "*", default="writeback")
        src_cache = self.params.get("src_cache", "*", default="writeback")
        compressed = self.params.get("compressed", "*", default="off")
        if compressed == "on":
            compressed_opt = "-c"
        else:
            compressed_opt = ""
        cmd = "%s convert -f %s -O %s -t %s -T %s %s %s %s"
        cmd %= (self.qemu_img,
                self.fmt,
                output_fmt,
                cache,
                src_cache,
                compressed_opt,
                self.input_filename,
                output_filename)
        process.run(cmd)
