import pyautogui as pa
import time

pa.sleep(0.5)

link = "https://web.whatsapp.com/"

pa.press("win")
pa.write("edge")
pa.press("enter")
pa.sleep(0.5)
pa.write(link)
pa.press("enter")
time.sleep(5)
pa.click(x=315, y=253)
pa.write("luany freitas")
pa.press("enter")

mensagens = "eu te amo mais que tudo"
while True:
    for mensagem in mensagens:
        pa.write(mensagens)
        time.sleep(0.1)
        pa.press("enter")
        time.sleep(0.1)
z