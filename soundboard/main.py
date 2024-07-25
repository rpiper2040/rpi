import machine
import time

uart = machine.UART(0, baudrate=9600, tx=0, rx=1)  # UART setup

START_BYTE = 0x7E
VERSION_BYTE = 0xFF
COMMAND_LENGTH = 0x06
END_BYTE = 0xEF
ACKNOWLEDGE = 0x00
ACTIVATED = 0

button1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

def execute_cmd(CMD, Par1, Par2):
    checksum = -(VERSION_BYTE + COMMAND_LENGTH + CMD + ACKNOWLEDGE + Par1 + Par2)
    command_line = bytearray([START_BYTE, VERSION_BYTE, COMMAND_LENGTH, CMD, ACKNOWLEDGE, Par1, Par2, checksum >> 8, checksum & 0xFF, END_BYTE])
    uart.write(command_line)

def play_first():
    execute_cmd(0x3F, 0, 0)
    time.sleep(0.5)
    set_volume(30)
    time.sleep(0.5)

def set_volume(volume):
    execute_cmd(0x06, 0, volume)
    time.sleep(2)
print("333")
play_first()
print("444")
while True:
    if button1.value() == ACTIVATED:
        execute_cmd(0x03, 0, 1)
        print("5a")
        time.sleep(0.5)
    if button2.value() == ACTIVATED:
        execute_cmd(0x03, 0, 3)
        time.sleep(0.5)
    if button3.value() == ACTIVATED:
        execute_cmd(0x03, 0, 2)
        time.sleep(0.5)


