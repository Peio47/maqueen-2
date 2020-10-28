maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
basic.pause(maqueen.Ultrasonic(PingUnit.Centimeters))
maqueen.motorStop(maqueen.Motors.All)
basic.forever(function on_forever() {
    
    maqueen.motorStop(maqueen.Motors.All)
})
