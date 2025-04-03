import RPi.GPIO as GPIO
import time

# Ustawienia pinów
PUL_PIN = 5   # PUL - sygnał kroków
DIR_PIN = 6   # DIR - kierunek obrotu

# Ilość kroków do wykonania
steps = 100

# Czas trwania impulsu (szybkość obrotu) – im krótszy, tym szybciej
pulse_delay = 0.001  # 1 ms

# Ustawienie trybu pinów
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PUL_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

try:
    # Ustaw kierunek (True = do przodu, False = do tyłu)
    GPIO.output(DIR_PIN, True)

    # Generuj impulsy
    for _ in range(steps):
        GPIO.output(PUL_PIN, GPIO.HIGH)
        time.sleep(pulse_delay)
        GPIO.output(PUL_PIN, GPIO.LOW)
        time.sleep(pulse_delay)

    print("Ruch zakończony.")

finally:
    GPIO.cleanup()
