Y = 0
X = 0

def on_forever():
    global Y, X
    Y = 4
    while Y <= 4:
        if Y % 2 == 0:
            X = 4
            while X <= 4:
                led.plot(X, Y)
                basic.pause(500)
                X += -1
                if X < 0:
                    Y += -1
                    break
        else:
            while Y <= 4:
                X = 0
                while X <= 4:
                    led.plot(X, Y)
                    basic.pause(500)
                    X += 1
                    if X > 4:
                        Y += -1
                        break
basic.forever(on_forever)
