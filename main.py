from Arduino import Arduino
import time, sys
from GUI import *
import threading


def debounce(wait):
    """ Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """

    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)

            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = threading.Timer(wait, call_it)
            debounced.t.start()

        return debounced

    return decorator


# debounce decorator makes our function to be executed after button release
# that allows us to only execute function once even if button is being held
@debounce(0.3)
def keyPressed(num):
    print(num)
    window.funct.func_list[num - 1](num)


# This function for example will be executed every time we listen to the new
# analog value
def test_func():
    print("YEP holding btn")


def listen(pin: int):
    pin_analog_value = board.analogRead(pin)
    # handle = open('test.txt', 'r')
    # pin_analog_value = int(handle.read())
    # handle.close()
    """
    BTN LAYOUT:
    5  4  3  2  1
    6  7  8  9  10
    """
    if pin_analog_value < 10:
        keyPressed(5)
    elif pin_analog_value < 516:
        keyPressed(4)
    elif pin_analog_value < 686:
        keyPressed(3)
    elif pin_analog_value < 771:
        keyPressed(2)
    elif pin_analog_value < 823:
        keyPressed(1)
    elif pin_analog_value < 856:
        keyPressed(6)
    elif pin_analog_value < 881:
        keyPressed(7)
    elif pin_analog_value < 899:
        keyPressed(8)
    elif pin_analog_value < 913:
        keyPressed(9)
    elif pin_analog_value < 924:
        keyPressed(10)


class ListenArduino(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while (True):
            listen(0)
            time.sleep(0.2)  # change sleep for different frequency calls


if __name__ == '__main__':
    board = Arduino("115200")
    app = QApplication(sys.argv)
    window = MainWindow()
    thread1 = ListenArduino()
    thread1.start()
    window.show()
    app.exec_()
