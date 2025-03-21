
import openpyxl
from urllib import quote
import webbrowser
import time
import pillow
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
time.sleep(30)
workbook= openpyxl.load_workbook('clientes.xlsx')   
page_clients= workbook['Shee1']

for l in page_clients.iter_rows(min_row=2):
    name= l[0].value
    phone= l[1].value
    venc= l[2].value
    message= f'Olá {name} seu boleto vence no dia {venc.strftime('%d/%m/%Y')}. Favor pagar no link: https://www.link_exemplo.com'
    
    try: 
        link_message_whatsapp= f'https://web.whatsapp.com/send? phone{phone}&text={quote(message)}'
        
        webbrowser.open(link_message_whatsapp)
        time.sleep(15)
        
        send= pyautogui.locateCenterOnScreen('seta.png')
        time.sleep(5)       
        
        pyautogui.click(send[0], send[1])
        time.sleep(5)
        
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(5)
    except: 
        
        print(f"Não foi possível enviar mensagem para {name}")
        
        with open('errors.csv', 'a', newline='', encoding='utf-8') as file:
            
            file.write(f'{name}, {phone}')
    














