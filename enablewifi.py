import argparse
from bluepy.btle import UUID, Peripheral

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ceyomur wifi enabler")
    parser.add_argument("--addr", dest="addr", type=str, help="Address of trail camera", required=True)

    args = parser.parse_args()
    p = Peripheral(args.addr, "public")
    serv = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    c = serv.getCharacteristics()[0]
    c.write(bytes('GPIO3','utf-8'))
