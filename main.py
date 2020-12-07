from Arduino import Arduino
import time
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
def test_func1():
    print("YEP pressed")

#This function for example will be executed every time we listen to the new
#analog value
def test_func2():
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
        test_func1()
    #Btn2
    elif pin_analog_value < 516:
        test_func2()
    elif pin_analog_value < 686:
        print("Btn3")
    elif pin_analog_value < 771:
        print("Btn4")
    elif pin_analog_value < 823:
        print("Btn5")
    elif pin_analog_value < 881:
        print("Btn6")
    elif pin_analog_value < 856:
        print("Btn7")
    elif pin_analog_value < 899:
        print("Btn8")
    elif pin_analog_value < 913:
        print("Btn9")
    elif pin_analog_value < 924:
        print("Btn10")
    else:  # basically remove this section
        print("No btn pressed")


if __name__ == '__main__':
    board = Arduino("115200")

    while (True):
        listen(0)
        time.sleep(0.5)  # change sleep for different frequency calls
