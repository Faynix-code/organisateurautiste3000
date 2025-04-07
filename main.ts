serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    let parts: string[];
let name: string;
let value: string;
let error_msg: string;
data = serial.readUntil("\n")
    // Lit une ligne complète
    if (data) {
        data = _py.py_string_strip(data)
if (data.indexOf(",") >= 0) {
            parts = _py.py_string_split(data, ",", 1)
name = parts[0]
            value = parts[1]
            if (_py.py_string_isdigit(value)) {
                // Vérifie si la valeur est un entier
                radio.sendValue(name, parseInt(value))
                serial.writeLine("OK,Envoyé")
            } else {
                // Confirme l'envoi
                error_msg = "ERREUR, Valeur invalide: " + value
                serial.writeLine(error_msg)
                // Envoie l'erreur au logiciel
                basic.showIcon(IconNames.Yes)
            }
        }
    } else {
        error_msg = "ERREUR, Format incorrect: " + data
        serial.writeLine(error_msg)
        // Envoie l'erreur au logiciel
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendValue("commande", 1)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("EMULATION")
    emulation = !(emulation)
    while (emulation == true) {
        serial.writeValue("accelerationx", randint(0, 150))
        serial.writeValue("accelerationy", randint(0, 150))
        serial.writeValue("temperature", randint(0, 25))
        serial.writeValue("niveausonore", randint(0, 100))
        serial.writeValue("signal", randint(0, 255))
    }
})
radio.onReceivedString(function (receivedString) {
    serial.writeLine(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("commande", 2)
})
radio.onReceivedValue(function (name, value) {
    if (name == "status") {
        if (value == 1) {
            basic.showString("AUTISTE ")
            basic.clearScreen()
            basic.showIcon(IconNames.Happy)
        }
        if (value == 2) {
            basic.showString("AUTISTE")
            basic.clearScreen()
            basic.showIcon(IconNames.Sad)
        }
    }
    serial.writeValue(name, value)
    basic.pause(500)
})
let data = ""
let emulation = false
emulation = false
let data2 = ""
radio.setGroup(67)
serial.redirectToUSB()
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
basic.forever(function () {
	
})
