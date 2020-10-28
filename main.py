maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
basic.pause(maqueen.ultrasonic(PingUnit.CENTIMETERS))
maqueen.motor_stop(maqueen.Motors.ALL)

def on_forever():
    pass
    maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever)
