Y = 0
X = 0

def on_forever():
    global Y, X
    while True:
        Y = 4
        while Y <= 4:
            X = 4
            while X <= 4:
                led.plot(X, Y)
                basic.pause(500)
                X += -1
            Y += -1
        basic.clear_screen()
basic.forever(on_forever)
