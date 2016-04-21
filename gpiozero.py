PINS = [False] * 100

class Pin(object):
    def __init__(self, number):
        self._number = number

    def on(self):
        self.value = True

    def off(self):
        self.value = False

    def _get_value(self):
        return PINS[self._number]

    def _set_value(self, value):
        PINS[self._number] = bool(value)
        state_changed()

    value = property(_get_value, _set_value)


class TrafficLights(object):
    def __init__(self, red_pin, amber_pin, green_pin):
        self.red = Pin(red_pin)
        self.amber = Pin(amber_pin)
        self.green = Pin(green_pin)

    def on(self):
        self.red.on()
        self.amber.on()
        self.green.on()

    def off(self):
        self.red.off()
        self.amber.off()
        self.green.off()

    def _get_value(self):
        return (self.red.value, self.amber.value, self.green.value)

    def _set_value(self, value):
        self.red.value, self.amber.value, self.green.value = value

    value = property(_get_value, _set_value)


class Button(object):
    def __init__(self, pin):
        self.when_pressed = None

    def press(self):
        if self.when_pressed is not None:
            self.when_pressed()


def lamp(color, state):
    if state:
        return '\033[40;%dm*\033[0m' % color
    else:
        return '\033[40m \033[0m'

def state_changed():
    REDS = (13, 21, 10, 7, 2, 18)
    AMBERS = (19, 20, 9, 8, 3, 15)
    GREENS = (26, 16, 11, 25, 4, 14)
    print('\033[2J') # clear screen
    print('ROAD1   ROAD2   CROSSING')
    print('   '.join(lamp(31, PINS[pin]) for pin in REDS))
    print('   '.join(lamp(33, PINS[pin]) for pin in AMBERS))
    print('   '.join(lamp(32, PINS[pin]) for pin in GREENS))

