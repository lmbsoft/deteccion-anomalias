from pynput import mouse, keyboard
from pynput.keyboard import Key  # Importa la clase Key
import time
import random

def mover_mouse():
    controller = mouse.Controller()
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    controller.move(x, y)

def presionar_tecla():
    controller = keyboard.Controller()
    # Usa Key para las teclas especiales
    key = random.choice(['a', 'b', 'c', Key.shift, Key.ctrl, Key.alt])
    controller.press(key)
    controller.release(key)

if __name__ == "__main__":
    try:
        while True:
            accion = random.choice([mover_mouse, presionar_tecla])
            accion()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Simulador de actividad detenido.")

