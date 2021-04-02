import sys
from bluepy.btle import UUID, Peripheral, DefaultDelegate

def enable_notify(peri,  chara_uuid):
    setup_data = b"\x01\x00"
    notify = peri.getServiceByUUID(list(services)[2].uuid).getCharacteristics(chara_uuid)[0]
    notify_handle = notify.getHandle() + 1
    peri.writeCharacteristic(notify_handle, setup_data, withResponse=True)

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        print(cHandle)
        print(data)

if len(sys.argv) != 2:
  print "Fatal, must pass device address:", sys.argv[0], "<device address="">"
  quit()

p = Peripheral(sys.argv[1],"public")
p.setDelegate(MyDelegate())
services = p.getServices()
enable_notify(p, list(services)[2].getCharacteristics()[0].uuid)

while True:
    if p.waitForNotifications(5.0):
        continue

    print ('waiting')
