import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button(button_text='Add item')
window = sg.Window('MY to-do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()