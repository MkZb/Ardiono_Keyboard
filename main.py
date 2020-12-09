from Arduino import Arduino
import time, sys
from GUI import *
from threading import Timer


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
            debounced.t = Timer(wait, call_it)
            debounced.t.start()

        return debounced

    return decorator


# debounce decorator makes our function to be executed after button release
# that allows us to only execute function once even if button is being held
@debounce(1)
def keyPressed(num):
    window.funct.func_list[num](num)

#This function for example will be executed every time we listen to the new
#analog value
def test_func():
    print("YEP holding btn")

def listen(pin: int):
    pin_analog_value = board.analogRead(pin)
    """
    BTN LAYOUT:
    5  4  3  2  1
    6  7  8  9  10
    """
    #Btn1
    if pin_analog_value < 10:
        keyPressed(1)
    #Btn2
    elif pin_analog_value < 516:
        keyPressed(2)
    elif pin_analog_value < 686:
        keyPressed(3)
    elif pin_analog_value < 771:
        keyPressed(4)
    elif pin_analog_value < 823:
        keyPressed(5)
    elif pin_analog_value < 881:
        keyPressed(6)
    elif pin_analog_value < 856:
        keyPressed(7)
    elif pin_analog_value < 899:
        keyPressed(8)
    elif pin_analog_value < 913:
        keyPressed(9)
    elif pin_analog_value < 924:
        keyPressed(10)
    # else:  # basically remove this section
    #     print("No btn pressed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # board = Arduino("115200")
    #
    # while (True):
    #     listen(0)
    #     time.sleep(0.5)  # change sleep for different frequency calls
    window.show()
    app.exec_()

