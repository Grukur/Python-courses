import PySimpleGUI as sg

sg.theme('BrightColors')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Corrovoremos tu rut :D')],
          [sg.Text('Ingresa tu rut sin guion ni codigo verificador'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Salir')]]


# Create the Window
window = sg.Window('Rutificador 3.0', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'Salir']:  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    for _ in range(1):
        rut = values[0]
        lista = [int(x) for x in str(rut)]
        lista.reverse()

        ctrl = [2, 3, 4, 5, 6, 7, 2, 3, 4]
        ver = 11 - sum(ctrl[i] * lista[i] for i in range(len(rut))) % 11

        if ver == 10 and 9 > len(rut) > 6:
            print("Tu RUT es: ", rut, "-", "K", "\n")
            sg.popup(f'Tu rut es: {rut} - {ver}')
        elif ver == 11 and 9 > len(rut) > 6:
            print("Tu RUT es: ", rut, "-", "0", "\n")
            sg.popup(f'Tu rut es: {rut} - {ver}')
        elif 0 < ver < 10 and 9 > len(rut) > 6:
            print("Tu RUT es: ", rut, "-", ver, "\n")
            sg.popup(f'Tu rut es: {rut} - {ver}')
        else:
            print("Tu RUT no existe")
            break
window.close()