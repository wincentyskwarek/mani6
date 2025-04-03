
import RPi.GPIO as GPIO
import time

# Ustawienia pinów
PUL_PIN1 = 5   # PUL - sygnał kroków
DIR_PIN1 = 6   # DIR - kierunek obrotu
PUL_PIN2 = 17   # PUL - sygnał kroków
DIR_PIN2 = 27   # DIR - kierunek obrotu
# Ilość kroków do wykonania
steps = 5000

# Czas trwania impulsu (szybkość obrotu) – im krótszy, tym szybciej
pulse_delay = 0.0005  # 1 ms

# Ustawienie trybu pinów
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PUL_PIN1, GPIO.OUT)
GPIO.setup(DIR_PIN1, GPIO.OUT)
GPIO.setup(PUL_PIN2, GPIO.OUT)
GPIO.setup(DIR_PIN2, GPIO.OUT)

try:
    # Ustaw kierunek (True = do przodu, False = do tyłu)
    GPIO.output(DIR_PIN1, False)
    GPIO.output(DIR_PIN2, False)

    # Generuj impulsy
    for _ in range(steps):
        GPIO.output(PUL_PIN1, GPIO.HIGH)
        time.sleep(pulse_delay)
        GPIO.output(PUL_PIN1, GPIO.LOW)
        time.sleep(pulse_delay)
    for _ in range(steps):
        GPIO.output(PUL_PIN2, GPIO.HIGH)
        time.sleep(pulse_delay)
        GPIO.output(PUL_PIN2, GPIO.LOW)
        time.sleep(pulse_delay)
    print("Ruch zakończony.")

finally:
    GPIO.cleanup()
