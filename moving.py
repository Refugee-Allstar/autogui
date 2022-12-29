import pyautogui
import PySimpleGUI as sg
from time import sleep

print("Welcome")    



sg.theme('BluePurple')

layout = [[sg.Text('Move the mouse to the top left corner of your screen to stop. There is a 3 second pause at the end of each loop to do this.'),
		[sg.Button('Start Moving')]]]

window = sg.Window('Introduction', layout)

while True:
    event, values = window.read()
    print(event, values)
	
    if event in (None, 'Exit'):
        break
	
    if event == 'Start Moving':
        while(1):
            pyautogui.click(478,363,duration=1)
            pyautogui.moveTo(177,58,duration=1)
            pyautogui.press('b')  
            sleep(3)

window.close()



	

