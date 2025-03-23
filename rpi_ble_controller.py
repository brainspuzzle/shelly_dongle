import serial
from bluepy.btle import Scanner
import subprocess

UART_PORT = '/dev/serial0'
BAUD_RATE = 9600

uart = serial.Serial(UART_PORT, baudrate=BAUD_RATE, timeout=1)

def scan_shelly_devices(duration=5):
    scanner = Scanner()
    devices = scanner.scan(duration)
    shelly_devices = []
    for dev in devices:
        name = dev.getValueText(9)
        addr = dev.addr
        rssi = dev.rssi
        if name and "Shelly" in name:
            shelly_devices.append(f"{addr},{name},{rssi} dBm")
    return shelly_devices

def send(msg):
    uart.write(f"{msg}\n".encode())

def main():
    send("Raspberry Pi BLE Controller paleistas. Laukiama komandu.")
    while True:
        if uart.in_waiting > 0:
            cmd = uart.readline().decode().strip()
            if cmd == "scan":
                send("BLE_Scan_pradetas")
                devices = scan_shelly_devices()
                if devices:
                    for dev in devices:
                        send(f"Shelly,{dev}")
                else:
                    send("Shelly_irenginiai_nerasta")
                send("BLE_Scan_baigtas")
            elif cmd == "status":
                send("RaspberryPi_aktyvus_ir_pasiekiamas")
            elif cmd == "restart":
                send("RaspberryPi_bus_perkrautas")
                subprocess.run(["sudo", "reboot"])
            else:
                send(f"Nezinoma_komanda:{cmd}")

if __name__ == "__main__":
    main()