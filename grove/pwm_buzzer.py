import time
from grove.factory import Factory

buzzer = Factory.getGpioWrapper("Buzzer", 12)

buzzer.on()
time.sleep(1)
buzzer.off()
