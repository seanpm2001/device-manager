import os
import pynotify
import gtk

import cream
from cream.contrib.udisks import UDisks

pynotify.init('Cream Volume Manager')

EXPIRES = 5000

class VolumeManager(UDisks, cream.Module):
    def __init__(self):
        cream.Module.__init__(self)
        UDisks.__init__(self)

        self.connect('device-mounted', self.sig_device_mounted)
        self.connect('device-removed', self.sig_device_removed)

    def sig_device_mounted(self, udisks, device, mount_path):
        n = pynotify.Notification('Device mounted!', '%s was mounted to %s.' % (device.description, mount_path))
        n.set_expires(EXPIRES)
        n.show()

    def sig_device_removed(self, udisks, device):
        n = pynotify.Notification('Device removed!', '%s was removed.' % (device.description,))
        n.set_expires(EXPIRES)
        n.show()

if __name__ == '__main__':
    service = VolumeManager()
    service.main()
