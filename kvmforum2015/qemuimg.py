from avocado import Test, fail_on
from avocado.utils import process

class QEMUImg(Test):

    """
    Simple qcow2 good and bad image check
    """

    @fail_on(process.CmdError)
    def test(self):
        good_image = self.get_data_path('good.qcow2')
        process.run("qemu-img info %s" % good_image)
        process.run("qemu-img check %s" % good_image)

        def bad():
            bad_image = self.get_data_path('bad.qcow2')
            process.run("qemu-img info %s" % bad_image)
        self.assertRaises(process.CmdError, bad)
