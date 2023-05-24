import PySimpleGUI as sg
import os 

#ruta general
os_path = os.path.realpath('.')   
path_img = os.path.join(os_path,'img')
path_avatar = os.path.join(os_path,'avatar')

nick = 'david'
avatar = os.path.join(path_avatar,'avatar_1.png')
    
def create_window():
    #avatar,nick,config y help images
    menu_profile = avatar
    print('avatar: ',avatar)
    menu_nick = nick
    print('nick: ',nick)
    menu_config = os.path.join(path_img,'config.img')
    menu_help = os.path.join(path_img,'help.img')

    #main menu buttons system
    profile_button = sg.Button(
        key= '-PROFILE-',
        image_source= menu_profile)
    
    config_button = sg.Button(
        key= '-CONFIG-',
        image_source= menu_config)
    
    help_button = sg.Button(
        key= '-HELP-',
        image_source=menu_help)
    
    #menu buttons
    tag_button = sg.Button(
        key= '-ETIQUETAR-',
        button_text= 'tag images')
    
    meme_button = sg.Button(
        key= '-MEME-',
        button_text= 'generate meme')
    
    collage_button = sg.Button(
        key= '-COLLAGE-',
        button_text= 'generate collage')  
    
    salir_button = sg.Button(
        key= '-SALIR-',
        button_text= 'salir')

    #layout
    menu_layout = [[profile_button, sg.Text(' '*90), config_button, help_button],
        [menu_nick],
        [tag_button],
        [meme_button],
        [collage_button],
        [salir_button]]

    #window creation 
    menu_window = sg.Window("menu", menu_layout, margins=(15,30))
    print(menu_window)
    return menu_window

#def main_menu():
    #lllamo al crear ventana con datos de un solo perfil
window = create_window()
    
while True:
    event, values = window.read()
    print(f'evento: {event}, valores{values}')
    if event == sg.WIN_CLOSED:
        break
    
window.close()    


#if __name__ == '__main__':
#    main_menu()