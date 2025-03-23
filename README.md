# 🧠 Shelly BLE Dongle – by brainspuzzle

**Shelly BLE Dongle** – tai Raspberry Pi pagrindu veikiantis automatinio Shelly įrenginių aptikimo ir konfigūravimo įrankis, valdantis viską per BLE ir RPC.

Šis projektas leidžia sukurti *donglą*, kuris:
- Aptinka Shelly Gen2/Gen3 įrenginius per **BLE**
- Komunikuoja su **Arduino Uno R3** per **UART**
- Siunčia rezultatus atgal į Arduino
- Automatiškai veikia kaip **systemd servisas**

---

## ⚙️ Architektūra

```text
[Arduino Uno R3] <--UART--> [Raspberry Pi Zero W2]
                                  |
                                  +--> BLE Scanner (bluepy)
                                  +--> UART listener (pyserial)
