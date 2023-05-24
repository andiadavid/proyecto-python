import PySimpleGUI as sg
import os

#ruta general
os_path = os.path.realpath('.') 
#ruta de la carpeta img y imagen logo 
path_image = os.path.join(os_path,'img','signoSuma.img')
#ruta de la carpeta y archivo json con los perfiles 
path_json = os.path.join(os_path,'data','perfiles.josn') 

#ventana
def create_window():
    layout = [
        [sg.Text('primer texto')]
    ]
    window_created = sg.Window('PANTALL INICIO',layout)
    return window_created

def start():
    window=create_window()
    
    #ok=funciones.abrir_json()

    while True:
        event, values = window.read()
        print(f"evento: {event}")
        if(event == sg.WIN_CLOSED):
            print(f"evento cerrar: {event}")
            break
    window.close()

if __name__ == '__main__':
    start()

