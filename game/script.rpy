# Dodaj to na początku swojego skryptu
default show_more_buttons = False


screen first_button_screen:
    # Przyciski do testów
    textbutton "Kliknij mnie" action [Hide("first_button_screen"), Jump("firestorm")]:
        xalign 0.8
        yalign 0.5
        background "#f00"




# Definiujemy ekran z przyciskiem tekstowym do testu
 # Czerwone tło debugowe dla widoczności

# Label po naciśnięciu przycisku

return

# W `script.rpy` na początek testowego uruchomienia gry
label start:

    # Testowe wyświetlenie obrazów
    scene black  # Wstawienie tła, by lepiej widzieć obrazy
    show image "gui/lg_idle.png"
    pause 1
    show image "gui/ls_idle.png"
    pause 1
    show image "gui/ld_idle.png"
    pause 1
    show image "gui/pd_idle.png"
    pause 1

    "Jeśli widzisz obrazy, oznacza to, że są prawidłowo ładowane."
    return


return