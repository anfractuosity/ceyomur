from bluepy.btle import UUID, Peripheral

p = Peripheral("MAC","public")
serv = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
c = serv.getCharacteristics()[0]
c.write(bytes('GPIO3','utf-8'))
