let Y = 0
let X = 0
basic.forever(function () {
    Y = 4
    while (Y <= 4) {
        X = 4
        if (true) {
            while (X <= 4) {
                led.plot(X, Y)
                basic.pause(500)
                X += -1
                if (X < 0) {
                    Y += -1
                    break;
                }
            }
        }
    }
})
