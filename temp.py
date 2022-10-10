from machine import Pin, ADC
from time import sleep

adc_pin = Pin(34, mode=Pin.IN)
pot = ADC(adc_pin)
pot.atten(ADC.ATTN_2_5DB)  # (for 3.3V) 100mV - 1250mV

while True:
    pot_value = pot.read()
    print("pot_value", pot_value)

    # analog value between 0 and 4096 => voltage
    vol = pot_value * 1.36 / 4096 + 0.01
    print("vol", vol)

    # voltage => temperature
    temp = (vol - 0.6)*100
    print("temp", temp)

    sleep(1)
