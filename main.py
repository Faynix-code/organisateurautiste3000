def on_data_received():
    global data
    data = serial.read_until("\n")
    # Lit une ligne complète
    if data:
        data = data.strip()
        if data.index_of(",") >= 0:
            parts = data.split(",", 1)
            name = parts[0]
            value = parts[1]
            if value.isdigit():
                # Vérifie si la valeur est un entier
                radio.send_value(name, int(value))
                serial.write_line("OK,Envoyé")
            else:
                # Confirme l'envoi
                error_msg = "ERREUR, Valeur invalide: " + value
                serial.write_line(error_msg)
                # Envoie l'erreur au logiciel
                basic.show_icon(IconNames.YES)
    else:
        error_msg = "ERREUR, Format incorrect: " + data
        serial.write_line(error_msg)
        # Envoie l'erreur au logiciel
        basic.show_icon(IconNames.NO)
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

def on_button_pressed_a():
    radio.send_value("commande", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global emulation
    basic.show_string("EMULATION")
    emulation = not (emulation)
    while emulation == True:
        serial.write_value("accelerationx", randint(0, 150))
        serial.write_value("accelerationy", randint(0, 150))
        serial.write_value("temperature", randint(0, 25))
        serial.write_value("niveausonore", randint(0, 100))
        serial.write_value("signal", randint(0, 255))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    serial.write_line(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_value("commande", 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name2, value2):
    if name2 == "status":
        if value2 == 1:
            basic.show_string("AUTISTE ")
            basic.clear_screen()
            basic.show_icon(IconNames.HAPPY)
        if value2 == 2:
            basic.show_string("AUTISTE")
            basic.clear_screen()
            basic.show_icon(IconNames.SAD)
    serial.write_value(name2, value2)
    basic.pause(500)
radio.on_received_value(on_received_value)

data = ""
emulation = False
emulation = False
data2 = ""
radio.set_group(67)
serial.redirect_to_usb()
music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.IN_BACKGROUND)

def on_forever():
    pass
basic.forever(on_forever)
