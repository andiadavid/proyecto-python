import PySimpleGUI as sg
import os

os_path = os.path.realpath('.')
image_path = os.path.join(os_path,'avatar')

def create_window():
    Layout = [
        [sg.Text(' '*135)],
        [sg.Popup('hola mundo')],
        [sg.FileBrowse('seleccionar un nuevo avatar: ',initial_folder=image_path)],
        [sg.Text(' '*135)]]
    edit_window = sg.Window("titulo: ",Layout,margins=(10,30))
    return edit_window 

window = create_window()
while True: 
    event, values = window.read()
    print(f"Evento: {event}, Values: {values}")
    if(event == sg.WIN_CLOSED):
        break
window.close()
